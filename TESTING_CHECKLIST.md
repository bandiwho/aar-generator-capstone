# Testing Checklist

This checklist tracks testing for the Security Incident AAR Generator prototype. It helps confirm that the app can generate useful after-action report drafts from realistic incident details.

## Test Environment

- Prototype folder: `updated_prototype`
- Backend: FastAPI
- Frontend: browser form
- Test data: `SAMPLE_INCIDENTS.md`
- Report styles tested: technical and executive
- LLM modes: real LLM mode and mock fallback mode

## Sample Incident Testing

| # | Sample Incident | Audience | Expected Result | Status | Notes |
|---|---|---|---|---|---|
| 1 | Phishing Email Led to Microsoft 365 Account Compromise | Technical | Report includes timeline, evidence, 5 Whys, root cause, remediation, lessons learned, and open questions. | Passed | Formatting cleanup was reviewed; output was usable after broken-character and export fixes. |
| 2 | Ransomware Detected on Shared File Server | Executive | Report explains business impact, response actions, recovery plan, and lessons learned in non-technical language. | Passed | Markdown, HTML, and PDF exports were reviewed and considered clean enough for demo and journal evidence. |
| 3 | Public Cloud Storage Bucket Exposed Customer Files | Executive | Report explains exposure risk, impact, containment, policy issue, and follow-up questions. | Passed with minor formatting note | Content quality was strong and Open Questions evidence was paired correctly. Some generated versions still used `Why 1` labels in the 5 Whys section. |
| 4 | Malware Alert on Finance Workstation | Technical | Report includes endpoint evidence, suspicious command activity, containment, root cause, and next steps. | Passed with minor formatting note | Content quality was strong and Open Questions evidence was paired correctly. Some generated versions still used `Why 1` labels in the 5 Whys section. |
| 5 | SQL Injection Attempt Against Customer Portal | Technical | Report includes WAF alerts, affected endpoints, database review, root cause, remediation, and recommendations. | Passed | Report included clean formatting, clear evidence, useful open questions, and practical recommendations. |

## Pass Criteria

A generated report passes testing if it:

- Uses the provided incident details accurately.
- Includes the required AAR sections.
- Matches the selected audience.
- Does not invent major facts.
- Gives specific remediation and improvement recommendations.
- Is clear enough to use as a professional report draft.

## Needs Revision Criteria

A generated report needs revision if it:

- Leaves out major incident details.
- Misses the timeline, evidence, root cause, remediation, or lessons learned.
- Uses the wrong audience tone.
- Claims facts that were not provided.
- Gives vague recommendations.
- Is too short or poorly organized.

## Evidence To Capture

- Screenshot of the completed prototype form.
- Screenshot of the generated report output.
- Screenshot or note showing whether real LLM mode or mock fallback mode was used.
- Notes about any issue found during testing.

## Demo Selection

Use all five sample incidents for testing. For the final demo, choose the three strongest generated reports so the presentation stays focused and easy to explain.
