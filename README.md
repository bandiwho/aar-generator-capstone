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

- Incident detail entry through a clear frontend form.
- Support for timelines, log snippets, impact notes, and remediation steps.
- LLM-supported report generation workflow.
- 5 Whys root-cause analysis.
- Technical and executive reporting styles.
- Realistic sample incident data for testing.
- Demo workflow documentation for presentation practice.
- GitHub repository for shared source code and documentation.

## Current Project Status

- [x] GitHub repository created for the team project.
- [x] Updated prototype folder organized.
- [x] README polished to match the instructor's expected format.
- [x] Project description, team member descriptions, timeline, milestones, and tasks added to the README.
- [x] Project plan converted into Markdown for GitHub viewing.
- [x] Checkboxes added for weekly tasks, MVP requirements, testing, deliverables, and completion criteria.
- [x] Shared deliverables checklist added.
- [x] Demo workflow instructions added.
- [x] Form field review completed.
- [x] Realistic sample incidents added for testing and demo use.
- [x] Sample incidents page created in Markdown for easier GitHub viewing.
- [x] Backend schema work added to define incident input and report output structure.

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
| [ ] | June 22 - June 28 | Milestone 2 | Backend data structure, report-generation workflow, and frontend form refinement |
| [ ] | June 29 - July 5 | Milestone 3 | Technical and executive report styles, improved 5 Whys analysis, and output formatting |
| [ ] | July 6 - July 12 | Milestone 4 | Testing, error handling, validation, and sample incident review |
| [ ] | July 13 - July 19 | Milestone 5 | Documentation, screenshots, presentation draft, and demo script |
| [ ] | July 20 - July 24 | Milestone 6 | Final polish, final testing, submission package, and presentation practice |
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
| [ ] | Garrett | Define JSON structure for incident input | Request/response structure for report generation | Data fields support timeline, logs, impact, remediation, and open questions |
| [ ] | Garrett | Build report-generation workflow | Backend service logic and prompt workflow | Prototype can produce structured report sections |
| [ ] | Mike | Improve frontend form layout | Updated form layout and clearer input sections | Users can enter incident details without confusion |
| [ ] | Mike | Improve report output display | Cleaner generated report output area | Generated report is readable during demo |
| [ ] | Brittany | Review output quality | Notes on missing, unclear, or weak report sections | Review notes are ready for Garrett and Mike |

### Milestone 3: Report Style and Root-Cause Analysis

Dates: June 29 - July 5, 2026  
Goal: Improve the generated report and support different reporting audiences.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Garrett | Add technical report style support | Technical report generation path | Output includes technical details and evidence references |
| [ ] | Garrett | Add executive report style support | Executive report generation path | Output summarizes impact, risk, and recommendations clearly |
| [ ] | Garrett | Improve 5 Whys analysis | Root-cause analysis section | 5 Whys section connects incident evidence to likely causes |
| [ ] | Mike | Add or improve style controls | Technical/executive selection in UI | User can choose report audience style |
| [ ] | Brittany | Compare report tone and clarity | Quality review notes | Technical and executive outputs match their audiences |

### Milestone 4: Testing and Validation

Dates: July 6 - July 12, 2026  
Goal: Test the prototype with multiple incidents and improve reliability.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Brittany | Test app with sample incidents | Testing notes and screenshots | At least three incident scenarios are tested |
| [ ] | Garrett | Improve backend error handling | Backend fallback and error handling logic | App handles incomplete or weak input without crashing |
| [ ] | Mike | Improve frontend validation | Required-field behavior and user-facing messages | Users understand what information is missing |
| [ ] | Team | Review test results | Bug list and improvement notes | Issues are documented and assigned |

### Milestone 5: Documentation and Demo Preparation

Dates: July 13 - July 19, 2026  
Goal: Prepare the project for final presentation and demonstration.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Brittany | Finalize project documentation | Final README, journal notes, and checklist updates | Documentation is clear and complete |
| [ ] | Brittany | Prepare presentation outline | Slide outline and speaker notes | Presentation covers problem, solution, prototype, and lessons learned |
| [ ] | Garrett | Prepare backend explanation | Backend workflow summary | Team can explain how report generation works |
| [ ] | Mike | Prepare demo flow | Demo script and frontend walkthrough | Demo can be completed smoothly |

### Milestone 6: Final Polish and Submission

Dates: July 20 - July 24, 2026  
Goal: Finish the prototype, documentation, screenshots, and final submission package.

| Done | Member | Task | Outputs Produced | Measurement |
|---|---|---|---|---|
| [ ] | Brittany | Run final quality review | Final grammar, formatting, and requirement check | Submission materials are clean and organized |
| [ ] | Garrett | Confirm backend/report generation | Final backend test notes | Report generation works with final demo data |
| [ ] | Mike | Confirm frontend/demo workflow | Final interface check and demo screenshots | Prototype is ready for presentation |
| [ ] | Team | Practice final demo | Full demo rehearsal | Team can present within the assigned time |

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
| [`SAMPLE_INCIDENTS.md`](SAMPLE_INCIDENTS.md) | Readable sample incident scenarios for GitHub review and screenshots |
| [`DEMO_WORKFLOW_INSTRUCTIONS.md`](DEMO_WORKFLOW_INSTRUCTIONS.md) | Step-by-step instructions for demonstrating the prototype |
| [`FORM_FIELD_REVIEW.md`](FORM_FIELD_REVIEW.md) | Review of required form fields for the MVP workflow |
