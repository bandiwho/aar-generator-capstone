# Team 1 Capstone Project Plan

## Project Details

| Field | Details |
| --- | --- |
| Course | CSC 482 Capstone Project II |
| Team | Capstone Project Team 1 |
| Project Name | Security Incident Postmortem: Automated After-Action Report (AAR) Generator |
| Team Members | Brittany, Garrett, Mike |
| Session | Summer 2026 |
| Final Presentation | July 27-28, 2026 |

## Project Overview

Our team is building a Security Incident Postmortem: Automated After-Action Report (AAR) Generator. The application is designed to help organizations create a professional after-action report after a cybersecurity incident.

The user enters incident details such as timelines, log snippets, affected systems, known impact, remediation steps, and lessons learned. The prototype organizes the information and generates a structured report draft that can be reviewed, edited, and used for technical or executive audiences.

## Project Goal

The goal of this project is to create a usable prototype that accepts pasted or manually entered incident data and produces a professional after-action report draft. The generated report should include an executive summary, incident overview, timeline, impact analysis, technical findings, root-cause analysis, 5 Whys analysis, response actions, lessons learned, recommendations, and conclusion.

## Problem Statement

After a cybersecurity incident, organizations often need to document what happened, why it happened, how it was handled, and what should be improved. Writing this report manually can be time-consuming and inconsistent, especially when incident details are scattered across notes, logs, timelines, and response updates.

This project addresses that problem by providing a guided tool that helps turn raw incident information into a structured after-action report draft.

## Main Objectives

- [ ] Build a web interface for entering or pasting incident details.
- [ ] Allow users to include timelines, log snippets, affected systems, known impact, and remediation steps.
- [ ] Create a backend workflow that organizes the input and prepares it for report generation.
- [ ] Use structured prompting to generate consistent report sections.
- [ ] Include a 5 Whys root-cause analysis section.
- [ ] Support both technical and executive reporting styles.
- [ ] Allow basic review, revision, or regeneration of report content.
- [ ] Use realistic sample incidents to test the prototype.
- [ ] Prepare documentation, screenshots, and a final demo.

## Project Scope

| In Scope | Out of Scope |
| --- | --- |
| Incident input form | Live SIEM integration |
| Pasted-text workflow | Real-time monitoring |
| Timeline and log entry | Automatic production log collection |
| Backend API | Full incident response automation |
| Prompt templates | Enterprise authentication |
| Structured AAR draft output | Long-term report database |
| Technical and executive report styles | Full compliance mapping unless time allows |
| 5 Whys analysis | Production deployment security hardening |
| Basic review and revision workflow |  |
| Final demo scenario |  |

## Recommended Technology Stack

| Area | Technology | Purpose |
| --- | --- | --- |
| Frontend | HTML, CSS, JavaScript, or React | User interface and demo workflow |
| Backend | Python with Flask or FastAPI | API route and report-generation workflow |
| LLM Support | OpenAI API or approved LLM service | Generate structured report drafts |
| Data Format | JSON | Store sample incidents and structured input/output |
| Tools | GitHub, VS Code, Python, Node.js | Development, collaboration, and version control |

## System Architecture

1. The user opens the web application.
2. The user enters incident details into the form.
3. The frontend sends the incident data to the backend.
4. The backend organizes the data into a structured format.
5. The report-generation workflow creates the AAR draft.
6. The frontend displays the generated report for review.

## Core Features and Build Requirements

| Component | Purpose | Output | Success Measurement |
| --- | --- | --- | --- |
| Incident input area | Collect incident details | User-entered incident data | User can enter timeline, logs, impact, and remediation details |
| Input guidance template | Help users know what to enter | Clear form labels and sample prompts | User understands what information is needed |
| Data organization logic | Prepare information for report generation | Structured incident data | Input is organized before report creation |
| Prompt templates | Guide the report-generation process | Consistent report sections | Required report sections appear consistently |
| Few-shot examples | Improve report quality | Better structured report drafts | Output follows expected AAR style |
| Structured output format | Keep report readable | Report with clear headings | Report is easy to review and edit |
| Audience style selector | Support different audiences | Technical or executive report style | User can generate both styles |
| Feedback and revision input | Allow improvement of output | Revised report section or draft | User can request changes |
| Report output display | Show generated report | Visible report draft | Report appears clearly in the interface |
| Testing dataset | Support demo and evaluation | Sample incident records | Team can test multiple scenarios |
| Evaluation rubric | Judge report quality | Review checklist | Team can measure completeness and clarity |

