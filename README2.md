# Security Incident AAR Generator Updated Prototype

Prototype for Team 1's CSC 482 Capstone Project II.

## Description of Team Project

The Security Incident Postmortem: Automated After-Action Report (AAR) Generator is a capstone project that helps teams create professional incident review reports after a cybersecurity incident.

Users enter incident details such as the timeline, log snippets, known impact, and remediation steps. The prototype generates a structured after-action report draft with sections for executive summary, timeline, impact, evidence, 5 Whys root-cause analysis, technical root cause, remediation, recommendations, open questions, and lessons learned.

The project supports two report styles:

- Technical audience: focuses on evidence, systems, control gaps, and remediation tasks.
- Executive audience: focuses on business impact, risk, accountability, and high-level recommendations.

## Description of Each Team Member

### Brittany

Brittany is the project leader, documentation lead, and quality reviewer. She keeps the project organized, tracks assignment requirements, reviews grammar and formatting, and makes sure the final deliverables match the class expectations.

### Garrett

Garrett is responsible for backend development, Python API work, and the report-generation workflow. He focuses on making sure the prototype can process incident details and generate structured after-action report sections.

### Mike

Mike is responsible for frontend development, the user interface, and the demo workflow. He focuses on making the prototype easy to use, readable, and ready for the final class demonstration.

## Milestones Complete and To Be Completed Each Week

| Week | Dates | Milestones Complete | Milestones To Be Completed |
|---|---|---|---|
| Week 1 | June 1 - June 7 | Team formed; project topic selected; VM setup started. | Confirm all setup notes are saved for documentation. |
| Week 2 | June 8 - June 14 | Project plan created; weekly schedule created; prototype structure started. | Finish GitHub setup and make sure all team members can access the repository. |
| Week 3 | June 15 - June 21 | `updated_prototype` created; shared checklist created; README updated for assignment requirements. | Create public GitHub repository, upload source code, add collaborators, and submit the repository URL. |
| Week 4 | June 22 - June 28 | Basic report structure and 5 Whys section planned. | Improve report quality, validate required sections, and test with more sample incidents. |
| Week 5 | June 29 - July 5 | Technical and executive report style options planned. | Improve report style selection, user feedback, and handling of incomplete input. |
| Week 6 | July 6 - July 12 | Testing and documentation plan started. | Complete testing evidence, screenshots, setup instructions, and cleanup. |
| Week 7 | July 13 - July 19 | Demo and presentation responsibilities assigned. | Draft final presentation, write demo script, and practice the full workflow. |
| Week 8 | July 20 - July 28 | Final submission plan created. | Complete final documentation, presentation, demo practice, and final submission. |

## Tasks Complete and To Be Completed by Each Team Member

### Brittany

Completed:

- [x] Organized the project folder and planning documents.
- [x] Created the weekly team plan checklist.
- [x] Created the shared deliverables checklist.
- [x] Reviewed assignment requirements for the GitHub repository and weekly journal.
- [x] Updated README content for project description, team member descriptions, milestones, and tasks.

To be completed:

- [ ] Create or confirm the public GitHub repository.
- [ ] Add the GitHub repository URL to the weekly journal and Canvas team homepage.
- [ ] Review grammar and formatting before submission.
- [ ] Collect screenshots and evidence for the weekly journal PDF.
- [ ] Lead the final submission check.

### Garrett

Completed:

- [ ] Reviewed backend/report-generation responsibilities.
- [ ] Helped define backend workflow needs for the AAR generator.
- [ ] Backend/report service files are included in `updated_prototype`.

To be completed:

- [ ] Review backend setup instructions.
- [ ] Test report generation with sample incident data.
- [ ] Improve prompt/report-generation logic.
- [ ] Help verify technical and executive report outputs.
- [ ] Add backend progress notes for the weekly journal.

### Mike

Completed:

- [x] Provided prototype work that was combined into `updated_prototype`.
- [x] Frontend interface files are included in `updated_prototype`.
- [x] Demo workflow responsibilities are identified.

