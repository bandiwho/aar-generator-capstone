# Team 1 Meeting Log

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike

## Purpose

This meeting log documents weekly team attendance, discussion topics, assigned tasks, completion status, and ongoing collaboration. It supports the weekly journal, midterm report, and final report requirements.

## Meeting Requirements

For each meeting, record:

- Date and time
- Who attended and who was absent
- Topics discussed
- Tasks assigned and completion status

## Weekly Collaboration Summary

Team 1 meets every Tuesday to review project progress, assign next steps, and check that the work is aligned with the course schedule. The team also uses Microsoft Teams chat throughout the week to share updates, troubleshoot issues, and keep everyone informed. Brittany, Garrett, and Mike all participate in the weekly planning and project work.

## Meeting Entries

### Week 4 Meeting

Date and time: Tuesday, June 23, 2026, 6:30 PM
Location: Team meeting and Microsoft Teams follow-up chat
Attended: Brittany, Garrett, Mike
Absent: None

Topics discussed:

- Reviewed the Week 4 requirement to code and test planned project tasks.
- Discussed the OpenAI API model issue and the need to use automatic model selection from the class API project.
- Reviewed the prototype form fields and confirmed that incident type needed to be included.
- Checked progress on the backend report-generation workflow, frontend form, README, milestone todos, and shared deliverables checklist.
- Planned screenshot evidence for testing and the midterm report.

Tasks assigned and completion status:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Update README, milestone todos, shared deliverables checklist, sample incidents, and report wording. Review grammar, organization, and testing evidence. | Completed and continuing |
| Garrett | Maintain backend schema, report-generation service, OpenAI client integration, automatic model selection, mock fallback, and tests. | Completed and continuing |
| Mike | Maintain frontend form workflow, add user-facing fields, improve generated report display, and support demo screenshots. | Completed and continuing |

### Week 5 Meeting

Date and time: Tuesday, June 30, 2026, 6:30 PM
Location: Team meeting and Microsoft Teams follow-up chat
Planned attendees: Brittany, Garrett, Mike
Absences: Everyone was present by 6:29PM meeting ended at 7:12PM

Planned topics:

- Review Week 5 Weekly Journal requirements.
- Confirm GitHub achievements are committed and pushed.
- Review technical and executive report style work.
- Review 5 Whys root-cause analysis and recommendations.
- Confirm testing screenshots and notes for the weekly journal.
- Assign any remaining fixes before the team report is exported to PDF.

Planned tasks:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Keep weekly meeting log current, update documentation, collect screenshots, compare report tone, and prepare weekly journal content. | In Progress |
| Garrett | Continue backend report style logic, 5 Whys analysis, recommendations, OpenAI integration, and test coverage. | Complete |
| Mike | Continue frontend style controls, report output formatting, demo workflow, and screenshot support. | Complete |

## During Meeting/Afterthoughts Topics:
- Discussed Layout 
- Update dropdown audience to clickable audience button for readability.
- Change Executive Summary to matched the correct audience.
- Layout of submit = Generate button- We decided placement is fine.
- Discussed adding an Areas of Improvement page to show which improvements were most important and where Brittany should take screenshots to provide evidence of improvements.
- There was suggestion of keeping a database of logged past incident reports. It is beyond scope. We will focus on requirement output and if we have extra time we may implement.                   - Helper text to indicate to user who report is written for.
- Section of output shows buttons. Depending on time they may be labels or buttons that show summary. 
- Make Sample incidents follow design of layout and more descriDiptive.

## Chat Topics:

6/29

- Preparation for meeting
  
06/30
- Improving GitHub layout
- Changing datye field
- Adding visual hints to required fields that need to be filled out.
- Hiding errors from users
  
07/01
- Discuss Progress
- Blocker - sample incidents update had been resolved.
  
07/02
- Garrett updated backend
- Progression details
- Testing started
- Mike Added Copy button
- Blocker - Frontend updates resolved. Screenshot are able to be taken.
  
07/03
- View Journal
- Last minute updates for Journal
- Signatures
- Premtive Discussion For Next Goals

