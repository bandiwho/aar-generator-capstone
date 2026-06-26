# Form Field Review

Reviewer: Brittany
Date: June 16, 2026
Project: Security Incident AAR Generator

## Decision

The current form fields are enough for the MVP.

The prototype can generate a useful after-action report draft because it collects the main information needed for the required report sections.

## Current Form Fields

- Incident title
- Incident type
- Incident date
- Audience style: technical or executive
- Detection source
- Affected assets
- Incident summary
- Timeline
- Log snippets
- Remediation steps
- Known impact
- Lessons learned
- Open questions

## Required Fields

These fields should stay required:

- Incident title
- Incident date
- Audience style
- Incident summary
- Timeline
- Remediation steps

## Optional Fields

These fields can stay optional because the user may not know the answers at the beginning of an incident review:

- Incident type
- Detection source
- Affected assets
- Log snippets
- Known impact
- Lessons learned
- Open questions

## Missing Fields Decision

Incident type was added as an optional field because it helps classify the scenario before report generation. It is useful for testing and screenshots, but it does not need to be required because the incident title and summary can still describe the situation.

The current fields support these AAR sections:

- Executive summary
- Incident overview
- Timeline of events
- Impact assessment
- Evidence and log observations
- 5 Whys root-cause analysis
- Technical root cause
- Remediation completed
- Recommendations
- Open questions
- Lessons learned

## Optional Future Improvements

These fields could be added later, but they are not required for the MVP:

- Incident severity
- Detection source
- Affected business unit
- Incident owner
- Recommendation owner
- Due date for follow-up actions
- Final approval status

## Notes for Weekly Journal

Brittany reviewed the prototype form fields and confirmed that the MVP has enough required inputs to generate an after-action report draft. Optional fields can be added later after the team finishes the core report-generation workflow.
