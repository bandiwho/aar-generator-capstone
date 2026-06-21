from aar_generator.schemas import IncidentInput


SYSTEM_PROMPT = """
You are a security incident postmortem assistant. Produce professional,
fact-grounded after-action report drafts from user-provided incident details.
Do not invent facts. Mark uncertain conclusions as assumptions or open
questions. Use the 5 Whys method for root cause analysis.
""".strip()


def build_report_prompt(data: IncidentInput) -> str:
    """Build the prompt for the AAR draft."""
    # TODO: Week 3 - Add few-shot examples for ransomware, phishing, and cloud misconfiguration incidents.
    # TODO: Week 4 - Request strict JSON first, then render Markdown from validated sections.
    # TODO: Week 5 - Include prior reviewer feedback when the revision workflow is implemented.
    audience_guidance = {
        "technical": (
            "Write for a technical security and IT audience. Include concrete "
            "technical details, likely control gaps, evidence references, and "
            "specific remediation tasks."
        ),
        "executive": (
            "Write for executives. Focus on business impact, risk, decisions, "
            "accountability, and high-level corrective actions. Avoid excessive jargon."
        ),
    }[data.audience.value]

    return f"""
Create a security incident after-action report draft.

Audience guidance:
{audience_guidance}

Required report sections:
1. Executive Summary
2. Incident Overview
3. Detection and Escalation
4. Timeline of Events
5. Impact Assessment
6. Evidence and Log Observations
7. 5 Whys Root Cause Analysis
8. Technical Root Cause
9. Process and Communication Gaps
10. Remediation Completed
11. Recommendations and Owners
12. Lessons Learned
13. Open Questions

Incident title:
{data.title}

Incident date:
{data.incident_date}

Detection source:
{data.detection_source or "Not provided."}

Affected assets:
{data.affected_assets or "Unknown or not provided."}

Incident summary:
{data.incident_summary}

Timeline:
{data.timeline}

Log snippets:
{data.log_snippets or "No log snippets provided."}

Remediation steps:
{data.remediation_steps}

Known impact:
{data.known_impact or "Unknown or not provided."}

Lessons learned:
{data.lessons_learned or "None provided."}

Open questions:
{data.open_questions or "None provided."}

Rules:
- Do not claim certainty when the evidence is incomplete.
- Put assumptions and missing evidence in the Open Questions section.
- Keep recommendations actionable.
- Assign likely owners or owner groups for recommendations when the input supports it.
- Use Markdown headings and bullet lists.
""".strip()

