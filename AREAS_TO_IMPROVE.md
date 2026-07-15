# Areas To Improve

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike  
Current focus: Week 7, July 13-19, 2026

## Purpose

This page tracks the detailed areas that still need improvement for Week 7. Week 7 is focused on final presentation preparation, demo practice, screenshots, journal evidence, backup materials, and final project polish. The goal is not to add large new features. The goal is to make the existing prototype, documentation, slides, and demo evidence clean enough for final review.

Each section below uses small checklist tasks so the team can clearly mark what is done, what is still in progress, and what needs to be discussed during the Week 7 meeting.

Status key:

- `[ ]` Not started
- `[~]` In progress
- `[x]` Done

## Week 7 Priority Summary

| Priority | Focus | Owner | Current Status | Why It Matters |
|---|---|---|---|---|
| 1 | Final demo screenshots | Brittany and Mike | Not started | Screenshots are needed for the Week 7 journal, final report, and presentation backup. |
| 2 | Speaking roles and demo script | Team | In progress | Each team member needs to know exactly what to explain during the final presentation. |
| 3 | Backup generated report | Garrett and Brittany | Not started | The team needs a saved report in case the live demo has a problem. |
| 4 | Frontend visual polish | Mike | Planned | The homepage, form, report display, and export controls need to look clean during screenshots and demo. |
| 5 | Backend explanation and final demo data | Garrett | Planned | Garrett needs clear talking points and confirmation that the selected demo incident works. |
| 6 | Week 7 journal evidence | Brittany | In progress | The journal needs milestones, testing evidence, blockers, lessons learned, and contributions. |
| 7 | GitHub readiness | Team | Not started | Final source files should be organized, with no API keys, secrets, or local-only drafts uploaded. |

## 1. Final Demo Screenshots

Owner: Brittany and Mike  
Priority: High  
Current status: Not started

Why this needs improvement: The Week 7 journal, final report, and presentation all need clear visual evidence. The team should not wait until the final presentation week to collect screenshots.

### Small Tasks

- [ ] Decide which browser window size will be used for final screenshots.
- [ ] Open the prototype homepage and confirm the page loads cleanly.
- [ ] Capture a homepage screenshot.
- [ ] Open the report form page.
- [ ] Load or enter the final demo incident.
- [ ] Capture a completed form screenshot.
- [ ] Select the technical audience option.
- [ ] Generate a technical report.
- [ ] Capture the technical report title and summary section.
- [ ] Capture the technical report 5 Whys section.
- [ ] Capture the technical report recommendations section.
- [ ] Select the executive audience option.
- [ ] Generate an executive report.
- [ ] Capture the executive report title and summary section.
- [ ] Capture the audience selection controls.
- [ ] Capture the Copy Report control.
- [ ] Capture the Editable Text download control.
- [ ] Capture the HTML download control.
- [ ] Capture the Save as PDF control.
- [ ] Capture one screenshot showing required-field validation.
- [ ] Capture one screenshot showing the smaller-screen/mobile-friendly layout if it looks clean.
- [ ] Review every screenshot for exposed API keys.
- [ ] Review every screenshot for exposed `.env` content.
- [ ] Review every screenshot for terminal secrets or private configuration.
- [ ] Rename screenshots with clear names.
- [ ] Save screenshots in a final evidence folder.
- [ ] Choose which screenshots belong in the Week 7 journal.
- [ ] Choose which screenshots belong in the final presentation.
- [ ] Choose which screenshots belong in the final report.

### Evidence Needed

- Screenshot of homepage.
- Screenshot of completed form.
- Screenshot of generated technical report.
- Screenshot of generated executive report.
- Screenshot of 5 Whys section.
- Screenshot of recommendations section.
- Screenshot of export controls.
- Screenshot proving no private key or secret is visible.

## 2. Final Demo Incident

Owner: Team  
Priority: High  
Current status: Not started

Why this needs improvement: The team needs one final demo incident that is reliable, realistic, and easy to explain. The phishing/Microsoft 365 account compromise sample is currently the likely demo scenario, but it should be confirmed.

### Small Tasks