## Team Roles and Responsibilities

| Team Member | Primary Role | Responsibilities |
| --- | --- | --- |
| Brittany | Project Leader, Documentation Lead, Quality Reviewer | Coordinates communication, tracks deadlines, organizes documentation, reviews clarity, supports project planning, and helps prepare the final presentation and demo flow. |
| Garrett | Backend and Report-Generation Lead | Builds backend logic, organizes structured data, supports prompt and report-generation workflow, handles JSON input/output, and tests report quality. |
| Mike | Frontend and Demo Workflow Lead | Supports the user interface, demo workflow, report display, frontend planning, usability checks, and presentation-ready screenshots. |

## MVP Requirements

The minimum viable product should include:

- [ ] A web form or pasted-input area for incident details.
- [ ] A button or workflow to generate a report draft.
- [ ] A structured AAR output with clear sections.
- [ ] Technical and executive audience options.
- [ ] A 5 Whys root-cause analysis section.
- [ ] Basic revision or regeneration support.
- [ ] At least one realistic sample incident for testing and demo use.

## Stretch Goals

- [ ] PDF export.
- [ ] DOCX export.
- [ ] Saved report history.
- [ ] Multiple incident templates.
- [ ] Severity scoring.
- [ ] MITRE ATT&CK mapping.
- [ ] NIST or ISO 27001 mapping.
- [ ] Dashboard-style summary page.

## Project Timeline

| Week | Date Range | Primary Focus | Team Outputs |
| --- | --- | --- | --- |
| Week 1 | June 1-7 | Course setup, project selection, and team formation | Team formed and project topic selected |
| Week 2 | June 8-14 | Tools, repository, project plan, and MVP planning | GitHub repository, signed plan, timeline, and schedule |
| Week 3 | June 15-21 | Requirements, scope, report design, frontend planning | User needs summary, AAR template, wireframe, sample incident data, and basic frontend page |
| Week 4 | June 22-28 | Prompt engineering, output structure, backend API, frontend connection | Prompt templates, schema, backend route, frontend connection, and first generated or mock report draft |
| Week 5 | June 29-July 5 | Prototype input, report generation, reporting styles, and 5 Whys | Input parser, report pipeline, style selector, and improved output |
| Week 6 | July 6-12 | Structured reports, feedback, validation, errors, and bug fixes | Revision workflow, feedback checklist, validation, loading states, and multiple tested reports |
| Week 7 | July 13-19 | Testing, polish, documentation, screenshots, and presentation draft | User guide, evaluation rubric, test results, demo script, screenshots, and presentation draft |
| Week 8 | July 20-28 | Final build, testing, report, presentation, and demo | Final app, final report, slides, and completed demo |

## Completed So Far

- [x] GitHub repository created for the team project.
- [x] Updated prototype folder organized.
- [x] README polished to better match the instructor's expected format.
- [x] Project description, team member descriptions, timeline, milestones, and tasks added to the README.
- [x] Signed project plan converted into this Markdown project plan.
- [x] Checkboxes added for weekly tasks, MVP requirements, testing, deliverables, and completion criteria.
- [x] Shared deliverables checklist added.
- [x] Demo workflow instructions added.
- [x] Form field review completed.
- [x] Realistic sample incidents added for testing and demo use.
- [x] Sample incidents page created in Markdown for easier GitHub viewing.
- [x] Backend schema work added to define incident input and report output structure.

## Weekly Task Checklist

### Week 3: June 15-21

