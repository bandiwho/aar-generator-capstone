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

- [x] Team: Code and test assigned project tasks as planned.
- [x] Team: Push completed achievements to GitHub.
- [x] Team: Update the README to reflect current progress.
- [x] Garrett: Replace the frontend mock report with a backend API call.
- [x] Garrett: Update `/generate-report` to accept incident data from the frontend.
- [x] Garrett: Create an initial prompt template for report generation.
- [x] Garrett: Return a structured draft report from the backend.
- [x] Garrett: Configure real LLM mode to use automatic model selection from the class API project.
- [x] Garrett: Keep mock fallback available if the OpenAI API is unavailable.
- [x] Mike: Add a loading state while the report is generating.
- [x] Mike: Add an error message if the backend fails.
- [x] Mike: Display the generated report and model/mock-mode metadata in the browser.
- [x] Brittany: Test the first generated report using a sample incident.
- [x] Brittany: Write review notes on what is missing or unclear.
- [x] Brittany: Collect demo screenshots as evidence of testing.
- [x] Brittany: Prepare the team midterm report draft.
- [x] Brittany: Add the GitHub repository URL as the report subtitle.
- [x] Brittany: Document milestones achieved with brief descriptions.
- [x] Brittany: Document subtasks completed with brief descriptions.
- [x] Brittany: Add detailed testing descriptions with screenshots as evidence.
- [x] Brittany: Add lessons learned.
- [x] Brittany: Add each team member's contribution.
- [x] Brittany: Explain whether the team progressed as planned.
- [x] Brittany: Explain any plan adjustments if needed.
- [x] Team: Review and sign the midterm report before submission.

Deliverable:

- [x] Team: The frontend can send incident data to the backend and display a report draft.
- [x] Team: The team midterm report is complete, signed by each member, exported as a PDF, and submitted.

## Week 5: Report Styles and Root-Cause Analysis

Goal: Make the generated report more useful, add audience-specific output, test the week's work, and document team contributions for the Week 5 journal.

- [~] Team: Code and test assigned project tasks as planned for Week 5.
- [ ] Team: Push completed achievements to GitHub.
- [x] Team: Update the README to reflect current Week 5 progress.
- [x] Team: Add a weekly meeting log for attendance, topics, assigned tasks, and completion status.
- [~] Team: Include meeting log information in the Week 5 journal.
- [~] Team: Collect testing screenshots without showing the OpenAI API key.
- [~] Garrett: Add technical report style generation.
- [~] Garrett: Add executive report style generation.
- [ ] Garrett: Add 5 Whys root-cause analysis.
- [ ] Garrett: Add recommendations based on the incident details.
- [~] Garrett: Confirm backend tests pass after Week 5 report-style changes.
- [X] Mike: Help capture frontend demo screenshots for the weekly journal.
- [x] Mike: Add clear style selection controls in the frontend.
- [x] Mike: Improve report formatting in the output area.
- [x] Mike: Preserve form values after report generation.
- [x] Mike: Change the incident date field to a date picker.
- [x] Mike: Add required-field hints and inline validation messages.
- [x] Mike: Add clearer loading feedback while reports generate.
- [x] Mike: Add sample incident autofill with rotating sample data.
- [x] Mike: Show which sample incident was loaded.
- [x] Mike: Render Markdown output as a cleaner formatted report preview.
- [x] Mike: Improve Evidence, Timeline, Remediation, and Open Questions formatting.
- [~] Brittany: Compare technical and executive reports for tone and clarity.
- [ ] Brittany: Review recommendations to make sure they are realistic.
- [x] Brittany: Update README, milestone todos, and shared deliverables checklist for the Week 5 assignment.
- [x] Brittany: Create `MEETING_LOG.md` to make Garrett and Mike's contributions visible.
- [ ] Brittany: Write the Week 5 journal sections for milestones, subtasks, testing evidence, lessons learned, contributions, and progress compared to plan.
- [ ] Brittany: Export the Week 5 journal as a PDF for Canvas submission.

Deliverable:

- [~] Team: The app generates technical and executive reports with root-cause analysis.
- [x] Team: GitHub shows current README, todos, deliverables, and meeting log updates.
- [~] Team: The Week 5 journal includes contribution evidence for Brittany, Garrett, and Mike.

## Week 6: Revision Feature, Validation, and Testing

Goal: Improve reliability and make the app easier to use.