- [ ] Review the available sample incidents.
- [ ] Confirm whether the phishing/Microsoft 365 account compromise sample will be the main demo.
- [ ] Make sure the selected incident has a clear title.
- [ ] Make sure the selected incident has a realistic date.
- [ ] Make sure the selected incident has a clear incident summary.
- [ ] Make sure the selected incident has a useful timeline.
- [ ] Make sure the selected incident has enough log snippets or evidence notes.
- [ ] Make sure the selected incident has clear impact details.
- [ ] Make sure the selected incident has remediation steps.
- [ ] Make sure the selected incident has open questions if evidence is incomplete.
- [ ] Generate a report from the selected incident.
- [ ] Confirm the generated report includes a summary.
- [ ] Confirm the generated report includes a timeline.
- [ ] Confirm the generated report includes evidence observations.
- [ ] Confirm the generated report includes 5 Whys.
- [ ] Confirm the generated report includes root cause.
- [ ] Confirm the generated report includes recommendations.
- [ ] Confirm the generated report includes lessons learned or follow-up actions.
- [ ] Save the final demo incident text for quick copying if autofill does not work.
- [ ] Add a short note explaining why this incident is a good demo choice.

### Evidence Needed

- Final demo incident name.
- Generated report from final demo incident.
- Short note explaining why the incident was selected.

## 3. Backup Generated Report

Owner: Garrett and Brittany  
Priority: High  
Current status: Not started

Why this needs improvement: A live demo can fail because of API delays, internet problems, local server issues, or timing. The team needs a backup report that can be shown if the live demo does not work.

### Small Tasks

- [ ] Generate one strong report using the final demo incident.
- [ ] Confirm the report uses the correct audience style.
- [ ] Confirm the report title is clean.
- [ ] Confirm the report summary is easy to explain.
- [ ] Confirm the timeline is readable.
- [ ] Confirm the 5 Whys section is readable.
- [ ] Confirm the recommendations are specific to the incident.
- [ ] Confirm the report does not include placeholder text.
- [ ] Confirm the report does not include raw Markdown symbols that look unprofessional.
- [ ] Confirm the report does not include labels that were previously removed, such as `Gap:`, `Task:`, `Open item:`, or `Evidence note:`.
- [ ] Save the report as a backup file.
- [ ] Save a screenshot of the backup report.
- [ ] Save a screenshot of the 5 Whys section.
- [ ] Save a screenshot of the recommendations section.
- [ ] Decide whether the backup should be shown as a screenshot, browser view, HTML file, or PDF.
- [ ] Add the backup report location to the meeting notes.

### Evidence Needed

- Saved backup generated report.
- Backup report screenshot.
- Note showing where the backup report is stored.

## 4. Presentation Slides

Owner: Brittany  
Priority: High  
Current status: In progress

Why this needs improvement: The slides need to clearly show the project problem, solution, prototype workflow, testing evidence, team roles, lessons learned, and remaining work. The slides should not be overloaded, and screenshots should be easy to read.

### Small Tasks

- [x] Create or update the Week 7 presentation draft.
- [ ] Review the title slide for project name and team name.
- [ ] Confirm the problem statement slide is clear.
- [ ] Confirm the solution slide explains the AAR Generator in plain language.
- [ ] Confirm the prototype workflow slide matches the actual app.
- [ ] Confirm the technology stack slide is accurate.
- [ ] Confirm the testing evidence slide matches actual testing.
- [ ] Add final homepage screenshot.
- [ ] Add final completed form screenshot.
- [ ] Add final generated report screenshot.
- [ ] Add final 5 Whys screenshot.
- [ ] Add final recommendations screenshot.
- [ ] Add final export-controls screenshot if space allows.
- [ ] Confirm Brittany's speaking section is clear.
- [ ] Confirm Garrett's speaking section is clear.
- [ ] Confirm Mike's speaking section is clear.
- [ ] Add or update lessons learned.
- [ ] Add backup demo note.
- [ ] Check every slide for spelling and grammar.
- [ ] Check every slide for text that is too small.
- [ ] Check every slide for crowded content.
- [ ] Check every slide for screenshots that are blurry.
- [ ] Confirm no slide shows an API key or private configuration.
- [ ] Save the final deck in the required format.

