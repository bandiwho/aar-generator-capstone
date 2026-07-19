# User Guide

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Team: Brittany, Garrett, Mike  
Course: CSC 482 Capstone Project II

## Purpose

This guide explains how to use the Security Incident AAR Generator prototype. The tool helps a user turn security incident details into a structured after-action report draft.

The report is a draft. A human reviewer should still confirm the facts, remove unsupported assumptions, and approve the final report before it is shared.

## What The Tool Does

The AAR Generator accepts incident details from a browser form and creates a structured after-action report. The report can include:

- Report summary
- Incident overview
- Detection and escalation notes
- Timeline of events
- Impact assessment
- Evidence and log observations
- 5 Whys root-cause analysis
- Technical root cause
- Process and communication gaps
- Remediation completed
- Recommendations and owners
- Lessons learned
- Open questions

## Before You Start

You need:

- The `updated_prototype` project folder.
- Python installed.
- The project dependencies installed in the virtual environment.
- A browser such as Chrome, Edge, or Firefox.
- One realistic incident scenario or one sample incident from `SAMPLE_INCIDENTS.md`.

The app can run in mock mode without an API key. If the OpenAI API is configured, the app can use the LLM-supported report-generation workflow.

## Start The App On Windows

Easiest option: double-click `Start_Demo.cmd` in the `updated_prototype` folder. It opens the server in a PowerShell window and then opens the app in the browser.

Manual option: open the `updated_prototype` folder in VS Code. In the VS Code terminal, run:

```powershell
.\.venv\Scripts\Activate.ps1
.\run_windows.ps1
```

Then open:

```text
http://localhost:7860
```

## Start The App On Ubuntu

Open the `updated_prototype` folder in the terminal. Run:

```bash
source .venv/bin/activate
./run_ubuntu.sh
```

Then open:

```text
http://localhost:7860
```

## Use The Form

Complete the required fields first:

| Field | What To Enter |
|---|---|
| Incident title | A short name for the incident, such as `Phishing Email Led to Microsoft 365 Account Compromise`. |
| Incident date | The date the incident occurred or was detected. |
| Audience style | Choose `Technical` or `Executive`. |
| Incident summary | A plain-language summary of what happened. |
| Timeline | Key events in order, with times if available. |
| Remediation steps | What the team did to contain, fix, or follow up on the incident. |

Optional fields improve the report quality:

| Field | What To Enter |
|---|---|
| Incident type | The category, such as phishing, ransomware, account compromise, malware, cloud exposure, or SQL injection. |
| Detection source | How the incident was found, such as SIEM alert, Defender alert, user report, help desk ticket, or audit log review. |
| Affected assets | Users, accounts, devices, servers, applications, mailboxes, cloud resources, or data affected. |
| Log snippets | Short logs, alert text, audit entries, or command output that support the incident facts. |
| Known impact | Confirmed or possible impact, such as account access, downtime, data exposure, or business disruption. |
| Lessons learned | Notes about what worked, what failed, and what should improve. |
| Open questions | Unresolved facts that still need review before the final report is approved. |

## Use A Sample Incident

For testing or demo practice, click `Load Sample Incident`. The app fills the form with a realistic sample incident.

Recommended final demo scenario:

```text
Phishing Email Led to Microsoft 365 Account Compromise
```

This incident is strong for the final demo because it is easy to explain and includes timeline events, logs, impact notes, remediation steps, and open questions.

## Choose The Report Audience

Use `Technical` when the report is for IT, security analysts, or technical reviewers. This style should keep evidence, logs, root cause, and remediation detail visible.

Use `Executive` when the report is for leadership or non-technical reviewers. This style should focus on business impact, risk, decisions, accountability, and high-level corrective actions.

For screenshots, test both styles when possible so the team can show the advanced component.

## Generate The Report

After the form is complete:

1. Click `Generate Report Draft`.
2. Wait for the report preview to appear.
3. Review the report sections.
4. Check that the report matches the selected audience.
5. Check that the 5 Whys and recommendations are specific to the incident.
6. Record any unclear wording, missing evidence, or formatting issue in the testing notes.

## Review The Report

Before using the report as evidence, check:

- The report uses the incident details accurately.
- The timeline is clear.
- The evidence section uses the provided logs or notes.
- The 5 Whys section connects to the incident facts.
- The recommendations are specific and actionable.
- The report does not claim facts that were not provided.
- Open questions stay listed instead of being treated as confirmed facts.
- Formatting is clean enough for screenshots, copied text, or downloaded files.

## Copy Or Save The Report

The generated report page includes export options:

- `Copy`: Copies the report text for pasting into notes, a journal, or a report draft.
- `Editable Text`: Downloads a Markdown text copy of the report.
- `HTML`: Downloads a browser-readable report file.
- `Save as PDF`: Opens the print dialog so the user can choose Save as PDF.

For final evidence, review the saved or copied output before submitting it. A file can technically download but still need formatting cleanup.

## Screenshot Checklist

Capture screenshots that do not show API keys, secrets, private environment files, or terminal credentials.

Useful screenshots:

- Homepage or opening form.
- Completed form with a sample incident.
- Technical report output.
- Executive report output.
- 5 Whys root-cause analysis.
- Recommendations and owners.
- Copy or download controls.
- Validation message for missing required fields.
- Backup generated report for final presentation.

## Troubleshooting

| Problem | What To Check |
|---|---|
| The page does not open | Confirm the app is running and use `http://localhost:7860`. |
| The terminal shows a missing package error | Confirm the virtual environment is activated and dependencies are installed. |
| The report does not generate | Check that all required fields are filled in. |
| The report is too vague | Add more timeline detail, logs, impact notes, and remediation steps. |
| The report includes assumptions | Move unsupported claims to Open Questions and add more evidence before final use. |
| The API is unavailable | Use mock mode or saved backup screenshots for the demo. |
| Exported output looks messy | Use the browser preview or Save as PDF for cleaner evidence, and note the formatting issue in lessons learned. |

## Final Demo Tips

- Use one strong sample incident instead of switching between too many examples.
- Practice the full workflow before presentation day.
- Keep a backup generated report ready.
- Keep screenshots ready in case the live app has a problem.
- Have Brittany explain the project purpose and documentation.
- Have Garrett explain the backend, prompt workflow, API option, fallback behavior, and 5 Whys.
- Have Mike explain the frontend form, report display, and live demo workflow.

## User Reminder

This tool creates a draft after-action report. It helps organize information, but the final report still needs human review, evidence confirmation, and team approval.
