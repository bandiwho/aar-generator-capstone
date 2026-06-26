# Sample Incidents for Testing and Demo

These sample incidents are used to test and demonstrate the Security Incident AAR Generator. They match the prototype form fields so the team can copy the information into the app, generate an after-action report, and compare the technical and executive report styles.

## How To Use These Samples

1. Open the prototype app.
2. Choose one sample incident.
3. Copy the incident title, date, audience, summary, timeline, log evidence, known impact, remediation, lessons learned, and open questions into the form.
4. Generate the report.
5. Save a screenshot of the completed form and the generated report output.
6. Review whether the report includes the executive summary, timeline, evidence observations, 5 Whys analysis, root cause, remediation, recommendations, lessons learned, and open questions.

## Form Field Checklist

Use this checklist before generating a report:

- Incident title is specific.
- Incident date is included.
- Audience is set to technical or executive.
- Detection source is listed.
- Affected assets are listed.
- Incident summary explains what happened.
- Timeline has clear time-based events.
- Log evidence includes realistic alerts, audit events, or system records.
- Known impact separates confirmed facts from unknowns.
- Remediation steps describe containment, recovery, and follow-up.
- Lessons learned explain what should improve.
- Open questions identify facts that still need confirmation.

## 1. Phishing Email Led to Microsoft 365 Account Compromise

**Incident type:** Phishing and account compromise  
**Detection source:** Employee report, Microsoft Defender phishing alert, and Azure AD sign-in review  
**Affected assets:** Microsoft 365, Outlook, SharePoint, employee account  
**Incident date:** 2026-06-16  
**Report audience:** Technical

### Incident Summary

An employee reported a suspicious email after entering credentials into a fake Microsoft 365 login page. Security review showed successful mailbox access from an unfamiliar IP address and several suspicious inbox rules.

### Timeline

- 8:10 AM - Employee received an email claiming their Microsoft 365 password would expire.
- 8:14 AM - Employee clicked the link and entered credentials into a fake login page.
- 8:26 AM - Successful Microsoft 365 login detected from an unfamiliar IP address.
- 8:31 AM - Suspicious inbox forwarding rule created.
- 8:50 AM - Employee reported the email to the help desk.
- 9:05 AM - Security team disabled the account and revoked active sessions.
- 9:25 AM - Password reset completed and MFA registration reviewed.
- 10:15 AM - Mailbox rules removed and message trace review started.

### Log Evidence

- AzureAD SignIn: user=brittany.employee result=success location=unfamiliar_ip
- Exchange Audit: New-InboxRule created forwarding external address
- Defender Alert: Phishing URL clicked by user
- Message Trace: Similar phishing email delivered to 14 users

### Known Impact

One employee mailbox was accessed. No confirmed data exfiltration has been identified at this stage, but mailbox contents and SharePoint access require review.

### Remediation Steps

- Disabled the affected account.
- Revoked active Microsoft 365 sessions.
- Reset the user password.
- Removed suspicious mailbox forwarding rules.
- Blocked the phishing URL and sender domain.
- Started a message trace to identify other affected users.
- Sent a warning notice to employees who received the same email.

### Lessons Learned

Phishing reporting worked, but MFA enforcement and inbox rule monitoring should be reviewed. Employees need continued phishing awareness training, and the security team should confirm whether suspicious mailbox rules are detected quickly.

### Open Questions

- Was MFA challenged or bypassed during the suspicious login?
- Did the attacker access or download SharePoint files?
- Did any other users enter credentials into the phishing page?

## 2. Ransomware Detected on Shared File Server

**Incident type:** Ransomware and file encryption  
**Detection source:** Help desk reports, endpoint protection alert, and file server activity logs  
**Affected assets:** Windows file server, shared department drive, endpoint workstation  
**Incident date:** 2026-06-17  
**Report audience:** Executive

### Incident Summary

Users reported that shared documents would not open and file extensions had changed. Endpoint protection alerted on ransomware behavior from one workstation connected to a shared department drive.

### Timeline