### Evidence Needed

- Updated PowerPoint deck.
- Final screenshot list.
- Speaking-role notes.
- Slide review notes.

## 5. Week 7 Journal

Owner: Brittany  
Priority: High  
Current status: In progress

Why this needs improvement: The Week 7 journal needs clear evidence of progress, testing, blockers, lessons learned, contribution, and meeting attendance. The journal should be a Word/PDF file for submission, not a GitHub Markdown draft.

### Small Tasks

- [x] Start the Week 7 journal draft.
- [x] Add a signature page.
- [x] Keep the Week 7 journal as a local-only DOCX draft.
- [ ] Confirm the Week 7 journal does not need to be uploaded to GitHub.
- [ ] Add milestones achieved this week.
- [ ] Add brief descriptions for each milestone.
- [ ] Add subtasks completed by Brittany.
- [ ] Add subtasks completed by Garrett.
- [ ] Add subtasks completed by Mike.
- [ ] Add detailed testing descriptions.
- [ ] Add final screenshot evidence.
- [ ] Add lessons learned.
- [ ] Add team contribution section.
- [ ] Add progress compared to plan.
- [ ] Add plan adjustments if needed.
- [ ] Add Week 7 blockers.
- [ ] Add meeting attendance and meeting discussion summary.
- [ ] Confirm the signature page has Brittany, Garrett, and Mike.
- [ ] Confirm each signature line keeps `Date:` on the same line as `Signature:`.
- [ ] Review grammar and sentence clarity.
- [ ] Export the journal as a PDF.
- [ ] Confirm the PDF opens correctly.
- [ ] Submit the PDF before Friday if possible.
- [ ] If Friday is not possible, submit by the Sunday deadline.

### Evidence Needed

- Week 7 journal DOCX draft.
- Week 7 journal PDF.
- Signature page.
- Meeting log summary.
- Screenshot evidence.

## 6. Meeting Log And Meeting Discussion

Owner: Brittany  
Priority: High  
Current status: In progress

Why this needs improvement: Meeting notes prove attendance, planning, assigned work, and blockers. The Week 7 entry still needs final details after the meeting.

### Small Tasks

- [x] Add Week 7 meeting entry.
- [x] Add planned Week 7 meeting topics.
- [x] Add planned Week 7 owner assignments.
- [ ] Record exact Week 7 attendance.
- [ ] Record if anyone was absent.
- [ ] Record the meeting start time.
- [ ] Record the meeting end time.
- [ ] Record final demo incident decision.
- [ ] Record screenshot owner.
- [ ] Record backup report owner.
- [ ] Record speaking roles.
- [x] Record that the homepage now uses a full-page background image.
- [ ] Record GitHub push/sync plan.
- [ ] Record any final blockers.
- [ ] Add Microsoft Teams chat notes if useful.
- [ ] Make sure Week 7 meeting notes are summarized in the journal.

### Evidence Needed

- Updated Week 7 meeting log.
- Attendance record.
- Owner assignments.
- Blocker notes.

## 7. Backend Polish

Owner: Garrett  
Priority: Medium  
Current status: Planned

Why this needs improvement: The backend is working, but Garrett still needs a clean explanation for the final demo. The team should avoid risky backend changes unless they are needed for demo reliability.

### Small Tasks

- [ ] Confirm the backend starts successfully.
- [ ] Confirm the report-generation route works.
- [ ] Confirm the final demo incident works through the backend.
- [ ] Confirm fallback/mock behavior still works.
- [ ] Confirm no API key is printed in screenshots or documentation.
- [ ] Confirm backend tests pass before final demo practice.
- [ ] Review backend comments for anything confusing or outdated.
- [ ] Remove or update comments that no longer match the code.
- [ ] Confirm 5 Whys output is incident-specific.
- [ ] Confirm recommendations are incident-specific.
- [ ] Confirm technical audience output has technical detail.
- [ ] Confirm executive audience output is easier for leadership to read.
- [ ] Prepare a short backend explanation for Garrett.
- [ ] Prepare one sentence explaining mock fallback.
- [ ] Prepare one sentence explaining OpenAI/API mode.
- [ ] Prepare one sentence explaining why 5 Whys helps the report.

