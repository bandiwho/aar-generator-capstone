# Demo Workflow Instructions

Project: Security Incident AAR Generator
Prepared by: Brittany
Date: June 16, 2026

## Demo Goal

Show that the prototype can take security incident details and generate a structured after-action report draft.

## Before the Demo

- Open the `updated_prototype` folder in VS Code.
- Confirm the Python environment is ready.
- Confirm the app runs at `http://localhost:7860`.
- Keep one sample incident ready from `data/sample_incidents.json`.
- Have backup screenshots ready in case the live demo has a problem.

## Start the App

In the VS Code terminal, run:

```powershell
.\.venv\Scripts\Activate.ps1
.\run_windows.ps1
```

Open this URL in a browser:

```text
http://localhost:7860
```

## Demo Steps

1. Show the Security Incident AAR Generator homepage.
2. Explain that the tool helps create an after-action report after a cybersecurity incident.
3. Point out the main form fields:
   - incident title
   - incident date
   - audience style
   - incident summary
   - timeline
   - log snippets
   - remediation steps
   - known impact
   - open questions
4. Use the default sample incident or paste one from `data/sample_incidents.json`.
5. Choose the report audience:
   - technical for IT/security detail
   - executive for business-level summary
6. Click `Generate Report Draft`.
7. Review the generated report output.
8. Point out the report sections:
   - executive summary
   - timeline
   - impact assessment
   - evidence and log observations
   - 5 Whys root-cause analysis
   - remediation completed
   - recommendations
   - lessons learned
9. Explain that the current version can run in mock mode without an API key.
10. Explain that the final version can connect to the OpenAI API when configured.

## What Each Team Member Can Say

### Brittany

Brittany explains the project purpose, assignment requirements, documentation, checklists, and quality review.

### Garrett

Garrett explains the backend/report-generation workflow and how incident details are turned into report sections.

### Mike

Mike explains the frontend form, user interface, and demo workflow.

## Backup Plan

If the live app does not run during the demo:

- Show screenshots of the homepage.
- Show screenshots of a generated report.
- Open the README and explain the project structure.
- Open `data/sample_incidents.json` and show the sample incident data.
- Explain what the live workflow is supposed to do.

## Notes for Weekly Journal

Brittany wrote simple user instructions for the demo workflow. The instructions explain how to start the app, open the browser page, enter or use sample incident data, generate a report draft, and explain the team member roles during the demo.