- 2:05 PM - Help desk received reports that shared files would not open.
- 2:11 PM - Endpoint protection generated a ransomware behavior alert.
- 2:16 PM - Security team identified one workstation modifying many files rapidly.
- 2:20 PM - Workstation was isolated from the network.
- 2:28 PM - File share access was temporarily disabled.
- 2:45 PM - Server snapshots and backups were checked.
- 3:30 PM - Affected file paths were documented.
- 4:15 PM - Restore plan was approved by IT leadership.

### Log Evidence

- EDR Alert: Mass file rename activity detected on WORKSTATION-22
- File Server Event: High volume write activity from WORKSTATION-22
- Windows Security Log: User account accessed shared drive before encryption activity
- Backup System: Last successful snapshot completed at 1:00 PM

### Known Impact

A shared department drive was partially encrypted. Initial review suggests the affected files can be restored from backup. No confirmed evidence of data theft has been identified at this stage.

### Remediation Steps

- Isolated the affected workstation.
- Disabled file share access temporarily.
- Preserved logs for review.
- Checked backup availability.
- Restored affected files from the last clean snapshot.
- Reset credentials for the affected user account.
- Scheduled malware scan and workstation rebuild.

### Lessons Learned

Rapid isolation helped limit ransomware spread, but the team should improve early detection of unusual file activity and confirm that backup restoration procedures are tested regularly.

### Open Questions

- How did the ransomware execute on the workstation?
- Was the initial entry point phishing, malicious download, or exposed remote access?
- Were any files copied out before encryption started?
- Were backup and restore procedures completed within the expected recovery time?

## 3. Public Cloud Storage Bucket Exposed Customer Files

**Incident type:** Cloud misconfiguration and data exposure  
**Detection source:** Cloud security scan, storage access policy review, and object access logs  
**Affected assets:** Cloud storage bucket, customer support portal, access policy configuration  
**Incident date:** 2026-06-18  
**Report audience:** Executive

### Incident Summary

A routine cloud security scan found that a storage bucket used by the customer support portal allowed public read access. The bucket contained uploaded support attachments, including screenshots and troubleshooting files.

### Timeline

- 9:00 AM - Cloud security scan detected public read access on a storage bucket.
- 9:12 AM - Security team confirmed the bucket was reachable without authentication.
- 9:20 AM - Public access was disabled.
- 9:35 AM - Cloud access logs were exported for review.
- 10:10 AM - Support team identified the business process that used the bucket.
- 11:00 AM - Security team started reviewing whether files were accessed externally.
- 1:30 PM - New bucket policy review rule was added to prevent public access.

### Log Evidence

- Cloud Security Finding: storage_bucket_public_read=true
- Object Access Log: anonymous GET request observed for two files
- Policy Change: public read access disabled by security-admin
- IAM Review: support-app-role has write permissions

### Known Impact

A customer support storage bucket was exposed to public read access. Two anonymous file access events were observed, but the full impact requires log review.

### Remediation Steps

- Disabled public read access immediately.
- Exported cloud access logs.
- Reviewed bucket policy and IAM permissions.
- Enabled a cloud policy rule to block public bucket access.
- Started file review to determine whether sensitive information was present.
- Opened follow-up ticket for support portal upload workflow review.

### Lessons Learned

Cloud storage policies need stronger preventive controls. Public access should be blocked by default, and storage buckets should be reviewed before being connected to customer-facing workflows.

### Open Questions

- Which files were accessed anonymously?
- Did the exposed files contain personal or sensitive information?
- How long was the bucket publicly readable?
- Why was the public access policy not blocked earlier?

## 4. Malware Alert on Finance Workstation

**Incident type:** Endpoint malware detection  
**Detection source:** Endpoint detection alert, DNS logs, and email gateway review  
**Affected assets:** Finance workstation, endpoint detection tool, shared finance folder  
**Incident date:** 2026-06-19  
**Report audience:** Technical

### Incident Summary

Endpoint detection alerted on a suspicious PowerShell command running from a finance workstation. The workstation had recently opened an email attachment that appeared to be an invoice.

