# Areas To Improve

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike

## Purpose

This page tracks the main areas that need improvement for Week 6. Week 6 focuses on validation, error handling, fallback behavior, sample incident testing, and making the prototype easier to use before final demo preparation. It shows what needs to be done, why it matters, who owns the work, current status, and what evidence should be collected for the Week 6 weekly journal and final report.

## Week 6 Priority Summary

The most important Week 6 work is to prove the prototype is reliable. The team should focus first on items that create evidence for the weekly journal: testing notes, screenshots, backend test results, validation screenshots, and fallback behavior notes.

| Priority | Focus | Owner | Reason |
|---|---|---|---|
| 1 | Sample incident testing and testing notes | Brittany | The Week 6 journal needs real testing evidence, not only task descriptions. |
| 2 | Frontend validation screenshots | Mike | Validation proves the app guides users when required information is missing. |
| 3 | Backend error handling and fallback behavior | Garrett | Fallback behavior protects the final demo if the LLM or API connection fails. |
| 4 | Meeting and contribution evidence | Brittany | The instructor needs proof of each member's work and attendance. |
| 5 | Backup demo evidence | Team | Backup screenshots and saved reports reduce final presentation risk. |

## Improvement Chart

| Area to Improve | Why It Matters | Owner | Current Status | Next Action | Priority | Evidence Needed |
|---|---|---|---|---|---|---|
| Sample incident testing | Week 6 requires proof that the app works with realistic incident scenarios. | Brittany | In progress | Test at least three sample incidents, mark pass/fail status, and write short notes about report quality. | High | Updated `TESTING_CHECKLIST.md` plus screenshots for at least three generated reports. |
| Testing documentation | The weekly journal needs detailed testing descriptions and evidence. | Brittany | In progress | Record what passed, what needs revision, and whether technical/executive tone matched the selected audience. | High | Testing notes, screenshot list, and confirmation that no API key appears in screenshots. |
| Meeting and contribution evidence | The instructor grades individual contribution, so each member's work needs to be visible. | Brittany | In progress | Update `MEETING_LOG.md`, `MILESTONE_TODOS.md`, and `SHARED_DELIVERABLES_CHECKLIST.md` after the Week 6 meeting. | High | Week 6 meeting entry, owner assignments, and updated checklist screenshots. |
| Frontend validation | Users need clear messages when required fields are missing or too short. | Mike | Planned | Improve required-field validation, inline messages, and user-facing guidance before report generation. | High | Screenshot showing validation messages on the form. |
| Backend error handling | The app should handle API failures or weak input without confusing the user. | Garrett | Planned | Improve backend error handling, keep mock fallback available, and confirm the report service returns a usable response when the LLM is unavailable. | High | Test result or screenshot showing fallback/mock behavior without exposing the API key. |
| Technical vs executive output review | The advanced component depends on clear audience differences. | Brittany and Garrett | In progress | Compare technical and executive reports for the same or similar incident and note whether the tone is different enough. | High | Side-by-side notes or screenshots of technical and executive outputs. |
| 5 Whys and recommendations quality | The report should connect root cause and recommendations to the incident details. | Garrett | In progress | Review whether 5 Whys, root cause, and recommendations reference timeline, evidence, impact, and remediation details. | High | Generated report screenshot showing incident-specific 5 Whys and recommendations. |
| Copy/export behavior | The team needs clean evidence and backup reports for demo and submission. | Mike | Planned | Improve copy, download, print, or export behavior so generated reports are easy to save. | Medium | Screenshot or saved report file showing copy/download/print behavior. |
| Mobile and usability polish | The frontend should remain usable on smaller screens and during live demo practice. | Mike | Planned | Review layout spacing, responsive behavior, form controls, and generated report readability. | Medium | Screenshot of the app on a smaller browser width. |
| Final demo risk reduction | The team needs backup evidence if the live API or demo environment fails. | Team | Planned | Prepare backup screenshots, a backup generated report, and notes explaining fallback behavior. | Medium | Backup screenshots, saved generated report file, and fallback explanation notes. |

## Week 6 Focus

| Team Member | Focus This Week | Expected Output |
|---|---|---|
| Brittany | Test at least three sample incidents, update Week 6 documentation, collect screenshots, track pass/fail notes, and prepare journal evidence. | Week 6 testing notes, updated checklists, meeting log evidence, and screenshots with no API key visible. |
| Garrett | Improve backend error handling, fallback behavior, report revision support, 5 Whys quality, recommendation quality, and backend testing. | Stronger report-generation logic, fallback evidence, revision notes, and passing backend tests. |
| Mike | Improve required-field validation, copy/export behavior, mobile usability, and frontend screenshot support. | Cleaner form validation, easier report saving, improved layout, and frontend evidence screenshots. |
| Team | Review test results, assign fixes, push completed achievements to GitHub, and confirm evidence is ready before Week 6 journal submission. | Bug list, improvement notes, GitHub updates, and clear owner assignments for remaining work. |

## Screenshot Targets

Use these screenshots for the Week 6 journal and final report evidence:

- Completed form using a sample incident.
- Generated technical report output.
- Generated executive report output.
- Required-field validation message.
- Mock fallback or error-handling behavior.
- Copy, download, print, or saved report behavior.
- Smaller-screen layout if mobile usability is improved.
- Meeting log or checklist update showing Week 6 progress.

## Done Criteria

An improvement can be marked complete when:

- The related code or documentation is updated.
- The owner has tested or reviewed the change.
- A screenshot, test result, meeting note, or GitHub commit shows evidence.
- The task is reflected in the weekly journal or final report if required.