### Week 6 Meeting

Date and time: Tuesday, July 7, 2026, 6:30 PM
Location: Team meeting and Microsoft Teams follow-up chat
Planned attendees: Brittany, Garrett, Mike
Absences: No absences
Meeting lasted 6:28 - 7:02 (34 minutes). The meeting went well with no major blockers. Brittany had an issue with VS Code not getting a credential token from GitHub to pull updates.

Planned topics:

- Review Week 6 Weekly Journal requirements.
- Confirm GitHub achievements are committed and pushed.
- Review validation, error handling, fallback behavior, and sample incident testing.
- Confirm testing screenshots and notes for the Week 6 journal.
- Review Copy Report and Download Report behavior, including whether the downloaded HTML report layout is clean enough for final evidence.
- Assign fixes from the Week 6 testing notes.

Planned tasks:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Update meeting log, collect screenshots, test at least three incident scenarios, track bugs, and prepare Week 6 journal content. | Planned |
| Garrett | Improve backend error handling, fallback behavior, revision support, and test coverage. | Planned |
| Mike | Improve required-field validation, copy/export behavior, downloaded report layout, and frontend screenshot support. | Planned |

- This week is focused on testing. Everything seems to be working, but the team still needs to review the project for quality. Mobile support is optional, not a required feature. The other core focus is wrap-up. The team needs to decide who will speak about each section and prepare presentation notes. Brittany would like most of the slides established early so the team knows what to discuss. Brittany would also like to start the final report soon so the team can clearly define where the project will end.
- Export review note: The Download Report feature successfully saves the generated report as an HTML file, but the layout should be reviewed before using it as a polished final report. Screenshots or Print/Save as PDF may be better for final evidence if the downloaded HTML formatting looks crowded or shows raw Markdown formatting.
  
## Chat Topics

- 07/07
- Reviewed Copy Report and Download Report behavior.
- Downloaded HTML report preserved the report title, audience, sections, 5 Whys, recommendations, and open questions.
- Formatting concern: the downloaded HTML may show raw Markdown styling or crowded list formatting, so the team should use screenshots or Print/Save as PDF for polished evidence if needed.
- End of week we plan to revisit demo prep.
- Focal point is polish ready and next week really a last minute change week allowing us to focus on final report and demo
- May send message to teacher about early release of final report and slide so that we correctly create them.
- Mike is looking into mobile view stretch goal.
- Brittany's VS Code was not keeping up with GitHub because it could not get credential tokens. Some updates appeared to be lost during troubleshooting, but the issue was resolved after Brittany closed out, logged out, and signed back in.
  
- 07/08
- Mikes updates on what improvements to buttons.
- Even thought Brittany's computer was resolved night before some residual issues were going one finally a VS update popped up and fully resolved the issue.
- Brittany found report formatting issues.
- 07/09
- Formatting issues were discussed.
- Backend and Frontend needed fixes
- Fontend was trying to bold words and when displayed it showed ** around words that were meant to be bolded
- Backend had pulled lower cases bullets trying to break up point as bullets and 5 why section was hard to read and pull from clearly.

- 07/09
- Mike fixed Mobile/Small Screenview
- Mike provided screenshots for report.
- Brittany informed team all testing had passed. 
- Garretts backend was discussed and determined to do minor edits as far as not adding in extra alerts letting user know errors or if in mock mode. It is not in scope and we did not want to break anything as everything is passing. The other issue is it alreading takes 19 seconds loading time and did not want to extend that.
  
### Week 7 Meeting

Date and time: Tuesday, July 14, 2026, 6:30 PM
Location: Team meeting and Microsoft Teams follow-up chat
Planned attendees: Brittany, Garrett, Mike
Absences: No absences
Meeting lasted 6:32 - 7:26 (58 minutes). 
Meeting purpose: Use Week 7 to move from building and testing into final presentation preparation, journal evidence, screenshot planning, and final demo readiness.

Pre-meeting notes:

- Week 7 meeting agenda created.
- Week 7 journal draft started with signature page.
- Week 7 presentation copy updated.
- Week 7 Areas To Improve page updated with detailed small checklist tasks.
- Main remaining items are final screenshots, speaking-role confirmation, backup generated report, GitHub push/sync confirmation, and final demo practice meeting times.

Planned topics:

- Review Week 7 Weekly Journal requirements.
- Confirm GitHub achievements are committed and pushed.
- Review final documentation, screenshots, presentation draft, and demo script.
- Confirm each team member can explain their section of the project.
- Assign final polish tasks before final review.
- Select the final demo incident and confirm whether the phishing/Microsoft 365 sample should be used.
- Review the updated Areas To Improve page and use it as the Week 7 task checklist.

Detailed agenda:
   - Confirm Week 7 is focused on documentation, screenshots, demo practice, and final presentation preparation.

1. Documentation review
   - Review `README.md` Week 7 status.
   - Review `MILESTONE_TODOS.md` Week 7 tasks.
   - Review `SHARED_DELIVERABLES_CHECKLIST.md` Week 7 checklist.
   - Review `AREAS_TO_IMPROVE.md` Week 7 improvement tasks.
   - Confirm `USER_GUIDE.md` is ready as the stretch-goal user guide.
   - Confirm Week 7 journal and meeting agenda are local-only Word files, not GitHub Markdown files.

2. Final demo scenario
   - Decide whether the phishing/Microsoft 365 account compromise sample will be the final demo incident.
   - Confirm the selected incident has enough timeline, log, impact, remediation, and open-question detail.
   - Confirm the selected incident works for both technical and executive report styles.
   - Confirm the team can explain why the selected incident is a good demo scenario.

3. Presentation preparation
   - Review the updated Week 7 presentation information.

4. Speaking roles
   - Confirm Brittany explains project purpose, documentation, quality review, journal evidence, and lessons learned.
   - Confirm Garrett explains backend workflow, LLM/API behavior, mock fallback, 5 Whys, recommendations, and backend testing.
   - Confirm Mike explains frontend workflow, form fields, sample incident flow, audience selection, report display, and copy/download behavior.
   - Confirm who starts and ends the live demo.

5. GitHub and file organization
   - Check which files are ready to push.
   - Confirm `USER_GUIDE.md` should be included in GitHub as the stretch-goal documentation item.

6. Final blockers and next meeting
   - Confirm demo practice time.
   - Confirm Presentation and Final Paper details.
   - Mike and Garretts key points. 
   - We now need to run presentation scenario through codex and use that result too.
   - Complete rough draft of slides over the weekend.


Planned tasks:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Finalize documentation, update meeting log, prepare Week 7 journal content, organize screenshot evidence, review grammar, and update presentation materials. | Complete |
| Garrett | Confirm backend report generation works with the final demo data, prepare backend explanation, confirm fallback/mock behavior, and prepare 5 Whys/recommendations talking points. | Planned |
| Mike | Confirm frontend demo flow, polish homepage and report display, confirm visual assets load correctly, review smaller-screen layout, and prepare frontend walkthrough. | Planned |
| Team | Select final demo incident, assign speaking roles, prepare backup report/screenshots, practice the demo, and confirm GitHub/local-only file organization. | Complete |

Detailed owner checklist:

| Owner | Small tasks to confirm | Evidence needed |
|---|---|---|
| Brittany | Confirm Week 7 journal draft, meeting agenda, updated checklist, updated Areas To Improve page, and presentation draft are organized. | Journal DOCX, meeting agenda DOCX, updated Markdown trackers, presentation deck, screenshot list. |
| Brittany | Review all writing for grammar, clarity, and correct Week 7 wording. | Clean README, checklist, meeting log, improvement tracker, and journal draft. |
| Garrett | Confirm final demo incident generates a complete report through the backend. | Generated report output and backend test confirmation. |
| Garrett | Prepare backend talking points for the final presentation. | Short explanation of report-generation route, LLM/API mode, mock fallback, 5 Whys, and recommendations. |
| Mike | Confirm homepage, form, audience controls, generated report view, and export controls are ready for screenshots. | Frontend screenshots and demo walkthrough notes. |
| Mike | Confirm the homepage background image renders correctly. | Decision note recorded in meeting log and checklist. |
| Team | Practice the demo and prepare backup materials. | Demo practice notes, backup screenshots, backup generated report, and final speaking order. |