### Evidence Needed

- Backend test result.
- Final demo report output.
- Garrett's backend talking points.

## 8. Frontend Polish

Owner: Mike  
Priority: Medium  
Current status: Planned

Why this needs improvement: The frontend is the part the audience will see most during the demo. It needs to look clean, guide the user, and make report output easy to read.

### Small Tasks

- [ ] Confirm the homepage loads.
- [ ] Confirm the report form loads.
- [ ] Confirm sample incident autofill works if available.
- [ ] Confirm the user can enter incident title.
- [ ] Confirm the user can enter incident date.
- [ ] Confirm the user can enter incident summary.
- [ ] Confirm the user can enter timeline details.
- [ ] Confirm the user can enter log snippets.
- [ ] Confirm the user can enter impact details.
- [ ] Confirm the user can enter remediation steps.
- [ ] Confirm the user can enter open questions.
- [ ] Confirm required-field validation appears when needed.
- [ ] Confirm validation messages are easy to understand.
- [ ] Confirm loading state appears while a report is being generated.
- [ ] Confirm technical audience button or control works.
- [ ] Confirm executive audience button or control works.
- [ ] Confirm generated report is readable.
- [ ] Confirm 5 Whys section is readable.
- [ ] Confirm recommendations section is readable.
- [ ] Confirm Copy Report works.
- [ ] Confirm Editable Text download works.
- [ ] Confirm HTML download works.
- [ ] Confirm Save as PDF option is available.
- [ ] Confirm smaller-screen layout is usable.
- [ ] Confirm no visible text overlaps.
- [ ] Confirm buttons and labels fit their containers.
- [x] Confirm the homepage background image task is complete.

### Evidence Needed

- Frontend screenshots.
- Demo flow notes.
- Decision about homepage background image.

## 9. GitHub And File Organization

Owner: Team  
Priority: High  
Current status: Not started

Why this needs improvement: The project should be clean before final review. GitHub should include source code and project documentation, but local-only Word drafts should not be uploaded.

### Small Tasks

- [ ] Check Git status before pushing.
- [ ] Confirm `README.md` changes are intentional.
- [ ] Confirm `MILESTONE_TODOS.md` changes are intentional.
- [ ] Confirm `SHARED_DELIVERABLES_CHECKLIST.md` changes are intentional.
- [ ] Confirm `MEETING_LOG.md` changes are intentional.
- [ ] Confirm `AREAS_TO_IMPROVE.md` changes are intentional.
- [ ] Confirm `USER_GUIDE.md` should be added to GitHub.
- [ ] Confirm the PowerPoint deck should be added to GitHub or kept local.
- [ ] Confirm Week 7 DOCX journal draft stays local-only.
- [ ] Confirm Week 7 DOCX meeting agenda stays local-only.
- [ ] Confirm no Week 7 Markdown journal draft is in the GitHub project.
- [ ] Confirm no Week 7 Markdown agenda draft is in the GitHub project.
- [ ] Confirm no API keys are in tracked files.
- [ ] Confirm no `.env` file is tracked.
- [ ] Confirm no test cache or temporary render folder is tracked.
- [ ] Push only the files the team wants on GitHub.
- [ ] Re-check GitHub after push to make sure the files appear correctly.

### Evidence Needed

- Git status check.
- GitHub repository review.
- Note confirming local-only DOCX drafts were not uploaded.

## 10. Demo Practice

Owner: Team  
Priority: High  
Current status: Not started

Why this needs improvement: The team needs to practice the demo before the final presentation window. Each person should know their part and what to do if the live demo fails.

### Small Tasks