- [x] Brittany: Finalize user needs, documentation structure, and project requirements.
- [x] Brittany: Review sample incident data and confirm it supports the demo workflow.
- [x] Garrett: Add backend schemas and define report-generation data structures.
- [x] Garrett: Outline backend build tasks for report-generation logic.
- [x] Mike: Plan frontend layout and demo workflow.
- [x] Mike: Identify form fields needed for the prototype.

### Week 4: June 22-28

- [ ] Brittany: Review executive-audience wording and report clarity.
- [ ] Brittany: Keep README, project plan, and weekly documentation updated.
- [ ] Garrett: Build or improve the backend route for report generation.
- [ ] Garrett: Connect structured incident data to the report-generation workflow.
- [ ] Mike: Build or refine the input form and report display page.
- [ ] Mike: Connect frontend fields to the backend workflow.

### Week 5: June 29-July 5

- [ ] Brittany: Test the pasted incident input workflow using sample incidents.
- [ ] Brittany: Record screenshots and notes for the weekly journal.
- [ ] Garrett: Improve report-generation pipeline and output formatting.
- [ ] Garrett: Add or refine the 5 Whys section.
- [ ] Mike: Add technical and executive style selection to the interface.
- [ ] Mike: Improve page readability and demo flow.

### Week 6: July 6-12

- [ ] Brittany: Create feedback review criteria for generated reports.
- [ ] Brittany: Review report quality against the project plan.
- [ ] Garrett: Add feedback-based revision or regeneration support.
- [ ] Garrett: Improve backend error handling.
- [ ] Mike: Add validation, loading states, and user-facing error messages.
- [ ] Mike: Test the full workflow with multiple sample incidents.

### Week 7: July 13-19

- [ ] Brittany: Write user guide, testing notes, and quality review.
- [ ] Brittany: Organize screenshots for the final presentation.
- [ ] Garrett: Improve backend reliability and formatting.
- [ ] Garrett: Support final testing and bug fixes.
- [ ] Mike: Polish the interface and report display.
- [ ] Mike: Prepare demo screenshots and display checks.

### Week 8: July 20-28

- [ ] Brittany: Finalize documentation, final report, and presentation slides.
- [ ] Brittany: Coordinate final demo flow and team speaking order.
- [ ] Garrett: Prepare demo-ready backend and report-generation workflow.
- [ ] Garrett: Confirm technical and executive report outputs work.
- [ ] Mike: Prepare final frontend demo flow.
- [ ] Mike: Confirm the prototype is ready for presentation.

## Milestone Assignments

| Milestone | Brittany | Garrett | Mike | Measurement |
| --- | --- | --- | --- | --- |
| Requirements, Scope, and Report Design | Define user needs, reporting goals, and user stories | Define system scope and workflow | Support AAR structure and frontend wireframe planning | Input, LLM processing, report generation, feedback, and final output are clearly described |
| Prompt Engineering and Output Structure | Create executive-audience prompt requirements and review clarity | Create technical prompt template and report-generation logic | Define structured output sections | Required report sections appear consistently |
| Prototype Input and Report Generation | Design pasted incident input workflow and review sample data | Build report-generation pipeline | Build input form and report display page | Prototype creates a complete draft report from pasted incident data |
| Structured Reports, 5 Whys, and Feedback | Define feedback review criteria | Add style selection and feedback-based regeneration | Add selector controls, validation, and user-facing error states | Prototype can generate technical and executive drafts and support revisions |
| Testing, Polish, and Documentation | Write user guide, testing notes, and quality review | Improve backend reliability and formatting | Polish interface, output, and usability | Prototype handles incomplete or messy input without crashing and improves report quality |
| Final Demo and Presentation | Prepare slides for problem, users, value, and final documentation | Prepare live demo workflow and demo-ready backend | Prepare frontend demo flow, screenshots, and display checks | Demo generates both reporting styles |
| Final Presentation | Present problem, user need, input workflow, and project value | Demonstrate report generation and audience modes | Present results, evaluation, limitations, and future improvements | Presentation covers problem, solution, workflow, architecture, technologies, demo, results, and future work |

