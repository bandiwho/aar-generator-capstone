# Security Incident Postmortem: Automated After-Action Report Generator

## Project Details

| Field | Details |
|---|---|
| Project | Security Incident Postmortem: Automated After-Action Report (AAR) Generator |
| Course | CSC 482 Capstone Project II |
| Team | Capstone Project Team 1: Brittany, Garrett, Mike |
| Planning Window | June 15 - July 24, 2026 |
| Final Presentation | July 27 - July 28, 2026 |
| Deliverable | Lightweight web application that accepts incident details and generates structured After-Action Report drafts |

## Project Goal

Build a lightweight web-based tool that helps users create professional after-action reports after cybersecurity incidents. The user enters incident details such as raw log data, incident timelines, affected systems, known impact, and remediation steps. The system uses an LLM-supported backend workflow to organize the information, support root-cause analysis, and generate a structured report draft.

## Core Capabilities

- [~] Incident detail entry through a clear frontend form.
- [x] Support for timelines, log snippets, impact notes, and remediation steps.
- [x] LLM-supported report generation workflow.
- [x] 5 Whys root-cause analysis.
- [x] Technical and executive reporting styles.
- [~] Realistic sample incident data for testing.
- [x] Demo workflow documentation for presentation practice.
- [x] Final user guide added for stretch-goal documentation.
- [x] GitHub repository for shared source code and documentation.

## Current Project Status

- [x] GitHub repository created for the team project.
- [x] Updated prototype folder organized.
- [x] README polished to match the instructor's expected format.
- [x] Project description, team member descriptions, timeline, milestones, and tasks added to the README.
- [x] Project plan converted into Markdown for GitHub viewing.
- [x] Checkboxes added for weekly tasks, MVP requirements, testing, deliverables, and completion criteria.
- [x] Shared deliverables checklist added.
- [x] Demo workflow instructions added.
- [x] User guide added to explain setup, form use, report review, export options, screenshots, and troubleshooting.
- [x] Form field review completed.
- [x] Realistic sample incidents added for testing and demo use.
- [x] Sample incidents page created in Markdown for easier GitHub viewing.
- [x] Backend schema work added to define incident input and report output structure.
- [x] FastAPI backend route added for JSON report generation.
- [x] Frontend form route added so users can submit incident details from the browser.
- [x] Prompt-building workflow added for structured AAR generation.
- [x] Real LLM mode tested with the class API key project using automatic model selection.
- [x] Mock fallback kept available so the demo can still run if the API is unavailable.
- [x] Backend tests added and passing.
- [x] Sample incidents Markdown updated to match the prototype form fields.
- [x] Testing checklist added to document sample incident validation and pass/fail criteria.
- [x] Meeting log added to document weekly attendance, topics, assigned tasks, and contribution evidence.
- [x] Week 5 README, todos, and shared deliverables checklist updated for the weekly journal requirements.
- [x] Technical and executive report styles added for different reporting audiences.
- [x] 5 Whys root-cause analysis and recommendations added to the generated report structure.
- [x] Week 6 validation, error handling, fallback behavior, sample incident testing, and journal submission are complete.
- [~] Week 7 documentation, demo screenshots, presentation update, meeting agenda, and journal draft are in progress.

## Current Week Focus

Week 7 focus: prepare the project for final presentation by organizing documentation, updating the presentation deck, drafting the Week 7 journal, preparing meeting discussion points, collecting final demo screenshots, and confirming team speaking roles.

The Week 6 journal has been turned in. The Week 7 journal should summarize final documentation work, presentation preparation, demo practice, screenshot evidence, lessons learned, each team member's contribution, meeting attendance, progress compared to the project plan, and any needed plan adjustments.

Current Week 7 responsibilities:

