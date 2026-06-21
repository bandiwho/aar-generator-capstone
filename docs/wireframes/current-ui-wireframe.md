# Current UI Wireframe

This wireframe documents the current planned screen for the Security Incident AAR Generator prototype.

## Main Screen

```text
+--------------------------------------------------------------------------+
| CSC 482 Capstone Project II | Team 1                                     |
| Security Incident AAR Generator                                          |
| Paste incident details and generate a structured AAR draft.              |
| [Brittany role] [Garrett role] [Mike role]                               |
+------------------------------------+-------------------------------------+
| Incident Details                   | Report Draft                        |
|                                    |                                     |
| Incident Overview                  | Title                               |
| - Incident title                   | Audience | Model | Mock mode        |
| - Incident date                    |                                     |
| - Audience                         | [Executive Summary] [Timeline]      |
| - Incident summary                 | [5 Whys] [Recommendations]          |
|                                    |                                     |
| Evidence and Impact                | Generated Markdown report:          |
| - Detection source                 | - Executive Summary                 |
| - Affected assets                  | - Incident Overview                 |
| - Timeline                         | - Detection and Escalation          |
| - Log snippets                     | - Timeline of Events                |
| - Known impact                     | - Impact Assessment                 |
|                                    | - Evidence and Log Observations     |
| Response and Follow-Up             | - 5 Whys Root Cause Analysis        |
| - Remediation steps                | - Technical Root Cause              |
| - Lessons learned                  | - Process and Communication Gaps    |
| - Open questions                   | - Remediation Completed             |
|                                    | - Recommendations and Owners        |
| [Generate Report Draft]            | - Lessons Learned                   |
|                                    | - Open Questions                    |
+------------------------------------+-------------------------------------+
```

## User Flow

```text
Open app
  -> Review sample incident fields
  -> Replace sample details with real incident notes
  -> Select technical or executive audience
  -> Generate report draft
  -> Review output sections
  -> Copy or refine report content
```

## Form Sections

- Incident Overview: captures the incident title, date, audience, and summary.
- Evidence and Impact: captures detection source, affected assets, timeline, logs, and impact.
- Response and Follow-Up: captures remediation steps, lessons learned, and open questions.

## Report Output Sections

- Executive Summary
- Incident Overview
- Detection and Escalation
- Timeline of Events
- Impact Assessment
- Evidence and Log Observations
- 5 Whys Root Cause Analysis
- Technical Root Cause
- Process and Communication Gaps
- Remediation Completed
- Recommendations and Owners
- Lessons Learned
- Open Questions
