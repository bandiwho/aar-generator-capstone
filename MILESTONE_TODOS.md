# Prototype Milestone TODOs

Use this file as the working checklist for the prototype. During each team meeting, update the status of each task.

Status options:

- `[ ]` Not started
- `[~]` In progress
- `[x]` Done

## Week 1: Project Setup and Topic Confirmation

Goal: Confirm the project direction and make sure the team understands the problem.

- [x] Brittany: Confirm the project title and summary.
- [x] Brittany: Create or update project notes in `PROJECT_PLAN.md`.
- [x] Brittany: Keep a list of team decisions from the first meeting.
- [x] Garrett: Confirm technical setup needs for backend and LLM integration.
- [x] Mike: Confirm technical setup needs for frontend development.
- [x] Team: Agree on the minimum version of the prototype.

Deliverable:

- [x] Team: Project topic, team roles, and MVP are confirmed.

## Week 2: Development Environment and Prototype Structure

Goal: Make sure everyone can open, edit, and run the starter prototype.

- [x] Brittany: Verify that project files are organized and easy to understand.
- [x] Brittany: Create a basic team task tracking system.
- [x] Garrett: Install Python and confirm the backend starter file can run.
- [x] Garrett: Review `prototype/backend/app.py` and identify backend changes needed.
- [x] Mike: Open `prototype/frontend/index.html` in a browser.
- [x] Mike: Review frontend files and identify UI changes needed.
- [x] Team: Confirm Git, Python, Node.js, and VS Code are installed.

Deliverable:

- [x] Team: Everyone can access the prototype and understands their assigned files.

## Week 3: Wireframe, Inputs, and Sample Incidents

Goal: Define what information the user must enter before generating a report.

- [x] Brittany: Create at least two realistic sample incidents.
- [x] Brittany: Review the form fields and decide if any required fields are missing.
- [x] Brittany: Write simple user instructions for the demo workflow.
- [x] Garrett: Define the JSON structure the backend expects.
- [x] Garrett: List the data needed for root-cause analysis and 5 Whys.
- [x] Mike: Create or update the wireframe for the form and report output.
- [x] Mike: Improve the frontend form layout if needed.

Deliverable:

- [x] Team: The form fields, sample data, and report sections are defined.

## Week 4: Backend Connection and First Generated Draft

Goal: Connect the frontend to the backend and generate a first report draft.

- [ ] Team: Code and test assigned project tasks as planned.
- [ ] Team: Push completed achievements to GitHub.
- [ ] Team: Update the README to reflect current progress.
- [ ] Garrett: Replace the frontend mock report with a backend API call.
- [ ] Garrett: Update `/generate-report` to accept incident data from the frontend.
- [ ] Garrett: Create an initial prompt template for report generation.
- [ ] Garrett: Return a structured draft report from the backend.
- [ ] Mike: Add a loading state while the report is generating.
- [ ] Mike: Add an error message if the backend fails.
- [ ] Brittany: Test the first generated report using a sample incident.
- [ ] Brittany: Write review notes on what is missing or unclear.
- [ ] Brittany: Collect demo screenshots as evidence of testing.
- [ ] Brittany: Prepare the team midterm report draft.
- [ ] Brittany: Add the GitHub repository URL as the report subtitle.
- [ ] Brittany: Document milestones achieved with brief descriptions.
- [ ] Brittany: Document subtasks completed with brief descriptions.
- [ ] Brittany: Add detailed testing descriptions with screenshots as evidence.
- [ ] Brittany: Add lessons learned.
- [ ] Brittany: Add each team member's contribution.
- [ ] Brittany: Explain whether the team progressed as planned.
- [ ] Brittany: Explain any plan adjustments if needed.
- [ ] Team: Review and sign the midterm report before submission.

Deliverable:

- [ ] Team: The frontend can send incident data to the backend and display a report draft.
- [ ] Team: The team midterm report is complete, signed by each member, exported as a PDF, and submitted.

## Week 5: Report Styles and Root-Cause Analysis

Goal: Make the generated report more useful and add audience-specific output.

- [ ] Garrett: Add technical report style generation.
- [ ] Garrett: Add executive report style generation.
- [ ] Garrett: Add 5 Whys root-cause analysis.
- [ ] Garrett: Add recommendations based on the incident details.
- [ ] Mike: Add clear style selection controls in the frontend.
- [ ] Mike: Improve report formatting in the output area.
- [ ] Brittany: Compare technical and executive reports for tone and clarity.
- [ ] Brittany: Review recommendations to make sure they are realistic.

Deliverable:

- [ ] Team: The app generates technical and executive reports with root-cause analysis.

## Week 6: Revision Feature, Validation, and Testing

Goal: Improve reliability and make the app easier to use.

- [ ] Garrett: Add a way to revise or regenerate report sections.
- [ ] Garrett: Improve backend error handling.
- [ ] Garrett: Add fallback mock generation if the LLM is unavailable.
- [ ] Mike: Add required-field validation to the form.
- [ ] Mike: Improve copy/export behavior for the generated report.
- [ ] Mike: Make the frontend easier to use on smaller screens.
- [ ] Brittany: Test the app with at least three incident scenarios.
- [ ] Brittany: Track bugs and unclear output in a testing notes file.

Deliverable:

- [ ] Team: The app handles errors, validates inputs, and works with multiple test incidents.

## Week 7: Polish, Documentation, and Demo Preparation

Goal: Prepare the project for final presentation.

- [ ] Brittany: Finalize project documentation.
- [ ] Brittany: Write the final demo script.
- [ ] Brittany: Prepare presentation slides.
- [ ] Brittany: Capture screenshots for the presentation.
- [ ] Garrett: Clean up backend code and comments.
- [ ] Garrett: Confirm report generation works with final demo data.
- [ ] Mike: Polish the homepage and report display.
- [ ] Mike: Confirm the topographical homepage image displays correctly.
- [ ] Team: Practice the demo from start to finish.

Deliverable:

- [ ] Team: The app, documentation, slides, and demo script are ready for final review.

## Week 8: Final Testing and Submission

Goal: Finish, test, present, and submit the project.

- [ ] Brittany: Run the final quality review.
- [ ] Brittany: Confirm grammar, formatting, and documentation quality.
- [ ] Brittany: Confirm the team can explain each project section.
- [ ] Garrett: Confirm backend and LLM generation are working.
- [ ] Garrett: Prepare a backup plan if the LLM service fails during the demo.
- [ ] Mike: Confirm the frontend works on the presentation machine.
- [ ] Mike: Confirm the final demo flow is smooth.
- [ ] Team: Complete final presentation practice.
- [ ] Team: Submit final files.

Deliverable:

- [ ] Team: Final application, report, slides, and demo are complete.

## Optional Stretch Goal TODOs

Only work on these after the MVP is complete.

- [ ] Garrett: Add PDF export.
- [ ] Garrett: Add DOCX export.
- [ ] Garrett: Add saved report history.
- [ ] Mike: Add a report template selection screen.
- [ ] Mike: Add a dashboard for previous reports.
- [ ] Brittany: Add more sample incidents.
- [ ] Brittany: Add a final user guide.
- [ ] Team: Add MITRE ATT&CK or NIST mapping if time allows.

## Meeting Routine

Use this routine during each team meeting:

1. Mark completed tasks with `[x]`.
2. Change active tasks to `[~]`.
3. Add blockers beside any delayed task.
4. Assign a clear owner to every new task.
5. End the meeting with each person naming their next task.