To be completed:

- [ ] Review the browser form and report output display.
- [ ] Improve the user interface if needed.
- [ ] Confirm the demo flow works from start to finish.
- [ ] Capture frontend screenshots for the weekly journal.
- [ ] Add frontend progress notes for the weekly journal.

## What This Prototype Does

- Provides a browser form for incident overview, timeline, log snippets, remediation, and audience style.
- Generates a structured AAR draft with executive summary, timeline, impact, 5 Whys analysis, root cause, lessons learned, and follow-up actions.
- Supports two audience styles: `technical` and `executive`.
- Runs in mock mode without an API key so the team can test the application flow before connecting OpenAI.
- Uses the OpenAI API when `OPENAI_API_KEY` is configured.
- Includes milestone TODOs and project checklist files for class tracking.

## Prerequisites

Install these before running the prototype:

1. Python 3.11 or newer
2. Git, recommended for team collaboration
3. A code editor, such as VS Code
4. OpenAI API key, stored in `OPENAI_API_KEY`
5. Internet access on the VM when installing Python packages and when using the OpenAI API

No model training is required. This prototype uses prompt templates and API calls.

## Windows Server 2025 Setup

Open PowerShell in this folder:

```text
updated_prototype
```

Then run:

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.4-mini
MOCK_LLM=false
```

If PowerShell blocks virtual environment activation, run this once as your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Ubuntu 24.04 LTS Setup

Open a terminal in this folder:

```text
updated_prototype
```

Then run:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.4-mini
MOCK_LLM=false
```

## Run the Prototype

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
.\run_windows.ps1
```

Ubuntu:

```bash
source .venv/bin/activate
./run_ubuntu.sh
```

Open:

```text
http://localhost:7860
```

Health check:

```text
http://localhost:7860/health
```

API docs:

```text
http://localhost:7860/docs
```

## Run Without an OpenAI Key

The `.env.example` file defaults to mock mode:

```text
MOCK_LLM=true
```

Mock mode returns a deterministic sample report and is useful for demos, UI work, testing, and development when the API key is not available.

## Semester Milestone TODOs

The prototype includes TODO markers for:

- Week 2: finalize input fields and project setup
- Week 3: improve prompt templates and few-shot examples
- Week 4: implement structured output validation
- Week 5: add iterative user feedback and report revision workflow
- Week 6: add export options such as Markdown, DOCX, or PDF
- Week 7: add evaluation examples and demo incident scenarios
- Week 8: polish deployment, presentation flow, and final demo

Search the project for `TODO:` to find the work items.

## Deployment Notes

For a class demo, running Uvicorn directly is acceptable. For a VM-hosted deployment:

- Bind to `0.0.0.0` so other machines can reach the service.
- Open TCP port `7860` in the VM firewall or cloud security group.
- Keep `.env` off public repositories because it contains secrets.
- Set `MOCK_LLM=false` only after `OPENAI_API_KEY` is configured.
- Use a process manager for long-running VM use:
  - Windows Server: Task Scheduler or NSSM
  - Ubuntu: `systemd`

## Project Structure

```text
aar_generator/
  main.py          FastAPI routes and web form handling
  config.py        Environment settings
  schemas.py       Request and response models
  prompts.py       Prompt templates and milestone TODOs
  llm_client.py    OpenAI API and mock client
  report_service.py Report orchestration
  templates/       Browser UI
  static/          CSS
tests/
  test_report_service.py
data/
  sample_incident.json
MILESTONE_TODOS.md
DEPLOYMENT_AND_SUBMISSION_GUIDE.md
```

## Collaboration Exercise for README

Use this file for GitHub practice:

- [ ] Brittany adds the final milestone timeline and schedule.
- [ ] Garrett adds a short backend responsibility description.
- [ ] Mike adds a short frontend responsibility description.
- [ ] Each team member creates a branch, commits their README change, and opens a pull request.
- [ ] Brittany reviews and merges the pull requests after checking grammar and formatting.
