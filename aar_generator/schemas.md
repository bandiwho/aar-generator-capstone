## Request JSON (frontend → backend)

Required fields: title, incident_date, audience, incident_summary, timeline, remediation_steps
Optional fields: detection_source, affected_assets, log_snippets, known_impact, lessons_learned, open_questions

```json
{
  "title": "string",
  "incident_date": "2026-06-19",
  "audience": "technical | executive",
  "detection_source": "string",
  "affected_assets": "string",
  "incident_summary": "string",
  "timeline": [
    { "time": "8:10 AM", "event": "string" }
  ],
  "remediation_steps": ["string"],
  "log_snippets": ["string"],
  "known_impact": "string",
  "lessons_learned": ["string"],
  "open_questions": ["string"]
}
```

## Response JSON (generated AAR)

```json
{
  "executive_summary": "string",
  "incident_overview": "string",
  "timeline_of_events": "string",
  "impact_assessment": "string",
  "evidence_and_log_observations": "string",
  "five_whys": [
    { "why_number": 1, "question": "string", "answer": "string" }
  ],
  "technical_root_cause": "string",
  "remediation_completed": "string",
  "recommendations": ["string"],
  "open_questions": ["string"],
  "lessons_learned": ["string"]
}
```

## Data Needed for Root-Cause Analysis & 5 Whys

- Incident summary (what happened)
- Timeline of events (sequence leading up to and through response)
- Log snippets (technical evidence of what triggered it)
- Known impact (scope of what was affected)
- Remediation steps taken (helps confirm the root cause was correctly identified)
