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

        return f"""
## Executive Summary

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

1. Why did the incident happen? The available notes suggest a security control or process gap needs review.
2. Why was the issue detected at that time? The timeline should be compared against monitoring and alerting coverage.
3. Why was the impact limited or expanded? The team should verify affected systems, users, and data exposure.
4. Why did existing controls not fully prevent the event? The team should review access controls, MFA, patching, and response procedures.
5. Why could this happen again? Any repeated technical or process weakness should become a tracked recommendation.

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
