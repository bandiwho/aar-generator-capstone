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
- Discussed Addition on Areas of Improvement page = Help show which Improvements were more importand and where Brittany should take screenshots to provide evidence of improvements.
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
Meeting lasted 6:28 - 7:02 (34 Minutes) Meeting went well no huge blockers. Brittany did have an issue with vs code not getting a creditial token from github to do pulls. 

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

- This week is focusing on testing. Everything seems to be working. Just need to review to ensure quality. Mobile is a option. It is not a needed requirement. Other core focus is on wrapup. We need to decide who is going to talk about what and prepare for speeches. I would like to get most of slides established on what we are going to talk about I know we do not have the assignment yet but we can prepare. I will also like to start with the final report. That maybe a weekend thing because as this is not a crucial week we need to figure out where we are going to end our project.
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
- Brittanys VS was not keeping up with github due to an inability to get credential tokens. Deletion of some updates occurred but the good thing at one point it said sync 139 things. Brittany closed out and logged out of everything and though some things were lost, 139 things were not altered with no guarantee what. Issue was resolved.
  
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
Absences: To be recorded after meeting

Planned topics:

- Review Week 7 Weekly Journal requirements.
- Confirm GitHub achievements are committed and pushed.
- Review final documentation, screenshots, presentation draft, and demo script.
- Confirm each team member can explain their section of the project.
- Assign final polish tasks before final review.

Planned tasks:

| Team member | Assigned work | Status |
|---|---|---|
| Brittany | Finalize documentation, prepare presentation outline, capture screenshots, update meeting log, and prepare Week 7 journal content. | Planned |
| Garrett | Clean up backend code, confirm report generation works with final demo data, and prepare backend explanation. | Planned |
| Mike | Polish homepage and report display, confirm visual assets load correctly, and prepare frontend demo walkthrough. | Planned |

### Week 8 Meeting

Date and time: Tuesday, July 21, 2026, 6:30 PM
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
