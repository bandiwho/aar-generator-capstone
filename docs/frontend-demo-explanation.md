# Frontend and Demo Workflow Explanation

Project: Security Incident AAR Generator  
Team: Brittany, Garrett, Mike  
Presenter focus: Mike  
Final presentation window: July 27-28, 2026

## Frontend Purpose

The frontend is the user's main workflow for turning incident notes into a structured after-action report draft. It is designed to make the report-generation process clear enough for a live demo and practical enough for a security or IT team to understand.

The interface supports four main actions:

1. Enter incident details in a guided intake form.
2. Choose a Technical or Executive audience style.
3. Generate a structured after-action report draft.
4. Review, copy, download, or save the report for handoff.

## What To Point Out During The Demo

### 1. Incident Intake Form

The left side of the screen is the incident intake form. It is divided into three numbered sections so the user can follow a logical post-incident review process.

- Incident Overview captures the title, incident type, date, audience, and summary.
- Evidence and Impact captures detection source, affected assets, timeline, logs, and known impact.
- Response and Follow-Up captures remediation steps, lessons learned, and open questions.

Required fields are labeled so the user knows which details must be completed before report generation. The form also shows validation messages if required information is missing or too short.

### 2. Sample Incident Loader

The Load Sample Incident button supports testing and presentation practice. It fills the form with one realistic cybersecurity incident from `data/sample_incidents.json`.

For the final demo, the best default scenario is:

- Phishing Email Led to Microsoft 365 Account Compromise
- Audience: Technical

This scenario works well because it includes a clear timeline, log evidence, remediation steps, impact notes, and open questions.

### 3. Audience Style Selection

The audience style controls show one of the most important features of the prototype.

- Technical reports focus on evidence, logs, root cause, remediation tasks, and follow-up work.
- Executive reports focus on business impact, response status, risk, decisions, and recommendations.

This helps show that the tool is not only generating text. It is adapting the report draft to the reader.

### 4. Report Draft Preview

The right side of the screen is the generated report preview. Before generation, it shows the expected report sections. After generation, it shows the structured report with status information and review controls.

Important controls to mention:

- Section jump buttons help the presenter move directly to Summary, Timeline, Impact, 5 Whys, Root Cause, and Recommendations.
- Copy exports the report text to the clipboard.
- Editable Text downloads a Markdown file that can be revised.
- HTML downloads a clean browser-viewable report.
- Save as PDF opens the print dialog for PDF export.
- New Incident returns to a blank intake workflow.

### 5. Presentation Value

The frontend shows the full user journey in one screen: incident input on the left and report output on the right. That makes the demo easy to follow because the audience can see how the original incident details become a structured report.

## Mike's Suggested Speaking Notes

Use this section as a direct speaking guide during the frontend portion.

> This is the main user interface for our AAR Generator. The goal of the frontend is to guide the user through the information needed for a useful after-action report.
>
> The form is divided into incident overview, evidence and impact, and response follow-up. These sections match the type of information a security team normally collects after an incident.
>
> For the demo, I am using a sample phishing incident. The sample loader lets us test the same workflow consistently and keeps the live demonstration focused.
>
> The user can choose a technical or executive audience. Technical output is more detailed and evidence-focused, while executive output is more focused on business impact and decisions.
>
> Once I generate the report, the preview appears on the right. The section buttons help us quickly review the summary, timeline, impact, 5 Whys root-cause analysis, and recommendations.
>
> The export controls are important because the generated report is still a draft. A team can copy it, download editable text, save an HTML version, or save it as a PDF for review and handoff.

## Live Demo Run-Of-Show

Target time for Mike's portion: 3-4 minutes.

1. Open `http://localhost:7860`.
2. Point out the project title and one-screen layout.
3. Click Load Sample Incident.
4. Confirm the phishing incident title loaded.
5. Point out the three form sections and required-field guidance.
6. Keep Technical selected for the first demo path.
7. Click Generate Report Draft.
8. While generation runs, explain that the backend is organizing the incident facts into a structured AAR request.
9. Review the generated report title, audience label, and success message.
10. Use the section buttons to jump to Timeline, 5 Whys, and Recommendations.
11. Point out the export buttons: Copy, Editable Text, HTML, and Save as PDF.
12. Click New Incident only if there is time or if the team wants to show repeatability.

## Backup Demo Path

If the live app or API is unavailable:

1. Explain that the app supports mock fallback behavior for testing.
2. Use saved screenshots of the intake form and generated report.
3. Open `data/sample_incidents.json` or `SAMPLE_INCIDENTS.md` to show the source incident data.
4. Open `USER_GUIDE.md` to show the documented workflow.
5. Explain the same input-to-report process without rerunning generation live.

## Slide-Friendly Summary

Frontend improvements prepared for final presentation:

- Guided incident intake form with required-field validation.
- Technical and executive audience selection.
- Sample incident loader for repeatable demo testing.
- Cleaner report preview with section navigation.
- Copy, Markdown, HTML, and PDF export options.
- Responsive layout for smaller screens.
- New Incident workflow for repeated report generation.

## Final Demo Checklist

- Start the app before the presentation.
- Confirm `http://localhost:7860` loads.
- Confirm the homepage background image renders.
- Click Load Sample Incident and verify fields populate.
- Generate one Technical phishing report.
- Confirm section jump buttons work.
- Confirm Copy, Editable Text, HTML, and Save as PDF controls are visible.
- Keep backup screenshots ready.
- Do not show `.env`, API keys, or private terminal output.