| Member | Current Focus | Evidence Needed |
|---|---|---|
| Brittany | Finalize documentation, prepare Week 7 journal evidence, update presentation materials, organize screenshots, and track meeting discussion points. | Week 7 journal draft, meeting agenda, updated deck, checklist updates, screenshot list, and meeting log updates. |
| Garrett | Confirm backend explanation, final demo data behavior, fallback behavior, and 5 Whys/report-generation explanation. | Backend talking points, test confirmation, fallback explanation, and final demo data confirmation. |
| Mike | Confirm frontend demo flow, report display, copy/download behavior, and visual polish items. | Frontend walkthrough notes, screenshots, final demo flow confirmation, and confirmation that the homepage background image renders correctly. |
| Team | Confirm final demo incident, assign speaking roles, prepare backup materials, push updates to GitHub, and practice the demo. | Demo rehearsal notes, backup screenshots, backup generated report, GitHub sync confirmation, and Week 7 contribution evidence. |

## Team Member Descriptions

| Member | Role | Contribution Focus |
|---|---|---|
| Brittany | Project leader, documentation lead, quality reviewer | Organizes project files, tracks requirements, reviews grammar and formatting, maintains checklists, and prepares journal and submission materials. |
| Garrett | Backend development and report-generation architecture | Designs backend logic, defines JSON data structures, supports the LLM-driven analysis workflow, and prepares report-generation logic for integration. |
| Mike | Frontend development and demo workflow | Plans and builds the frontend interface, reviews user input requirements, improves the form layout, and prepares the prototype for demonstration. |

## Timeline

| Done | Dates | Milestone | Scheduled Work |
|---|---|---|---|
| [x] | June 15 - June 21 | Milestone 1 | Repository setup, README, sample incidents, form field review, and demo workflow instructions |
| [x] | June 22 - June 28 | Milestone 2 | Backend data structure, report-generation workflow, frontend form refinement, and first LLM-generated report draft |
| [x] | June 29 - July 5 | Milestone 3 | Technical and executive report styles, improved 5 Whys analysis, output formatting, testing screenshots, and meeting log evidence |
| [x] | July 6 - July 12 | Milestone 4 | Testing, error handling, validation, sample incident review, weekly journal, and meeting log evidence |
| [~] | July 13 - July 19 | Milestone 5 | Documentation, screenshots, presentation draft, demo script, weekly journal, and meeting log evidence |
| [ ] | July 20 - July 24 | Milestone 6 | Final report, presentation slides, final presentation preparation, final polish, and submission package |
| [ ] | July 27 - July 28 | Final Presentation | Final presentation and live demonstration |

## Milestone Task Plan

### Milestone 1: Repository Setup and Project Documentation

Dates: June 15 - June 21, 2026  
Goal: Set up the GitHub repository, organize the prototype, and document the Week 3 project work.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [x] | Brittany | Prepare README for GitHub assignment | README with project description, team descriptions, milestones, and task lists | README matches the assignment requirements |
| [x] | Brittany | Review form fields | `FORM_FIELD_REVIEW.md` | Required MVP fields confirmed |
| [x] | Brittany | Write demo workflow instructions | `DEMO_WORKFLOW_INSTRUCTIONS.md` | Demo steps are clear enough for the team to follow |
| [x] | Brittany | Create realistic sample incidents | `data/sample_incidents.json` | Multiple security incident scenarios are available for testing |
| [x] | Garrett | Review backend responsibilities | Backend planning notes and JSON structure direction | Backend work is scoped for report-generation logic |
| [x] | Garrett | Add backend schema work | Backend schema definitions for incident input and report output | Data structure is ready for report-generation integration |
| [x] | Mike | Plan frontend workflow | Frontend layout direction and weekend build plan | Interface work is scoped for the demo workflow |

### Milestone 2: Backend and Frontend Foundation

