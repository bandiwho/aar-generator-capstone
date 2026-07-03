# Areas To Improve

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike

## Purpose

This page tracks the main areas that need improvement for Week 6. Week 6 focuses on validation, error handling, fallback behavior, sample incident testing, and making the prototype easier to use before final demo preparation. It shows what needs to be done, why it matters, who owns the work, and what evidence should be collected for the Week 6 weekly journal and final report.

## Improvement Chart

| Area to Improve | Why It Matters | Owner | Tasks to Complete | Priority | Evidence Needed |
|---|---|---|---|---|---|
| Backend error handling | The app should handle API failures or weak input without confusing the user. | Garrett | Improve backend error handling, keep mock fallback available, and confirm the report service returns a usable response when the LLM is unavailable. | High | Test result or screenshot showing fallback/mock behavior without exposing the API key. |
| Frontend validation | Users need clear messages when required fields are missing or too short. | Mike | Improve required-field validation, inline messages, and user-facing guidance before report generation. | High | Screenshot showing validation messages on the form. |
| Sample incident testing | Week 6 requires the app to work with multiple realistic test incidents. | Brittany | Test at least three sample incidents, record pass/fail notes, compare output quality, and save screenshots. | High | Testing notes and screenshots for three sample incidents. |
| Technical vs executive output review | The advanced project requirement depends on clear audience differences. | Brittany and Garrett | Compare technical and executive reports, identify weak output, and refine prompt/report guidance if the tone is too similar. | High | Side-by-side notes or screenshots of technical and executive outputs. |
| 5 Whys and recommendations quality | The report should not only include these sections; they should connect to the incident details. | Garrett | Improve root-cause and recommendation logic so outputs reference timeline, evidence, impact, and remediation details. | High | Generated report screenshot showing incident-specific 5 Whys and recommendations. |
| Copy/export behavior | The team needs clean evidence and backup reports for demo and submission. | Mike | Improve copy, download, print, or export behavior so generated reports are easy to save. | Medium | Screenshot or saved report file showing copy/download/print behavior. |
| Testing documentation | The weekly journal needs detailed testing descriptions and evidence. | Brittany | Update `TESTING_CHECKLIST.md`, write testing notes, and confirm no screenshot shows the OpenAI API key. | High | Updated checklist and screenshot evidence with no secrets visible. |
| Meeting and contribution evidence | The instructor grades individual contributions, so each member's work needs to be visible. | Brittany | Update `MEETING_LOG.md`, `MILESTONE_TODOS.md`, and `SHARED_DELIVERABLES_CHECKLIST.md` for Week 6. | High | Meeting log entry and updated checklist screenshots. |
| Mobile and usability polish | The frontend should remain usable on smaller screens and during live demo practice. | Mike | Review layout spacing, responsive behavior, form controls, and generated report readability. | Medium | Screenshot of the app on a smaller browser width. |
| Final demo risk reduction | The team needs backup evidence if the live API or demo environment fails. | Team | Prepare backup screenshots, a backup generated report, and notes explaining fallback behavior. | Medium | Backup screenshots and saved generated report file. |

## Week 6 Focus

| Team Member | Focus This Week | Expected Output |
|---|---|---|
| Brittany | Test at least three sample incidents, update Week 6 documentation, collect screenshots, and track pass/fail notes. | Week 6 testing notes, updated checklists, meeting log evidence, and screenshots with no API key visible. |
| Garrett | Improve backend error handling, fallback behavior, 5 Whys quality, recommendation quality, and backend testing. | Stronger report-generation logic, fallback evidence, and passing backend tests. |
| Mike | Improve required-field validation, copy/export behavior, mobile usability, and frontend screenshot support. | Cleaner form validation, easier report saving, improved layout, and frontend evidence screenshots. |
| Team | Review test results and assign fixes before Week 6 journal submission. | Bug list, improvement notes, and clear owner assignments for remaining work. |

## Done Criteria

An improvement can be marked complete when:

- The related code or documentation is updated.
- The owner has tested or reviewed the change.
- A screenshot, test result, meeting note, or GitHub commit shows evidence.
- The task is reflected in the weekly journal or final report if required.