- [ ] Team: Code and test assigned project tasks as planned for Week 6.
- [ ] Team: Push completed achievements to GitHub.
- [ ] Team: Update the README to reflect Week 6 progress.
- [ ] Team: Update the meeting log with attendance, topics, assigned tasks, and completion status.
- [ ] Team: Include meeting log information in the Week 6 journal.
- [ ] Team: Collect testing screenshots without showing the OpenAI API key.
- [ ] Garrett: Add a way to revise or regenerate report sections.
- [ ] Garrett: Improve backend error handling.
- [ ] Garrett: Add fallback mock generation if the LLM is unavailable.
- [ ] Mike: Add required-field validation to the form.
- [ ] Mike: Improve copy/export behavior for the generated report.
- [ ] Mike: Make the frontend easier to use on smaller screens.
- [ ] Brittany: Test the app with at least three incident scenarios.
- [ ] Brittany: Track bugs and unclear output in a testing notes file.
- [ ] Brittany: Write the Week 6 journal sections for milestones, subtasks, testing evidence, lessons learned, contributions, and progress compared to plan.
- [ ] Brittany: Export the Week 6 journal as a PDF for Canvas submission.

Deliverable:

- [ ] Team: The app handles errors, validates inputs, and works with multiple test incidents.
- [ ] Team: The Week 6 journal includes contribution evidence for Brittany, Garrett, and Mike.

## Week 7: Polish, Documentation, and Demo Preparation

Goal: Prepare the project for final presentation.

- [ ] Team: Code and test assigned project tasks as planned for Week 7.
- [ ] Team: Push completed achievements to GitHub.
- [ ] Team: Update the README to reflect Week 7 progress.
- [ ] Team: Update the meeting log with attendance, topics, assigned tasks, and completion status.
- [ ] Team: Include meeting log information in the Week 7 journal.
- [ ] Team: Collect demo screenshots without showing the OpenAI API key.
- [ ] Brittany: Finalize project documentation.
- [ ] Brittany: Write the final demo script.
- [ ] Brittany: Prepare presentation slides.
- [ ] Brittany: Capture screenshots for the presentation.
- [ ] Garrett: Clean up backend code and comments.
- [ ] Garrett: Confirm report generation works with final demo data.
- [ ] Mike: Polish the homepage and report display.
- [ ] Mike: Confirm the topographical homepage image displays correctly.
- [ ] Team: Practice the demo from start to finish.
- [ ] Brittany: Write the Week 7 journal sections for milestones, subtasks, testing evidence, lessons learned, contributions, and progress compared to plan.
- [ ] Brittany: Export the Week 7 journal as a PDF for Canvas submission.

Deliverable:

- [ ] Team: The app, documentation, slides, and demo script are ready for final review.
- [ ] Team: The Week 7 journal includes contribution evidence for Brittany, Garrett, and Mike.

## Week 8: Final Testing and Submission

Goal: Finish the final report, presentation slides, final presentation preparation, final testing, and submission package.

- [ ] Brittany: Run the final quality review.
- [ ] Brittany: Confirm grammar, formatting, and documentation quality.
- [ ] Brittany: Confirm the team can explain each project section.
- [ ] Brittany: Finalize the final report.
- [ ] Brittany: Confirm the final report includes milestones, testing evidence, lessons learned, team contributions, and meeting log evidence.
- [ ] Brittany: Finalize the presentation slides.
- [ ] Brittany: Confirm the slides include project problem, solution, prototype workflow, screenshots, testing, lessons learned, and team roles.
- [ ] Garrett: Confirm backend and LLM generation are working.
- [ ] Garrett: Prepare a backup plan if the LLM service fails during the demo.
- [ ] Garrett: Prepare the backend and LLM explanation for the final presentation.
- [ ] Mike: Confirm the frontend works on the presentation machine.
- [ ] Mike: Confirm the final demo flow is smooth.
- [ ] Mike: Prepare the frontend and demo workflow explanation for the final presentation.
- [ ] Team: Complete final presentation practice.
- [ ] Team: Prepare final presentation roles for July 27-28.
- [ ] Team: Submit final files.

Deliverable:

- [ ] Team: Final application, report, slides, and demo are complete.

## Final Presentation: July 27 - July 28

Goal: Present the completed AAR Generator and demonstrate the working prototype.

- [ ] Brittany: Present project purpose, documentation, final report, quality review, and team organization.
- [ ] Garrett: Present backend workflow, LLM integration, testing evidence, and fallback plan.
- [ ] Mike: Present frontend workflow, user input form, generated report display, and live demo flow.
- [ ] Team: Complete the live prototype demonstration.
- [ ] Team: Answer questions about project scope, testing, lessons learned, and future improvements.
- [ ] Team: Use backup screenshots or a backup generated report if the live demo has technical issues.

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

