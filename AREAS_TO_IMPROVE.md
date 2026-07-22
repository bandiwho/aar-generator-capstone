# Areas To Improve

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike  
Current focus: Week 8, July 20-24, 2026

## Purpose

This page tracks the detailed areas that still need improvement for Week 8. Week 8 is focused on final presentation polish, final demo practice, submission organization, GitHub readiness, and final quality review. The goal is not to add large new features. The goal is to keep the completed prototype stable and make the final presentation, report evidence, and demo materials clear enough for final grading.

Each section below uses small checklist tasks so the team can clearly mark what is done, what is still in progress, and what needs to be completed before the final presentation window.

Status key:

- `[ ]` Not started
- `[~]` In progress
- `[x]` Done

## Week 8 Priority Summary

| Priority | Focus | Owner | Current Status | Why It Matters |
|---|---|---|---|---|
| 1 | Final presentation slides | Brittany and team | In progress | The deck is mostly complete and only needs a few remaining slides, final screenshots, speaker flow, and grammar review before practice. |
| 2 | Live demo practice | Team | Not started | The team still needs a timed run-through so the live demo and speaking order feel organized. |
| 3 | GitHub readiness | Team | In progress | Final source files and documentation should be pushed after the latest polish changes are reviewed. |
| 4 | Final report package | Brittany | Complete | The final paper draft is written, signed, and aligned with final slides and demo evidence. |
| 5 | Report export and formatting polish | Brittany and Garrett | In progress | PDF margins, owner labels, Open Questions styling, and downloaded report readability need final confirmation. |
| 6 | Backend and frontend talking points | Garrett and Mike | In progress | Each teammate needs concise talking points that match their slides and the live demo. |
| 7 | Backup demo materials | Team | Complete | Backup screenshots and generated reports are available if the live app, API, browser, or presentation machine has an issue. |

## Week 8 Final Push Checklist

- [~] Finalize the last few presentation slides, slide wording, screenshots, and visual consistency.
- [~] Confirm Brittany, Mike, and Garrett's speaking order.
- [ ] Practice the full presentation and live demo from start to finish.
- [x] Confirm the phishing/Microsoft 365 account compromise scenario is the final demo incident.
- [x] Confirm the app runs locally through `run_windows.ps1`.
- [x] Confirm `Start_Demo.cmd` opens the app without starting duplicate server windows.
- [x] Confirm latest automated tests pass.
- [x] Regenerate final technical and executive reports after the latest formatting fixes.
- [x] Re-check Save as PDF output, downloaded HTML output, and owner-label formatting.
- [ ] Push final documentation and code changes to GitHub after review.
- [x] Confirm no API key, `.env` file, terminal secret, or private configuration appears in screenshots or final materials.
- [ ] Keep backup screenshots and saved generated reports available during the presentation.

## 1. Final Demo Screenshots

Owner: Brittany and Mike  
Priority: High  
Current status: Complete

Why this needed improvement: The Week 7 journal, final report, and presentation all needed clear visual evidence. The team collected screenshots during Week 7 so final presentation week can focus on practice and submission readiness.

### Small Tasks

- [x] Decide which browser window size will be used for final screenshots.
- [x] Open the prototype homepage and confirm the page loads cleanly.
- [x] Capture a homepage screenshot.
- [x] Open the report form page.
- [x] Load or enter the final demo incident.
- [x] Capture a completed form screenshot.
- [x] Select the technical audience option.
- [x] Generate a technical report.
- [x] Capture the technical report title and summary section.
- [x] Capture the technical report 5 Whys section.
- [x] Capture the technical report recommendations section.
- [x] Select the executive audience option.
- [x] Generate an executive report.
- [x] Capture the executive report title and summary section.
- [x] Capture the audience selection controls.
- [x] Capture the Copy Report control.
- [x] Capture the Editable Text download control.
- [x] Capture the HTML download control.
- [x] Capture the Save as PDF control.
- [ ] Capture one screenshot showing required-field validation.
- [ ] Capture one screenshot showing the smaller-screen/mobile-friendly layout if it looks clean.
- [x] Review every screenshot for exposed API keys.
- [x] Review every screenshot for exposed `.env` content.
- [x] Review every screenshot for terminal secrets or private configuration.
- [x] Rename screenshots with clear names.
- [x] Save screenshots in a final evidence folder.
- [x] Choose which screenshots belong in the Week 7 journal.
- [~] Choose which screenshots belong in the final presentation.
- [x] Choose which screenshots belong in the final report.

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
Current status: Complete