Dates: June 22 - June 28, 2026  
Goal: Define the data structure, improve the form, and connect the workflow needed for report generation.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [x] | Garrett | Define JSON structure for incident input | Request/response structure for report generation | Data fields support timeline, logs, impact, remediation, and open questions |
| [x] | Garrett | Build report-generation workflow | Backend service logic, prompt workflow, OpenAI client integration, and mock fallback | Prototype can produce structured report sections |
| [x] | Mike | Improve frontend form layout | Updated form layout and clearer input sections | Users can enter incident details without confusion |
| [x] | Mike | Improve report output display | Cleaner generated report output area with report metadata | Generated report is readable during demo |
| [x] | Brittany | Review output quality | Sample incidents, checklist updates, and midterm report draft notes | Review notes are ready for Garrett and Mike |

### Milestone 3: Report Style and Root-Cause Analysis

Dates: June 29 - July 5, 2026  
Goal: Improve the generated report, support different reporting audiences, test the Week 5 work, and document team contributions.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [x] | Garrett | Add technical report style support | Technical report generation path | Output includes technical details and evidence references |
| [x] | Garrett | Add executive report style support | Executive report generation path | Output summarizes impact, risk, and recommendations clearly |
| [x] | Garrett | Improve 5 Whys analysis and recommendations | Root-cause and recommendation sections | 5 Whys and recommendations connect incident evidence to likely causes |
| [x] | Mike | Add or improve style controls | Technical/executive selection in UI | User can choose report audience style |
| [x] | Mike | Improve report formatting | Cleaner report display | Generated report is easy to read and screenshot |
| [x] | Brittany | Add meeting log for contribution evidence | `MEETING_LOG.md` | Weekly minutes show attendance, discussion topics, assigned tasks, and completion status |
| [x] | Brittany | Update README, todos, and deliverables for Week 5 | Updated GitHub documentation | GitHub pages match the Week 5 assignment requirements |
| [x] | Brittany | Compare report tone and clarity | Quality review notes and screenshots | Technical and executive outputs match their audiences |

### Milestone 4: Testing and Validation

Dates: July 6 - July 12, 2026  
Goal: Test the prototype with multiple incidents, improve reliability, and document Week 6 journal evidence.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [x] | Brittany | Test app with sample incidents | Testing notes and screenshots | At least three incident scenarios are tested |
| [~] | Garrett | Improve backend error handling | Backend fallback and error handling logic | App handles incomplete or weak input without crashing |
| [x] | Mike | Improve frontend validation | Required-field behavior and user-facing messages | Users understand what information is missing |
| [x] | Brittany | Prepare Week 6 journal evidence | Meeting log, screenshots, testing notes, and contribution summary | Week 6 journal is ready to export as a PDF |
| [x] | Team | Review test results | Bug list and improvement notes | Issues are documented and assigned |

### Milestone 5: Documentation and Demo Preparation

Dates: July 13 - July 19, 2026  
Goal: Prepare the project for final presentation and demonstration while documenting Week 7 journal evidence.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [~] | Brittany | Finalize project documentation | Final README, journal notes, and checklist updates | Documentation is clear and complete |
| [~] | Brittany | Prepare presentation outline | Slide outline and speaker notes | Presentation covers problem, solution, prototype, and lessons learned |
| [ ] | Garrett | Prepare backend explanation | Backend workflow summary | Team can explain how report generation works |
| [ ] | Mike | Prepare demo flow | Demo script and frontend walkthrough | Demo can be completed smoothly |
| [~] | Team | Prepare Week 7 journal evidence | Meeting log, screenshots, testing notes, and contribution summary | Week 7 journal is ready to export as a PDF |

### Milestone 6: Final Polish and Submission

Dates: July 20 - July 24, 2026  
Goal: Finish the prototype, final report, presentation slides, screenshots, and final presentation preparation before the July 27-28 final presentation.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Brittany | Run final quality review | Final grammar, formatting, and requirement check | Submission materials are clean and organized |
| [ ] | Brittany | Finalize final report | Final report PDF and supporting evidence | Report includes project summary, milestones, testing, lessons learned, and team contributions |
| [ ] | Brittany | Finalize presentation slides | Completed presentation deck | Slides cover problem, solution, demo workflow, testing, lessons learned, and contributions |
| [ ] | Garrett | Confirm backend/report generation | Final backend test notes | Report generation works with final demo data |
| [ ] | Mike | Confirm frontend/demo workflow | Final interface check and demo screenshots | Prototype is ready for presentation |
| [ ] | Team | Complete final presentation preparation | Full demo rehearsal, speaker roles, and backup plan | Team can present within the assigned time on July 27-28 |

