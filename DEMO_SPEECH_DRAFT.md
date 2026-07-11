# Demo Speech Draft

Project: Security Incident Postmortem: Automated After-Action Report Generator  
Team: Brittany, Garrett, Mike  
Course: CSC 482 Capstone Project II  
Week: Week 7 demo preparation

## Speaking Goal

Explain the project clearly, show the working prototype, and prove that the team can generate a useful after-action report from realistic security incident details.

## Brittany Opening

Good afternoon. We are Team 1, and our project is the Security Incident Postmortem Automated After-Action Report Generator. Our team members are Brittany, Garrett, and Mike.

The problem we are solving is that after a cybersecurity incident, teams need to write a clear after-action report, but that process can be slow and hard to organize. Important details can be spread across timelines, log snippets, impact notes, and remediation steps. Our tool helps turn those details into a structured report draft.

The goal is not to replace human review. The goal is to give security teams a stronger starting point. The generated report can help organize the incident summary, timeline, evidence observations, root-cause analysis, remediation steps, recommendations, and lessons learned.

## Brittany Project Overview

Our prototype is a lightweight web application. The user enters incident information into a form, chooses the report audience, and generates an after-action report draft. The application supports both technical and executive report styles.

The technical style is meant for IT or security teams that need evidence, logs, root cause, and remediation detail. The executive style is meant for leadership, so it focuses more on business impact, risk, response actions, and recommendations.

For our advanced component, we added audience-specific reporting and a 5 Whys root-cause analysis section. This helps the report explain not only what happened, but why the incident happened and what should be improved.

## Handoff To Mike

Mike will now walk through the frontend and show how a user enters incident details into the prototype.

## Mike Frontend Walkthrough

This is the main AAR Generator form. The form asks for the incident title, incident date, audience style, summary, timeline, log snippets, remediation steps, known impact, and open questions.

For the demo, we are using a realistic sample incident so the report has enough detail to work with. The sample incident helps us test the same workflow consistently and gives us clean screenshot evidence for the final report and presentation.

I will choose the report audience, review the form fields, and generate the report draft.

## Handoff To Garrett

Garrett will now explain what happens behind the scenes when the report is generated.

## Garrett Backend Explanation

The backend receives the incident details from the form and organizes them into a structured report request. The workflow uses defined input and output fields so the generated report stays consistent.

The prompt asks for a professional after-action report with sections such as summary, timeline, evidence observations, impact, 5 Whys, root cause, remediation, recommendations, and lessons learned.

The application can use the OpenAI API when it is configured. We also kept mock fallback behavior available so the demo can still produce a report if the API is unavailable. That makes the project more reliable for testing and presentation.

## Brittany Testing And Documentation

For testing, we used multiple realistic sample incidents, including phishing, ransomware, exposed cloud storage, malware, and SQL injection scenarios. We checked whether the generated reports included the required sections, matched the selected audience, used the incident details accurately, and gave useful recommendations.

During Week 6, we focused on reliability. We tested validation, error handling, fallback behavior, report formatting, copy/download behavior, and screenshot evidence. The Week 6 journal has been turned in, so Week 7 is focused on documentation polish, demo practice, presentation notes, and backup materials.

## Demo Output Explanation

The generated report gives the team a draft that can be reviewed and improved. The strongest sections for our project are the structured timeline, evidence observations, 5 Whys analysis, remediation steps, recommendations, and lessons learned.

This output would help an organization start a post-incident review faster because it organizes the most important information into a professional format.

## Lessons Learned

One lesson we learned is that report quality depends heavily on the quality of the incident details entered by the user. If the timeline, evidence, or impact details are vague, the report is less useful.

Another lesson is that formatting matters. Even when the report content is strong, the output still needs to be readable in the browser, copied text, downloaded files, screenshots, and final documentation.

We also learned the importance of having a backup plan. Since our project can depend on an API connection, mock fallback behavior and saved screenshots are important for a smooth final demo.

## Closing

In summary, our AAR Generator helps turn security incident details into a structured after-action report draft. It supports technical and executive audiences, includes 5 Whys root-cause analysis, and gives teams a stronger starting point for post-incident documentation.

Our next step is to finish the final presentation materials, practice the full demo, organize backup screenshots, and prepare the final report for submission.

Thank you. We are ready for questions.

## Practice Notes

- Brittany should open and close the presentation.
- Mike should control the live frontend demo unless the team decides otherwise.
- Garrett should explain backend/report generation in simple terms.
- Keep the live demo focused on one strong incident.
- Mention that the tool creates a draft and still requires human review.
- Do not show the API key, terminal secrets, or private configuration.
- Keep backup screenshots and a backup generated report ready.