Why this needed improvement: The team needed one final demo incident that is reliable, realistic, and easy to explain. The phishing/Microsoft 365 account compromise sample was selected and tested for final demo use.

### Small Tasks

- [x] Review the available sample incidents.
- [x] Confirm whether the phishing/Microsoft 365 account compromise sample will be the main demo.
- [x] Make sure the selected incident has a clear title.
- [x] Make sure the selected incident has a realistic date.
- [x] Make sure the selected incident has a clear incident summary.
- [x] Make sure the selected incident has a useful timeline.
- [x] Make sure the selected incident has enough log snippets or evidence notes.
- [x] Make sure the selected incident has clear impact details.
- [x] Make sure the selected incident has remediation steps.
- [x] Make sure the selected incident has open questions if evidence is incomplete.
- [x] Generate a report from the selected incident.
- [x] Confirm the generated report includes a summary.
- [x] Confirm the generated report includes a timeline.
- [x] Confirm the generated report includes evidence observations.
- [x] Confirm the generated report includes 5 Whys.
- [x] Confirm the generated report includes root cause.
- [x] Confirm the generated report includes recommendations.
- [x] Confirm the generated report includes lessons learned or follow-up actions.
- [x] Save the final demo incident text for quick copying if autofill does not work.
- [x] Add a short note explaining why this incident is a good demo choice.

### Evidence Needed

- Final demo incident name.
- Generated report from final demo incident.
- Short note explaining why the incident was selected.

## 3. Backup Generated Report

Owner: Garrett and Brittany  
Priority: High  
Current status: Complete

Why this needed improvement: A live demo can fail because of API delays, internet problems, local server issues, or timing. The team prepared a backup report that can be shown if the live demo does not work.

### Small Tasks

- [x] Generate one strong report using the final demo incident.
- [x] Confirm the report uses the correct audience style.
- [x] Confirm the report title is clean.
- [x] Confirm the report summary is easy to explain.
- [x] Confirm the timeline is readable.
- [x] Confirm the 5 Whys section is readable.
- [x] Confirm the recommendations are specific to the incident.
- [x] Confirm the report does not include placeholder text.
- [x] Confirm the report does not include raw Markdown symbols that look unprofessional.
- [x] Confirm the report does not include labels that were previously removed, such as `Gap:`, `Task:`, `Open item:`, or `Evidence note:`.
- [x] Save the report as a backup file.
- [x] Save a screenshot of the backup report.
- [x] Save a screenshot of the 5 Whys section.
- [x] Save a screenshot of the recommendations section.
- [x] Decide whether the backup should be shown as a screenshot, browser view, HTML file, or PDF.
- [~] Add the backup report location to the meeting notes.

### Evidence Needed

- Saved backup generated report.
- Backup report screenshot.
- Note showing where the backup report is stored.

## 4. Presentation Slides

Owner: Brittany  
Priority: High  
Current status: In progress

Why this needs improvement: The slides are mostly complete and already show the project problem, solution, prototype workflow, testing evidence, team roles, lessons learned, and final status. Only a few slides and final review items remain before presentation practice.

### Small Tasks

- [x] Create or update the Week 7 presentation draft.
- [x] Review the title slide for project name and team name.
- [x] Confirm the problem statement slide is clear.
- [x] Confirm the solution slide explains the AAR Generator in plain language.
- [x] Confirm the prototype workflow slide matches the actual app.
- [x] Confirm the technology stack slide is accurate.
- [x] Confirm the testing evidence slide matches actual testing.
- [x] Add final homepage screenshot.
- [x] Add final completed form screenshot.
- [x] Add final generated report screenshot.
- [x] Add final 5 Whys screenshot.
- [x] Add final recommendations screenshot.
- [x] Add final export-controls screenshot if space allows.
- [x] Confirm Brittany's speaking section is clear.
- [~] Confirm Garrett's speaking section is clear.
- [~] Confirm Mike's speaking section is clear.
- [x] Add or update lessons learned.
- [ ] Add backup demo note.
- [~] Check every slide for spelling and grammar.
- [~] Check every slide for text that is too small.
- [~] Check every slide for crowded content.
- [~] Check every slide for screenshots that are blurry.
- [~] Confirm no slide shows an API key or private configuration.
- [ ] Save the final deck in the required format.

### Evidence Needed

