import re

from aar_generator.config import Settings
from aar_generator.llm_client import LlmClient
from aar_generator.prompts import build_report_prompt
from aar_generator.schemas import IncidentInput, ReportResponse


class ReportService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.llm_client = LlmClient(settings)

    def generate_report(self, incident: IncidentInput) -> ReportResponse:
        # TODO: Week 4 - Validate generated report sections before returning to the UI.
        # TODO: Week 6 - Add export adapters for Markdown, DOCX, and PDF.
        prompt = build_report_prompt(incident)
        used_mock = self.settings.mock_llm or not self.settings.openai_api_key
        model_used = self.settings.openai_model
        if self.settings.mock_llm or not self.settings.openai_api_key:
            report_markdown = self._build_mock_report(incident)
        else:
            try:
                report_markdown = self.llm_client.generate(prompt)
                model_used = self.llm_client.last_model_used or self.settings.openai_model
            except Exception:
                report_markdown = self._build_mock_report(incident)
                used_mock = True
        report_markdown = self._clean_report_markdown(report_markdown)
        return ReportResponse(
            title=incident.title,
            audience=incident.audience,
            model_used=model_used,
            mock_mode=used_mock,
            report_markdown=report_markdown,
        )

    def _build_mock_report(self, incident: IncidentInput) -> str:
        audience_label = incident.audience.value.title()
        audience_note = {
            "technical": "This draft keeps technical evidence, system details, and remediation tasks visible.",
            "executive": "This draft emphasizes business impact, risk, accountability, and decision points.",
        }[incident.audience.value]
        five_whys = self._build_five_whys(incident)

        return f"""
## Report Summary

{incident.title} was reviewed as a security incident after-action report draft. {audience_note}

## Incident Overview

- Incident date: {incident.incident_date}
- Incident type: {incident.incident_type or "Not provided"}
- Audience style: {audience_label}
- Summary: {incident.incident_summary}

## Timeline of Events

{incident.timeline}

## Impact Assessment

{incident.known_impact or "Impact is not confirmed yet. This should stay listed as an open item until the team verifies it."}

## Evidence and Log Observations

{incident.log_snippets or "No log snippets were provided. Add alert text, authentication logs, ticket notes, or firewall events before the final report."}

## 5 Whys Root Cause Analysis

{five_whys}

## Technical Root Cause

The final root cause should be confirmed from logs, timeline evidence, and remediation notes. Do not state a final cause until the team can support it with evidence.

## Process and Communication Gaps

- Confirm who owned detection, containment, recovery, and follow-up.
- Confirm whether escalation steps were clear.
- Confirm whether documentation was updated during the incident.

## Remediation Completed

{incident.remediation_steps}

## Recommendations and Owners

- Assign an incident owner to confirm the final root cause using timeline, log, and remediation evidence.
- Assign the security operations team to verify affected accounts, systems, data exposure, and containment status.
- Assign a process owner to track remediation tasks, due dates, validation evidence, and follow-up review.

## Open Questions

{incident.open_questions or "No open questions were listed. Add unresolved facts before final submission if anything is uncertain."}

## Lessons Learned

- Keep report conclusions tied to evidence.
- Separate confirmed facts from assumptions.
- Track recommendations by owner and due date.
- Preserve screenshots, logs, and test results for the final capstone documentation.
""".strip()

    def _build_five_whys(self, incident: IncidentInput) -> str:
        incident_type = incident.incident_type or "the reported security incident"
        detection_source = incident.detection_source or "the available monitoring and reporting sources"
        affected_assets = incident.affected_assets or "the affected systems and users"
        first_timeline_event = self._sentence_fragment(self._first_line(incident.timeline))
        evidence_note = self._sentence_fragment(self._first_line(incident.log_snippets)) or "additional evidence should be collected before the final root cause is confirmed"
        remediation_note = self._sentence_fragment(self._first_line(incident.remediation_steps))
        impact_note = self._sentence_fragment(self._first_line(incident.known_impact)) or "impact still needs final confirmation"
        open_question_note = self._sentence_fragment(self._first_line(incident.open_questions)) or "the team should document any remaining unknowns before final submission"

        return "\n".join(
            [
                f"1. Why did the incident happen? The incident was recorded as {incident_type}. First known event: {first_timeline_event}",
                f"2. Why was it detected? Detection came from {detection_source}. Supporting evidence: {evidence_note}",
                f"3. Why did it affect the organization? Affected scope: {affected_assets}. Current impact notes: {impact_note}",
                f"4. Why did existing controls not fully prevent it? Response action reviewed: {remediation_note}. This suggests controls, monitoring, or response steps need review.",
                f"5. Why could it happen again? Remaining open issue: {open_question_note} This should become a tracked recommendation with an owner and due date.",
            ]
        )

    @staticmethod
    def _first_line(value: str) -> str:
        for line in value.splitlines():
            stripped = line.strip()
            if stripped:
                return stripped
        return ""

    @staticmethod
    def _sentence_fragment(value: str) -> str:
        return value.strip().rstrip(".")

    @staticmethod
    def _clean_report_markdown(report_markdown: str) -> str:
        mojibake_replacements = {
            "â€œ": '"',
            "â€": '"',
            "â€˜": "'",
            "â€™": "'",
            "â€“": "-",
            "â€”": "-",
            "â€¦": "...",
        }
        for broken_text, clean_text in mojibake_replacements.items():
            report_markdown = report_markdown.replace(broken_text, clean_text)

        label_pattern = re.compile(
            r"^(\s*[-*]\s+)(?:\*\*)?(Gap|Task):(?:\*\*)?\s+",
            re.IGNORECASE | re.MULTILINE,
        )
        report_markdown = label_pattern.sub(r"\1", report_markdown)
        security_team_pattern = re.compile(
            r"^(\s*(?:[-*]\s+)?)(The security team\s+)([a-z])",
            re.IGNORECASE | re.MULTILINE,
        )
        report_markdown = security_team_pattern.sub(
            lambda match: f"{match.group(1)}{match.group(3).upper()}",
            report_markdown,
        )
        open_item_pattern = re.compile(
            r"^(\s*(?:[-*]\s+)?)(?:\*\*)?(Open item|Assumption):(?:\*\*)?\s+",
            re.IGNORECASE | re.MULTILINE,
        )
        report_markdown = open_item_pattern.sub(r"\1", report_markdown)
        evidence_note_pattern = re.compile(
            r"^(\s*(?:[-*]\s+)?(?:\*\*)?Evidence)\s+note(\s*:(?:\*\*)?\s+)",
            re.IGNORECASE | re.MULTILINE,
        )
        report_markdown = evidence_note_pattern.sub(r"\1\2", report_markdown)
        chat_closing_pattern = re.compile(
            r"\n*\s*If you share additional[\s\S]*?(?:reduce assumptions|revise this draft)\.?\s*$",
            re.IGNORECASE,
        )
        return chat_closing_pattern.sub("", report_markdown).rstrip()
