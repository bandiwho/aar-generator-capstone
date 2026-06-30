# Areas To Improve

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Course: CSC 482 Capstone Project II  
Team members: Brittany, Garrett, Mike

## Purpose

This page tracks the main areas that still need improvement before the final demo. It shows what needs to be done, why it matters, who owns the work, and what evidence should be collected for the weekly journal and final report.

## Improvement Chart

| Area to Improve | Why It Matters | Owner | Tasks to Complete | Priority | Evidence Needed |
|---|---|---|---|---|---|
| Technical vs executive report variation | The advanced project requirement is to support multiple reporting styles. The two outputs need to look clearly different. | Garrett | Update the LLM prompt logic so technical reports use detailed security sections and executive reports use leadership-focused sections. | High | Screenshots of one technical report and one executive report from the same incident. |
| Report structure | The generated report should be easy to read, review, and submit as an AAR draft. | Garrett | Improve section headings, 5 Whys root-cause analysis, recommendations, remediation, and lessons learned. | High | Generated report screenshot showing clean sections. |
| Frontend audience selector | Users need to clearly understand that they can choose technical or executive output. | Mike | Confirm the audience dropdown works, make the selected audience obvious, and ensure it displays clearly in the generated report output. | High | Screenshot of the audience selector and output metadata. |
| Generated report display | The output area needs to look polished for screenshots, demo, and presentation. | Mike | Improve spacing, headings, copy/paste readability, and visual layout of the generated report. | Medium | Screenshot of generated report display. |
| Form usability | The form should be easy for a user to complete without guessing what each field means. | Mike | Improve labels, placeholder examples, required-field clarity, and spacing. | Medium | Screenshot of the completed form before submission. |
| Testing evidence | The weekly journal requires detailed testing descriptions and demo screenshots. | Brittany | Test the app using sample incidents, compare technical and executive outputs, record what worked, and collect screenshots. | High | Testing notes and screenshots with no API key visible. |
| Sample incident coverage | Strong sample incidents make testing and demo preparation easier. | Brittany | Confirm sample incidents cover phishing/account compromise, ransomware, cloud misconfiguration, insider exposure, and web app attack scenarios. | Medium | Updated sample incident file and screenshot of at least one test. |
| Error handling | The demo should still be understandable if the API fails or the user enters weak input. | Garrett and Mike | Improve backend error messages, frontend error display, and fallback behavior. | Medium | Screenshot of a clear error or fallback message. |
| Meeting and contribution evidence | The instructor grades individual contributions, so each member's work needs to be visible. | Brittany | Keep `MEETING_LOG.md`, `MILESTONE_TODOS.md`, and `SHARED_DELIVERABLES_CHECKLIST.md` updated with owner names and completion status. | High | Meeting log entry and updated checklist screenshots. |
| Final presentation readiness | The team needs to be ready for the July 27-28 final presentation. | Team | Prepare final report, slides, demo script, speaking roles, backup screenshots, and backup generated report. | High | Final report PDF, slide deck, and demo practice notes. |

## Week 5 Focus

| Team Member | Focus This Week | Expected Output |
|---|---|---|
| Brittany | Testing evidence, documentation updates, meeting log, screenshot collection, and weekly journal draft. | Updated GitHub docs, screenshots, testing notes, and journal content. |
| Garrett | Stronger technical vs executive prompt variation, 5 Whys analysis, recommendations, and backend testing. | Improved report-generation logic and test evidence. |
| Mike | Frontend audience selector, form usability, generated report display, and demo screenshot support. | Cleaner form and report output screenshots. |

## Done Criteria

An improvement can be marked complete when:

- The related code or documentation is updated.
- The owner has tested or reviewed the change.
- A screenshot, test result, meeting note, or GitHub commit shows evidence.
- The task is reflected in the weekly journal or final report if required.