- Updated PowerPoint deck.
- Final screenshot list.
- Speaking-role notes.
- Slide review notes.

## 5. Week 8 Final Report

Owner: Brittany  
Priority: High  
Current status: Complete

Why this needed improvement: The Week 8 journal needed clear evidence of progress, testing, blockers, lessons learned, contribution, and meeting attendance. The journal was prepared as a Word document for submission use, not as a GitHub Markdown draft.

### Small Tasks

- [x] Start the Week 8 journal draft.
- [x] Add a signature page.
- [x] Add milestones achieved this week.
- [x] Add brief descriptions for each milestone.
- [x] Add subtasks completed by Brittany.
- [x] Add subtasks completed by Garrett.
- [x] Add subtasks completed by Mike.
- [x] Add detailed testing descriptions.
- [x] Add final screenshot evidence.
- [x] Add lessons learned.
- [x] Add team contribution section.
- [x] Add progress compared to plan.
- [x] Add plan adjustments if needed.
- [x] Add Week 8 blockers.
- [x] Add meeting attendance and meeting discussion summary.
- [x] Confirm the signature page has Brittany, Garrett, and Mike.
- [x] Confirm each signature line keeps `Date:` on the same line as `Signature:`.
- [x] Review grammar and sentence clarity.
- [x] Export the journal as a PDF.
- [x] Confirm the PDF opens correctly.
- [x] Submit the PDF before Friday if possible.
- [x] If Friday is not possible, submit by the Sunday deadline.

### Evidence Needed

- Week 8 journal DOCX draft.
- Week 8 journal PDF.
- Signature page.
- Meeting log summary.
- Screenshot evidence.

## 6. Meeting Log And Meeting Discussion

Owner: Brittany  
Priority: High  
Current status: Complete

Why this needed improvement: Meeting notes prove attendance, planning, assigned work, and blockers. Week 7 meeting and chat details were summarized for the journal and final evidence.

### Small Tasks

- [x] Add Week 8 meeting entry.
- [x] Add planned Week 8 meeting topics.
- [x] Add planned Week 8 owner assignments.
- [x] Record exact Week 8 attendance.
- [x] Record if anyone was absent.
- [x] Record the meeting start time.
- [~] Record the meeting end time.
- [x] Record final demo incident decision.
- [x] Record screenshot owner.
- [x] Record backup report owner.
- [~] Record speaking roles.
- [x] Record that the homepage now uses a full-page background image.
- [ ] Record GitHub push/sync plan.
- [x] Record any final blockers.
- [x] Add Microsoft Teams chat notes if useful.
- [x] Make sure Week 7 meeting notes are summarized in the journal.

### Evidence Needed

- Updated Week 8 meeting log.
- Attendance record.
- Owner assignments.
- Blocker notes.

## 7. Backend Polish

Owner: Garrett  
Priority: Medium  
Current status: Complete

Why this needs improvement: The backend is working, but Garrett still needs a clean explanation for the final demo. The team should avoid risky backend changes unless they are needed for demo reliability.

### Small Tasks

- [x] Confirm the backend starts successfully.
- [x] Confirm the report-generation route works.
- [x] Confirm the final demo incident works through the backend.
- [x] Confirm fallback/mock behavior still works.
- [x] Confirm no API key is printed in screenshots or documentation.
- [x] Confirm backend tests pass before final demo practice.
- [x] Review backend comments for anything confusing or outdated.
- [x] Remove or update comments that no longer match the code.
- [x] Confirm 5 Whys output is incident-specific.
- [x] Confirm recommendations are incident-specific.
- [x] Confirm technical audience output has technical detail.
- [x] Confirm executive audience output is easier for leadership to read.
- [x] Prepare a short backend explanation for Garrett.
- [x] Prepare one sentence explaining mock fallback.
- [x] Prepare one sentence explaining OpenAI/API mode.
- [x] Prepare one sentence explaining why 5 Whys helps the report.

### Evidence Needed

- Backend test result.
- Final demo report output.
- Garrett's backend talking points.

## 8. Frontend Polish

Owner: Mike  
Priority: Medium  
Current status: Complete

Why this needs improvement: The frontend is the part the audience will see most during the demo. It needs to look clean, guide the user, and make report output easy to read.

### Small Tasks