### Final Presentation

Dates: July 27 - July 28, 2026  
Goal: Present the final AAR Generator project and demonstrate the working prototype.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Brittany | Present project purpose, documentation, and quality review | Speaking notes | Audience understands the problem, requirements, and team organization |
| [ ] | Garrett | Present backend and LLM workflow | Backend explanation and test evidence | Audience understands how report generation works |
| [ ] | Mike | Present frontend and demo workflow | Live demo walkthrough | Audience can see the user workflow from incident input to generated report |
| [ ] | Team | Complete final live demonstration | Final presentation and demo | Presentation is completed during the July 27-28 final window |

## Proposed Demo Scenario

Sample scenario: "Generate an after-action report for a phishing email that led to a Microsoft 365 account compromise."

1. User opens the Security Incident AAR Generator.
2. User enters the incident title, date, summary, timeline, log snippets, known impact, remediation steps, and open questions.
3. User selects either technical or executive report style.
4. The backend organizes the incident details into a structured prompt.
5. The LLM-supported workflow generates a draft report.
6. The report includes a summary, timeline, evidence observations, 5 Whys analysis, root cause, remediation, recommendations, and lessons learned.
7. The team reviews the output for clarity, accuracy, and usefulness.

## Success Criteria

| Area | Measurement |
|---|---|
| Incident input | Form captures the main incident details needed for an AAR draft |
| Report generation | Prototype generates structured report sections from the provided incident details |
| Root-cause analysis | Output includes a usable 5 Whys section |
| Reporting styles | Prototype supports technical and executive audience options |
| Testing | At least three realistic sample incidents are tested |
| Documentation | README, demo workflow instructions, sample data, and journal evidence are included |
| Final demo | Team can demonstrate the full workflow during the final presentation |

## Supporting Project Files

| File | Purpose |
|---|---|
| [`PROJECT_PLAN.md`](PROJECT_PLAN.md) | Full project plan with weekly, task ownership, testing plan, and deliverables |
| [`MILESTONE_TODOS.md`](MILESTONE_TODOS.md) | Detailed milestone and weekly task tracked with checkmarking. |
| [`SHARED_DELIVERABLES_CHECKLIST.md`](SHARED_DELIVERABLES_CHECKLIST.md) | Shared checklist for assignment and project deliverables |
| [`MEETING_LOG.md`](MEETING_LOG.md) | Weekly meeting minutes, attendance, assigned tasks, and contribution evidence |
| [`AREAS_TO_IMPROVE.md`](AREAS_TO_IMPROVE.md) | Improvement chart showing needed work, owners, priority, and evidence |
| [`SAMPLE_INCIDENTS.md`](SAMPLE_INCIDENTS.md) | Readable sample incident scenarios for GitHub review and screenshots |
| [`DEMO_WORKFLOW_INSTRUCTIONS.md`](DEMO_WORKFLOW_INSTRUCTIONS.md) | Step-by-step instructions for demonstrating the prototype |
| [`USER_GUIDE.md`](USER_GUIDE.md) | Final user guide with setup, usage, review, export, screenshot, and troubleshooting instructions |
| [`WEEK7_MEETING_AGENDA.md`](WEEK7_MEETING_AGENDA.md) | Week 7 meeting agenda with current status, discussion topics, blockers, and owner assignments |
| [`WEEK7_WEEKLY_JOURNAL_DRAFT.md`](WEEK7_WEEKLY_JOURNAL_DRAFT.md) | Week 7 journal draft with progress notes, blockers, contributions, and signature page |
| [`FORM_FIELD_REVIEW.md`](FORM_FIELD_REVIEW.md) | Review of required form fields for the MVP workflow |
