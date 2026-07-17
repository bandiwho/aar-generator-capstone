from aar_generator.schemas import IncidentInput


SYSTEM_PROMPT = """
You are a security incident postmortem assistant. Produce professional,
fact-grounded after-action report drafts from user-provided incident details.
Do not invent facts. Mark uncertain conclusions as assumptions or open
questions. Use the 5 Whys method for root cause analysis.
""".strip()


def build_report_prompt(data: IncidentInput) -> str:
    """Build the prompt for the AAR draft."""
    # Future enhancement: add few-shot examples and structured JSON rendering.
    # Future enhancement: include prior reviewer feedback if revision workflow is added.
    audience_guidance = {
        "technical": (
            "Write for a technical security and IT audience. Include concrete "
            "technical details, likely control gaps, evidence references, and "
            "specific remediation tasks."
        ),
        "executive": (
            "Write for executives. Focus on business impact, risk, decisions, "
            "accountability, and high-level corrective actions. Avoid excessive jargon. "
            "Summarize technical evidence in plain language instead of emphasizing raw log syntax."
        ),
    }[data.audience.value]

    return f"""
Create a security incident after-action report draft.

Audience guidance:
{audience_guidance}

Required report sections:
1. Report Summary
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

Incident type:
{data.incident_type or "Not provided."}

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
- Start every bullet with a complete, capitalized sentence.
- Do not repeat labels such as **Gap:**, **Task:**, or **Recommendation:** at the start of every bullet.
- Do not start every remediation bullet with repeated phrases such as "The security team".
- Let the section heading provide the category, then write clean bullet text underneath it.
- Do not split one recommendation sentence into several lowercase bullet fragments.
- If a recommendation has subconditions, keep them in the same bullet sentence or use capitalized sub-bullets.
- In Recommendations and Owners, put the owner at the end of the same recommendation bullet using "**Owner:** Team or role".
- End the report with the Open Questions section content only.
- Do not add chat-style closing offers such as "If you share additional details, I can revise this draft."
- In Open Questions, write the unresolved question first, followed by one short evidence note if needed.
- Do not repeat lead-in labels such as "Open item:" or "Assumption:" in the Open Questions section.
- Use "Evidence:" instead of "Evidence note:" when adding support under an open question.
- Do not add new Open Questions unless they are directly supported by the incident details.
""".strip()