- [x] Confirm the homepage loads.
- [x] Confirm the report form loads.
- [x] Confirm sample incident autofill works if available.
- [x] Confirm the user can enter incident title.
- [x] Confirm the user can enter incident date.
- [x] Confirm the user can enter incident summary.
- [x] Confirm the user can enter timeline details.
- [x] Confirm the user can enter log snippets.
- [x] Confirm the user can enter impact details.
- [x] Confirm the user can enter remediation steps.
- [x] Confirm the user can enter open questions.
- [x] Confirm required-field validation appears when needed.
- [x] Confirm validation messages are easy to understand.
- [x] Confirm loading state appears while a report is being generated.
- [x] Confirm technical audience button or control works.
- [x] Confirm executive audience button or control works.
- [x] Confirm generated report is readable.
- [x] Confirm 5 Whys section is readable.
- [x] Confirm recommendations section is readable.
- [x] Confirm Copy Report works.
- [x] Confirm Editable Text download works.
- [x] Confirm HTML download works.
- [x] Confirm Save as PDF option is available.
- [x] Confirm smaller-screen layout is usable.
- [x] Confirm no visible text overlaps.
- [x] Confirm buttons and labels fit their containers.
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
Current status: Complete

Why this needed improvement: Week 7 prepared the team for Week 8 final report work by organizing project wording, testing evidence, contribution notes, meeting evidence, and screenshots before final submission week. The Week 8 final paper draft is now written and signed.

### Small Tasks

- [x] Create a list of final report sections.
- [x] Collect project description wording.
- [x] Collect problem statement wording.
- [x] Collect solution summary wording.
- [x] Collect technology stack details.
- [x] Collect setup and usage evidence.
- [x] Collect testing summary notes.
- [x] Collect screenshot evidence.
- [x] Collect known limitations.
- [x] Collect future improvements.
- [x] Collect Brittany's contribution notes.
- [x] Collect Garrett's contribution notes.
- [x] Collect Mike's contribution notes.
- [x] Collect meeting log evidence.
- [x] Collect GitHub evidence.
- [x] Complete the final paper draft.
- [x] Confirm Brittany, Garrett, and Mike signed the final paper draft.
- [x] Identify missing final report content before Week 8 starts.

### Evidence Needed

- Final report outline.
- Evidence list.
- Missing-content list for Week 8.

## 12. Current Blockers

| Blocker | Owner | Impact | Small Next Step |
|---|---|---|---|
| GitHub push/sync needs confirmation. | Team | Documentation and code updates may not be visible to teammates or instructor yet. | Check Git status, choose files to push, and confirm local-only DOCX drafts stay off GitHub. |
| Presentation practice still needs to happen. | Team | The final presentation may feel unorganized without a full run-through. | Confirm Brittany, Garrett, and Mike's speaking sections and practice the demo from start to finish. |
| Final presentation slides are still being reviewed. | Brittany and team | The deck is mostly complete, but a few slides and speaker sections still need polish. | Finish the last slides, review grammar, and complete a practice run before final submission. |
| Final generated reports need final-use confirmation after formatting fixes. | Brittany and Garrett | Old downloaded reports may still show earlier formatting issues if reused. | Use the newest generated reports and keep backup screenshots ready for the demo. |

## 13. Done Criteria

An improvement can be marked complete when:

- [ ] The task has a named owner.
- [ ] The task has been tested, reviewed, or discussed.
- [ ] The evidence exists as a screenshot, saved report, test result, meeting note, slide, or journal section.
- [ ] The result does not expose an API key, `.env` file, terminal secret, or private configuration.
- [ ] The status is updated in the correct tracker file.
- [ ] The task is included in the final presentation, final report, or final evidence package if it supports final submission.
- [ ] The task is included in the final presentation or final report if it supports final submission.

## 14. Meeting Review Checklist

Use this section during Week 8 final review and demo practice.

- [x] Did we select the final demo incident?
- [x] Did we assign screenshot responsibilities?
- [x] Did we assign backup report responsibility?
- [~] Did we confirm speaking roles?
- [x] Did we confirm the homepage background image is ready?
- [~] Did we confirm what files should go to GitHub?
- [x] Did we confirm what files should stay local-only?
- [x] Did we confirm the final report and Week 7 journal evidence list?
- [~] Did we choose a demo practice time?
- [x] Did we identify anything that must wait until Week 8?
- [x] Did we confirm the final presentation slide order?
- [x] Did we confirm the final status slide wording?
- [x] Did we regenerate final report outputs after formatting fixes?
- [ ] Did we complete a timed practice run?