Decisions to record after meeting:

- Speaking order: Brittany -> Mike -> Garrett -> Brittany
- Brittany speaking section: Opening, Description, Our Solution, Documentation, Testing, Closing
- Garrett speaking section: Backend
- Mike speaking section: Frontend
- Homepage background image decision: The frontend now uses a background image.
- Demo practice date/time: TBA

**Chat Timeline Summary: July 14 - July 17**

- July 14

- The team focused on Week 7 submission preparation and final demo evidence. Brittany asked Mike to complete the frontend portion of the presentation so those points could also be used in the final paper. Brittany reviewed the generated report outputs and did not find major content errors. The team planned to finish updates by Friday or Saturday so final screenshots could be added to the final paper.

- Brittany shared both technical and executive generated report outputs for team review. A few formatting issues reappeared, including the PDF export moving close to the page edge and repeated “likely owner” wording. Brittany noted that these looked like simple fixes and planned to review them before copying final files.

- uly 15

- The formatting issues were reviewed and linked to the Python update. Brittany confirmed that the issues were fixed. The team continued reviewing the technical audience output and prepared the Week 7 journal for completion.

- July 16

- The team reviewed final demo workflow and frontend demo documentation through a pull request. Mike’s update added final presentation demo workflow notes, frontend walkthrough guidance, backup plan information, and speaking notes. Brittany clarified that the main focus was the frontend demo explanation and recommended using the same incident for both technical and executive views so the audience could clearly compare the difference between report styles.

- The team also discussed presentation timing. 

- July 17

- The presentation file was unlocked. The team continued preparing for Week 8 work, including final slides, backend explanation, frontend explanation, demo practice, and final presentation readiness.

### Week 8 Meeting

Date and time: Tuesday, July 21, 2026, 6:30 PM

The Week 8 meeting was moved to the weekend so the team could finish the remaining presentation slides before practicing. The team used Microsoft Teams chat on Tuesday to confirm progress, review final report status, discuss remaining presentation work, and keep everyone updated. This was sufficient for the Week 8 check-in because the main remaining task was presentation practice. The team agreed that practicing closer to the final presentation date would allow better preparation and a smoother run-through.
Location: Team meeting and Microsoft Teams follow-up chat

Planned attendees: Brittany, Garrett, Mike
Absences: To be recorded after meeting

Planned topics:

- Review Week 8 final report requirement.
- Review presentation slides requirement.
- Review final presentation preparation tasks.
- Confirm the final presentation window is July 27-28, 2026.
- Assign speaking roles and final demo responsibilities.
- Confirm backup screenshots and backup generated report are ready.

Planned tasks:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Finalize final report, review slides, confirm documentation quality, update meeting log, and prepare project-purpose speaking notes. | Planned |
| Garrett | Confirm backend and LLM generation, prepare backend explanation, prepare fallback plan, and verify testing evidence. | Planned |
| Mike | Confirm frontend demo workflow, polish report display, prepare frontend explanation, and verify demo screenshots. | Planned |

### Final Presentation

Date range: July 27 - July 28, 2026  
Planned presenters: Brittany, Garrett, Mike

Presentation responsibilities:

| Team member | Presentation responsibility | Backup material |
|---|---|---|
| Brittany | Project purpose, final report, documentation, quality review, team organization, and lessons learned. | Final report PDF, meeting log, and contribution notes |
| Garrett | Backend workflow, LLM integration, testing evidence, and fallback plan. | Backend notes, test results, and backup generated report |
| Mike | Frontend workflow, user input form, generated report display, and live demo flow. | Demo screenshots and frontend walkthrough notes |

## Notes Before Submission

- Add the exact meeting time before exporting the weekly journal or team report.
- Save screenshots without showing the OpenAI API key.
- Include this meeting log or a summarized version of it in the weekly journal, midterm report, and final report.
