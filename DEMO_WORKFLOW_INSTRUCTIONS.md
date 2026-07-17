# Final Demo Workflow Instructions

Project: Security Incident AAR Generator  
Team: Brittany, Garrett, Mike  
Final presentation window: July 27-28, 2026

## Demo Goal

Show that the prototype can take realistic cybersecurity incident details and generate a structured after-action report draft for either a technical or executive audience.

The demo should prove three things:

1. The frontend guides the user through the right incident details.
2. The backend turns those details into a structured AAR draft.
3. The generated report can be reviewed, copied, downloaded, or saved for handoff.

## Recommended Team Flow

| Presenter | Focus | Target Time |
|---|---|---|
| Brittany | Project purpose, problem statement, documentation, and quality review | 2-3 minutes |
| Mike | Frontend walkthrough and live demo workflow | 3-4 minutes |
| Garrett | Backend/report-generation explanation, LLM workflow, mock fallback, and 5 Whys logic | 2-3 minutes |
| Brittany or Team | Testing summary, lessons learned, final status, and questions | 2-3 minutes |

## Before The Demo

- Start the app before the presentation begins.
- Confirm the app opens at `http://localhost:7860`.
- Confirm the homepage background image renders.
- Confirm the Load Sample Incident button fills the form.
- Confirm one report can be generated successfully.
- Keep backup screenshots ready for the form and generated report.
- Keep a backup generated report available in case the live demo is interrupted.
- Do not show `.env`, API keys, private terminal output, or browser tabs with unrelated information.

## Start The App

From the project folder, run:

```powershell
.\.venv\Scripts\Activate.ps1
.\run_windows.ps1
```

Open:

```text
http://localhost:7860
```

## Recommended Demo Scenario

Use the first sample incident:

- Title: Phishing Email Led to Microsoft 365 Account Compromise
- Audience: Technical
- Why this is the best demo scenario: it has a clear timeline, Microsoft 365 evidence, remediation steps, known impact, and open questions.

If the team wants to briefly mention a second audience style, use:

- Title: Ransomware Detected on Shared File Server
- Audience: Executive
- Why this works: it explains business interruption, recovery, risk, and leadership-level recommendations.

## Live Demo Steps

1. Open the Security Incident AAR Generator homepage.
2. Briefly explain that the tool creates a draft after-action report from incident details.
3. Point out the one-screen layout:
   - incident intake on the left
   - report preview on the right
4. Click Load Sample Incident.
5. Confirm the phishing sample incident appears in the form.
6. Point out the three intake sections:
   - Incident Overview
   - Evidence and Impact
   - Response and Follow-Up
7. Point out required-field validation and the required labels.
8. Point out the audience style choices:
   - Technical for security and IT detail
   - Executive for leadership and business impact
9. Keep Technical selected.
10. Click Generate Report Draft.
11. While the report generates, explain that the incident facts are sent to the backend and organized into a structured report request.
12. Review the generated report preview.
13. Use section buttons to jump to:
   - Summary
   - Timeline
   - Impact
   - 5 Whys
   - Recommendations
14. Point out that 5 Whys helps connect the incident to likely process or control gaps.
15. Point out the export options:
   - Copy
   - Editable Text
   - HTML
   - Save as PDF
16. Explain that the report is a starting draft and still requires human review.
17. Use New Incident only if there is time and the team wants to show repeatability.

## Mike Frontend Speaking Notes

This is the main user interface for our AAR Generator. The frontend is designed to guide the user through the incident details needed for a useful after-action report.

The form is split into three sections: incident overview, evidence and impact, and response follow-up. Those sections match the type of information a security team would normally collect after an incident.

For the live demo, I am loading a sample phishing incident. This gives us realistic data and lets us run the same workflow consistently during testing and presentation practice.

The audience selection is important because the report changes depending on who needs to read it. A technical report focuses more on logs, evidence, root cause, and remediation. An executive report focuses more on business impact, response status, risk, and decisions.

After generation, the report preview appears on the right. The section buttons let us quickly review the summary, timeline, impact, 5 Whys analysis, and recommendations.

The export controls make the draft usable after generation. A user can copy the report, download editable text, save an HTML version, or use the print dialog to save a PDF.

## Garrett Backend Speaking Notes

The backend receives the incident details from the form and validates them against the expected report input structure. It then builds a structured prompt that asks for a professional after-action report.

The report-generation workflow is designed to keep the output consistent. It asks for key sections such as the report summary, timeline, impact assessment, evidence observations, 5 Whys root-cause analysis, remediation, recommendations, lessons learned, and open questions.

The app can use the OpenAI API when configured. It also supports mock fallback behavior so the demo and tests can still run if the API is unavailable.

## Brittany Documentation And Testing Notes

The documentation supports the demo with a README, user guide, testing checklist, sample incidents, meeting log, and final demo explanation.

Testing used multiple incident types, including phishing, ransomware, cloud exposure, malware, and SQL injection. The team checked whether each generated report used the provided details accurately, included the required sections, matched the selected audience, and gave useful recommendations.

## Backup Plan

If the live app does not run:

1. Show the saved screenshot of the homepage/intake form.
2. Show the saved screenshot of a generated report.
3. Open `SAMPLE_INCIDENTS.md` to show the realistic incident data.
4. Open `docs/frontend-demo-explanation.md` to explain the frontend flow.
5. Explain that mock fallback behavior is available for testing if the API is unavailable.

If report generation is slow:

1. Keep speaking while generation runs.
2. Explain the frontend sections and backend workflow.
3. If it still does not complete, switch to backup screenshots.

If the wrong sample loads:

1. Click Load Sample Incident again until the phishing sample appears, or continue with the loaded sample.
2. The workflow is the same for every sample incident.

## Final Presentation Reminders

- Keep the live demo focused on one strong incident.
- Do not spend time reading every generated paragraph.
- Show the structure of the report, not every line of the report.
- Emphasize that the output is a draft for human review.
- Mention technical and executive audiences.
- Mention 5 Whys as the advanced root-cause component.
- Mention export options because they show practical handoff value.