- [ ] Decide the speaking order.
- [ ] Decide who starts the live demo.
- [ ] Decide who explains the form fields.
- [ ] Decide who explains the backend.
- [ ] Decide who explains the generated report.
- [ ] Decide who explains 5 Whys.
- [ ] Decide who explains technical vs executive output.
- [ ] Decide who explains export options.
- [ ] Decide who explains testing evidence.
- [ ] Decide who explains lessons learned.
- [ ] Practice opening the app.
- [ ] Practice loading or entering the final demo incident.
- [ ] Practice generating the report.
- [ ] Practice switching between technical and executive audience if needed.
- [ ] Practice showing the 5 Whys section.
- [ ] Practice showing recommendations.
- [ ] Practice using backup screenshots.
- [ ] Practice using backup generated report.
- [ ] Time the full demo.
- [ ] Record what went smoothly.
- [ ] Record what was confusing.
- [ ] Record what needs one more fix before the final presentation.

### Evidence Needed

- Demo practice notes.
- Speaking-role list.
- Backup plan.
- Final demo timing.

## 11. Final Report Preparation

Owner: Brittany  
Priority: Medium  
Current status: Planned

Why this needs improvement: Week 7 should prepare the team for Week 8 final report work. Waiting until Week 8 to organize evidence will make the final report harder.

### Small Tasks

- [ ] Create a list of final report sections.
- [ ] Collect project description wording.
- [ ] Collect problem statement wording.
- [ ] Collect solution summary wording.
- [ ] Collect technology stack details.
- [ ] Collect setup and usage evidence.
- [ ] Collect testing summary notes.
- [ ] Collect screenshot evidence.
- [ ] Collect known limitations.
- [ ] Collect future improvements.
- [ ] Collect Brittany's contribution notes.
- [ ] Collect Garrett's contribution notes.
- [ ] Collect Mike's contribution notes.
- [ ] Collect meeting log evidence.
- [ ] Collect GitHub evidence.
- [ ] Identify missing final report content before Week 8 starts.

### Evidence Needed

- Final report outline.
- Evidence list.
- Missing-content list for Week 8.

## 12. Current Blockers

| Blocker | Owner | Impact | Small Next Step |
|---|---|---|---|
| Final screenshots are not organized yet. | Brittany and Mike | Week 7 journal and presentation evidence are incomplete. | Capture homepage, form, generated report, 5 Whys, recommendations, and export-control screenshots. |
| Speaking roles are not fully confirmed. | Team | The final presentation may feel unorganized. | Confirm Brittany, Garrett, and Mike's speaking sections during the Week 7 meeting. |
| Final demo incident still needs final confirmation. | Team | Demo practice cannot be fully locked in. | Choose the phishing/Microsoft 365 sample or another final scenario. |
| Backup generated report is not prepared yet. | Garrett and Brittany | The team has no fallback if live generation fails. | Generate and save one strong report before practice. |
| Homepage background image task updated. | Mike | The previous wording no longer matched the current frontend design. | Confirm the full-page homepage background image renders correctly for demo screenshots. |
| Week 7 GitHub push/sync needs confirmation. | Team | Documentation changes may not be visible to teammates or instructor. | Check Git status, choose files to push, and confirm local-only DOCX drafts stay off GitHub. |
| Week 7 journal evidence is incomplete. | Brittany | Journal cannot be finalized yet. | Add screenshots, meeting summary, blockers, and contribution notes. |

## 13. Done Criteria

An improvement can be marked complete when:

- [ ] The task has a named owner.
- [ ] The task has been tested, reviewed, or discussed.
- [ ] The evidence exists as a screenshot, saved report, test result, meeting note, slide, or journal section.
- [ ] The result does not expose an API key, `.env` file, terminal secret, or private configuration.
- [ ] The status is updated in the correct tracker file.
- [ ] The task is included in the Week 7 journal if it supports the weekly assignment.
- [ ] The task is included in the final presentation or final report if it supports final submission.

## 14. Meeting Review Checklist

Use this section during the Week 7 meeting.

- [ ] Did we select the final demo incident?
- [ ] Did we assign screenshot responsibilities?
- [ ] Did we assign backup report responsibility?
- [ ] Did we confirm speaking roles?
- [x] Did we confirm the homepage background image is ready?
- [ ] Did we confirm what files should go to GitHub?
- [ ] Did we confirm what files should stay local-only?
- [ ] Did we confirm the Week 7 journal evidence list?
- [ ] Did we choose a demo practice time?
- [ ] Did we identify anything that must wait until Week 8?