### Timeline

- 10:22 AM - Finance user opened an invoice attachment from an external sender.
- 10:25 AM - Endpoint detection flagged suspicious PowerShell execution.
- 10:27 AM - Workstation attempted to connect to a known suspicious domain.
- 10:30 AM - Security team isolated the workstation from the network.
- 10:45 AM - User account password was reset.
- 11:15 AM - Malware scan completed and suspicious file was quarantined.
- 12:10 PM - Email gateway search found three other users received the same attachment.

### Log Evidence

- EDR Alert: powershell.exe executed encoded command
- DNS Log: workstation attempted connection to suspicious-example-domain.com
- Email Gateway: attachment invoice_update.xlsm delivered to four users
- EDR Action: file quarantined successfully

### Known Impact

One workstation was affected. There is no confirmed lateral movement, but shared finance folder access needs review.

### Remediation Steps

- Isolated the workstation.
- Quarantined the suspicious file.
- Reset the affected user's password.
- Blocked the suspicious domain.
- Searched email gateway logs for similar messages.
- Warned other recipients not to open the attachment.
- Scheduled workstation rebuild if malware persistence is confirmed.

### Lessons Learned

Endpoint detection identified the malware quickly, but email attachment controls and user awareness should be improved. Finance workstations should receive extra monitoring because they may access sensitive files.

### Open Questions

- Did the malware create persistence on the workstation?
- Did the user have access to sensitive finance files during the incident?
- Did any other recipients open the attachment?
- Was the attachment blocked by email security after detection?

## 5. SQL Injection Attempt Against Customer Portal

**Incident type:** Web application attack  
**Detection source:** Web application firewall alert, application logs, and database audit review  
**Affected assets:** Customer portal, web application firewall, application database  
**Incident date:** 2026-06-20  
**Report audience:** Technical

### Incident Summary

The web application firewall detected repeated SQL injection attempts against the customer portal login and search pages. Most requests were blocked, but application logs need review to confirm whether any request reached the database.

### Timeline

- 6:40 PM - Web application firewall detected SQL injection patterns.
- 6:43 PM - Multiple requests targeted the login and search endpoints.
- 6:50 PM - WAF rule moved from monitor mode to block mode.
- 7:05 PM - Source IP addresses were blocked at the firewall.
- 7:30 PM - Application logs were collected for review.
- 8:15 PM - Database audit logs were checked for unusual queries.
- 9:00 PM - Development team opened a ticket to review input validation.

### Log Evidence

- WAF Alert: SQLi pattern detected on /login
- WAF Alert: SQLi pattern detected on /search
- Firewall Action: blocked source IP 203.0.113.xxx
- Database Audit: no confirmed unauthorized SELECT queries found during initial review

### Known Impact

No confirmed data loss has been identified at this stage. The attack was mostly blocked by the web application firewall, but logs must be reviewed to verify whether any request bypassed protection.

### Remediation Steps

- Enabled blocking mode for the relevant WAF rule.
- Blocked attacking source IP addresses.
- Collected web server and application logs.
- Reviewed database audit logs.
- Opened development ticket for input validation review.
- Scheduled follow-up vulnerability scan.

### Lessons Learned

The web application firewall helped reduce risk, but application input validation and database error handling need continued review. Security and development teams should coordinate after suspicious web traffic is detected.

### Open Questions

- Did any SQL injection request bypass the WAF?
- Are login and search inputs fully parameterized?
- Were any database errors exposed to the attacker?
- Should additional WAF rules be enabled before the next scan?

## Recommended Demo Coverage

For the midterm report or final presentation, use at least three scenarios:

- One technical report: Phishing account compromise or SQL injection attempt.
- One executive report: Ransomware or cloud storage exposure.
- One endpoint-focused report: Malware alert on finance workstation.

## Screenshot Evidence To Save

- The prototype form before data entry.
- The prototype form filled with one sample incident.
- The generated report output.
- The section showing the model used and `mock mode: False` when using the real LLM.
- Any terminal output showing tests passing.