## Testing and Evaluation Plan

### Functional Testing

- [ ] Confirm the application opens successfully.
- [ ] Confirm the incident form accepts user input.
- [ ] Confirm sample incident data can be entered or loaded.
- [ ] Confirm the report draft displays after generation.
- [ ] Confirm technical and executive styles produce different report language.
- [ ] Confirm required report sections are included.
- [ ] Confirm missing or incomplete fields do not crash the prototype.

### Prompt and Scenario Testing

The prototype should be tested with realistic cybersecurity incident scenarios, including:

- [ ] Unauthorized VPN login attempt.
- [ ] Phishing incident.
- [ ] Malware infection.
- [ ] Ransomware incident.
- [ ] Accidental data exposure.

### Usability Testing

- [ ] Confirm the workflow is understandable for a new user.
- [ ] Confirm the form labels are clear.
- [ ] Confirm generated output is readable.
- [ ] Confirm the demo workflow can be completed smoothly.

### Quality Measurements

| Area | Measurement |
| --- | --- |
| Completeness | Report includes required AAR sections |
| Clarity | Report is understandable and professionally written |
| Accuracy | Report reflects the incident details entered by the user |
| Structure | Output follows a logical after-action report format |
| Audience Fit | Technical and executive outputs use appropriate language |
| Reliability | Prototype handles sample incidents without crashing |

## Risks and Solutions

| Risk | Impact | Solution |
| --- | --- | --- |
| LLM output may be inconsistent | Report quality may vary | Use structured prompts, templates, and review criteria |
| Team members may have uneven availability | Work may fall behind schedule | Use weekly task tracking and assign clear owners |
| API or environment setup may fail | Demo may be delayed | Keep a mock report-generation fallback for demonstration |
| Scope may become too large | MVP may not be completed | Focus on core report generation first |
| Documentation may become scattered | Final submission may be harder to organize | Keep key files in the GitHub repository |

## Documentation and Final Deliverables

### Recommended Project Files

- [x] `README.md`
- [x] `PROJECT_PLAN.md`
- [x] `MILESTONE_TODOS.md`
- [x] `SHARED_DELIVERABLES_CHECKLIST.md`
- [x] `SAMPLE_INCIDENTS.md`
- [x] `DEMO_WORKFLOW_INSTRUCTIONS.md`
- [x] `FORM_FIELD_REVIEW.md`
- [ ] Final report or presentation files as required by the course

### Final Deliverables

- [ ] Working prototype.
- [x] GitHub repository with source code and documentation.
- [x] README with team project description, team member descriptions, milestones, and tasks.
- [x] Sample incident data.
- [x] Demo workflow instructions.
- [ ] Testing notes and screenshots.
- [ ] Final presentation and demo.

## Demo Plan

Recommended demo scenario: Unauthorized VPN Login Attempt.

1. Open the application.
2. Enter the sample incident details.
3. Select the audience style.
4. Generate the after-action report draft.
5. Review the summary, timeline, root-cause analysis, 5 Whys, lessons learned, and recommendations.
6. Explain how the report could be edited or regenerated.
7. Show how the prototype supports the project goal.

## Completion Criteria

The project is considered complete when:

- [ ] The prototype accepts incident details.
- [ ] The prototype generates a structured AAR draft.
- [ ] The report includes the required sections.
- [ ] The user can choose technical or executive style.
- [ ] Sample incidents are available for testing.
- [ ] The team can demonstrate the workflow clearly.
- [ ] Documentation is organized in the repository.
- [ ] The final presentation explains the problem, solution, architecture, demo, results, and future improvements.

## Team Organization Plan

- [ ] Use GitHub to store shared source code and documentation.
- [ ] Use Markdown files to track milestones, weekly tasks, sample incidents, and demo instructions.
- [ ] Keep README focused on the public project overview.
- [ ] Keep PROJECT_PLAN focused on the signed team plan.
- [ ] Keep weekly journal entries aligned with the project timeline and schedule.
- [ ] Use screenshots as evidence for completed prototype testing.
