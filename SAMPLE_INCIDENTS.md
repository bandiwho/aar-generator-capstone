# Sample Incidents for Testing and Demo

These sample incidents are used to test and demonstrate the Security Incident AAR Generator. They match the prototype form fields so the team can copy the information into the app, generate an after-action report, and compare the technical and executive report styles.

## How To Use These Samples

1. Open the prototype app.
2. Choose one sample incident.
3. Copy each section into the matching form field.
4. Generate the report.
5. Save a screenshot of the completed form and the generated report output.
6. Review whether the report includes the executive summary, timeline, evidence observations, 5 Whys analysis, root cause, remediation, recommendations, lessons learned, and open questions.

## Form Field Checklist

Use this checklist before generating a report:

- Incident title is specific.
- Incident type is listed.
- Incident date is included.
- Audience is set to technical or executive.
- Detection source is listed.
- Affected assets are listed.
- Incident summary explains what happened, how it was detected, and current status.
- Timeline has clear time-based events.
- Log snippets include realistic alerts, audit events, system records, or ticket notes.
- Known impact separates confirmed facts from unknowns.
- Remediation steps describe containment, recovery, and follow-up.
- Lessons learned explain what should improve.
- Open questions identify facts that still need confirmation.

## 1. Phishing Email Led to Microsoft 365 Account Compromise

**Incident title:** Phishing Email Led to Microsoft 365 Account Compromise  
**Incident type:** Phishing and account compromise  
**Incident date:** 2026-06-16  
**Report audience:** Technical  
**Detection source:** Employee report, Microsoft Defender phishing alert, Azure AD sign-in review, and Exchange audit logs  
**Affected assets:** Microsoft 365, Outlook mailbox, SharePoint access, employee account `brittany.employee`

### Incident Summary

An employee reported a suspicious email after entering credentials into a fake Microsoft 365 login page. Security review showed a successful mailbox login from an unfamiliar IP address, creation of a suspicious inbox forwarding rule, and phishing email delivery to other employees. The affected account was disabled, active sessions were revoked, and mailbox rules were reviewed. No confirmed data exfiltration has been identified yet, but mailbox contents and SharePoint access still require review.

### Timeline

- 8:10 AM - Employee received an email claiming their Microsoft 365 password would expire.
- 8:14 AM - Employee clicked the link and entered credentials into a fake Microsoft 365 login page.
- 8:26 AM - Azure AD recorded a successful login from an unfamiliar IP address.
- 8:31 AM - Exchange audit logs recorded creation of an inbox forwarding rule to an external address.
- 8:42 AM - Defender generated a phishing URL click alert.
- 8:50 AM - Employee reported the suspicious email to the help desk.
- 9:05 AM - Security team disabled the account and revoked active Microsoft 365 sessions.
- 9:25 AM - Password reset was completed and MFA registration was reviewed.
- 10:15 AM - Suspicious mailbox rules were removed and message trace review started.
- 11:00 AM - Security team sent a warning notice to other users who received the phishing message.

### Log Snippets

- AzureAD SignIn: user=brittany.employee result=success location=unfamiliar_ip app=Office365
- Exchange Audit: operation=New-InboxRule user=brittany.employee action=forward_to_external_address
- Defender Alert: category=Phishing URL clicked severity=High user=brittany.employee
- Message Trace: sender=security-update-example.com recipients=14 status=delivered
- SharePoint Audit: review pending for file access after suspicious login time

### Known Impact

One employee mailbox was accessed by an unfamiliar login. A suspicious forwarding rule was created and removed. Fourteen employees received similar phishing emails. No confirmed data exfiltration has been identified, but mailbox contents, SharePoint access, and whether any other users submitted credentials still need review.

### Remediation Steps

- Disabled the affected account.
- Revoked active Microsoft 365 sessions.
- Reset the user password.
- Reviewed MFA registration and sign-in history.
- Removed suspicious mailbox forwarding rules.
- Blocked the phishing URL and sender domain.
- Started message trace review to identify other affected users.
- Sent a warning notice to employees who received the same email.
- Started SharePoint and mailbox audit review for possible unauthorized access.

### Lessons Learned

The employee report helped the team respond quickly, but MFA enforcement, phishing-resistant authentication, and inbox rule monitoring need improvement. The team should also confirm whether phishing URL clicks and suspicious mailbox rules are escalated quickly enough.

### Open Questions

- Was MFA challenged, bypassed, or not enabled during the suspicious login?
- Did the attacker access or download SharePoint files?
- Did any other users enter credentials into the phishing page?
- How long was the forwarding rule active before removal?

## 2. Ransomware Detected on Shared File Server

**Incident title:** Ransomware Detected on Shared File Server  
**Incident type:** Ransomware and file encryption  
**Incident date:** 2026-06-17  
**Report audience:** Executive  
**Detection source:** Help desk tickets, endpoint protection alert, file server activity logs, and backup system review  
**Affected assets:** Windows file server `FS-DEPT-01`, shared department drive, endpoint workstation `WORKSTATION-22`, affected user account

### Incident Summary

Several users reported that shared department documents would not open and that file extensions had changed. Endpoint protection alerted on ransomware behavior from one workstation connected to the shared drive. The workstation was isolated, file share access was temporarily disabled, and the team confirmed that a clean backup snapshot was available. Initial review suggests partial encryption of the shared drive, with no confirmed evidence of data theft at this stage.

### Timeline

- 2:05 PM - Help desk received three tickets reporting that shared files would not open.
- 2:11 PM - Endpoint protection generated a ransomware behavior alert from `WORKSTATION-22`.
- 2:16 PM - Security team identified rapid file rename and write activity on the shared drive.
- 2:20 PM - `WORKSTATION-22` was isolated from the network.
- 2:28 PM - Department file share access was temporarily disabled to stop additional changes.
- 2:45 PM - Server snapshots and backups were checked.
- 3:05 PM - Last clean snapshot was confirmed from 1:00 PM.
- 3:30 PM - Affected file paths were documented for restore planning.
- 4:15 PM - Restore plan was approved by IT leadership.
- 5:30 PM - Recovery began from the last clean snapshot.

### Log Snippets

- EDR Alert: host=WORKSTATION-22 behavior=mass_file_rename severity=Critical
- File Server Event: source=WORKSTATION-22 action=high_volume_write path=department_share
- Windows Security Log: user account accessed shared drive before encryption activity
- Backup System: snapshot=FS-DEPT-01_2026-06-17_1300 status=successful
- Help Desk Ticket: multiple users reported files renamed and unreadable

### Known Impact

A shared department drive was partially encrypted, causing temporary loss of access to some department documents. Business impact included interrupted work for users who depended on the shared drive. Initial review suggests the affected files can be restored from backup. No confirmed evidence of data theft has been identified, but the team still needs to determine how the ransomware executed and whether any files were copied before encryption.

### Remediation Steps

- Isolated the affected workstation.
- Disabled file share access temporarily.
- Preserved endpoint, file server, and backup logs for review.
- Confirmed backup availability.
- Documented affected file paths.
- Restored affected files from the last clean snapshot.
- Reset credentials for the affected user account.
- Scheduled malware scan and workstation rebuild.
- Opened follow-up review for file activity monitoring and recovery time.

### Lessons Learned

Rapid isolation helped limit the spread of ransomware, and having a recent backup reduced recovery risk. The team should improve detection of unusual file activity, test backup restoration procedures regularly, and review whether endpoint controls could have stopped the ransomware earlier.

### Open Questions

- How did the ransomware execute on the workstation?
- Was the initial entry point phishing, malicious download, or exposed remote access?
- Were any files copied out before encryption started?
- Did the restore complete within the expected recovery time objective?
- Were any other workstations showing similar suspicious activity?

## 3. Public Cloud Storage Bucket Exposed Customer Files

**Incident title:** Public Cloud Storage Bucket Exposed Customer Files  
**Incident type:** Cloud misconfiguration and data exposure  
**Incident date:** 2026-06-18  
**Report audience:** Executive  
**Detection source:** Cloud security scan, storage access policy review, object access logs, and support portal review  
**Affected assets:** Cloud storage bucket `support-uploads-prod`, customer support portal, bucket access policy, support application role

### Incident Summary

A routine cloud security scan found that a storage bucket used by the customer support portal allowed public read access. The bucket contained customer support attachments, including screenshots and troubleshooting files. Public access was disabled after confirmation, and cloud access logs were exported for review. Two anonymous file access events were observed, but the full impact depends on confirming which files were accessed and whether they contained sensitive information.

### Timeline

- 9:00 AM - Cloud security scan detected public read access on `support-uploads-prod`.
- 9:12 AM - Security team confirmed the bucket was reachable without authentication.
- 9:20 AM - Public read access was disabled.
- 9:35 AM - Cloud access logs were exported for review.
- 10:10 AM - Support team confirmed the bucket was used for support portal uploads.
- 11:00 AM - Security team started reviewing anonymous access events.
- 12:15 PM - File inventory was started to identify potentially sensitive attachments.
- 1:30 PM - New policy review rule was added to block public bucket access.
- 2:10 PM - Follow-up ticket was opened for support portal upload workflow review.

### Log Snippets

- Cloud Security Finding: resource=support-uploads-prod storage_bucket_public_read=true severity=High
- Object Access Log: principal=anonymous action=GET object_count=2
- Policy Change: actor=security-admin action=disabled_public_read_access resource=support-uploads-prod
- IAM Review: role=support-app-role permission=write_objects public_read_not_required
- Ticket Note: support portal uploads stored customer-provided attachments

### Known Impact

A customer support storage bucket was exposed to public read access. Two anonymous file access events were observed. The team has not yet confirmed whether those files contained personal, customer, or sensitive information. Business risk includes possible customer data exposure, reporting obligations, and loss of trust if sensitive files were accessed.

### Remediation Steps

- Disabled public read access immediately.
- Exported cloud access logs.
- Reviewed bucket policy and IAM permissions.
- Enabled a cloud policy rule to block public bucket access.
- Started file review to determine whether sensitive information was present.
- Opened follow-up ticket for the support portal upload workflow.
- Added a review step for storage bucket policies connected to customer-facing systems.

### Lessons Learned

Cloud storage policies need stronger preventive controls. Public access should be blocked by default, and storage buckets should be reviewed before being connected to customer-facing workflows. The team should also improve asset ownership tracking so business owners can quickly confirm what data is stored in each bucket.

### Open Questions

- Which files were accessed anonymously?
- Did the exposed files contain personal, customer, or sensitive information?
- How long was the bucket publicly readable?
- Why was public access not blocked by default?
- Who owns the support portal upload workflow and approval process?

## 4. Malware Alert on Finance Workstation

**Incident title:** Malware Alert on Finance Workstation  
**Incident type:** Endpoint malware detection  
**Incident date:** 2026-06-19  
**Report audience:** Technical  
**Detection source:** Endpoint detection alert, DNS logs, email gateway review, and workstation malware scan  
**Affected assets:** Finance workstation `FIN-WS-07`, finance user account, endpoint detection tool, shared finance folder

### Incident Summary

Endpoint detection alerted on suspicious PowerShell activity from a finance workstation shortly after the user opened an email attachment labeled as an invoice. DNS logs showed an attempted connection to a suspicious domain, and the email gateway confirmed that the same attachment was delivered to four users. The workstation was isolated, the suspicious file was quarantined, and the affected user's password was reset. There is no confirmed lateral movement, but access to the shared finance folder requires review.

### Timeline

- 10:22 AM - Finance user opened an invoice attachment from an external sender.
- 10:25 AM - Endpoint detection flagged suspicious encoded PowerShell execution.
- 10:27 AM - Workstation attempted to connect to a suspicious domain.
- 10:30 AM - Security team isolated the workstation from the network.
- 10:45 AM - Affected user's password was reset.
- 11:15 AM - Malware scan completed and suspicious file was quarantined.
- 11:40 AM - DNS block was added for the suspicious domain.
- 12:10 PM - Email gateway search found three other users received the same attachment.
- 12:30 PM - Other recipients were warned not to open the attachment.

### Log Snippets

- EDR Alert: host=FIN-WS-07 process=powershell.exe command=encoded_command severity=High
- DNS Log: host=FIN-WS-07 query=suspicious-example-domain.com action=allowed_then_blocked
- Email Gateway: attachment=invoice_update.xlsm recipients=4 sender=external
- EDR Action: file=invoice_update.xlsm status=quarantined
- Windows Event: user opened attachment shortly before PowerShell alert

### Known Impact

One finance workstation was affected and isolated. The suspicious file was quarantined. There is no confirmed lateral movement or data exfiltration, but the user's access to the shared finance folder needs review because the workstation may have had access to sensitive financial documents.

### Remediation Steps

- Isolated the workstation.
- Quarantined the suspicious file.
- Reset the affected user's password.
- Blocked the suspicious domain.
- Searched email gateway logs for similar messages.
- Warned other recipients not to open the attachment.
- Reviewed finance folder access during the incident window.
- Scheduled workstation rebuild if malware persistence is confirmed.

### Lessons Learned

Endpoint detection identified the suspicious activity quickly, but email attachment controls and user awareness should be improved. Finance workstations should receive extra monitoring because they may access sensitive files. The team should also review whether macro-enabled attachments should be blocked or sandboxed before delivery.

### Open Questions

- Did the malware create persistence on the workstation?
- Did the user access sensitive finance files during the incident window?
- Did any other recipients open the attachment?
- Was the attachment blocked by email security after detection?
- Should macro-enabled attachments be restricted for finance users?

## 5. SQL Injection Attempt Against Customer Portal

**Incident title:** SQL Injection Attempt Against Customer Portal  
**Incident type:** Web application attack  
**Incident date:** 2026-06-20  
**Report audience:** Technical  
**Detection source:** Web application firewall alert, application logs, database audit review, and firewall block list  
**Affected assets:** Customer portal, login endpoint, search endpoint, web application firewall, application database

### Incident Summary

The web application firewall detected repeated SQL injection attempts against the customer portal login and search pages. Most requests were blocked, and the WAF rule was moved from monitor mode to block mode. Application and database logs were collected to confirm whether any request reached the database. Initial database audit review found no confirmed unauthorized queries, but input validation and error handling still need review by the development team.

### Timeline

- 6:40 PM - Web application firewall detected SQL injection patterns.
- 6:43 PM - Multiple requests targeted `/login` and `/search` endpoints.
- 6:50 PM - WAF rule was moved from monitor mode to block mode.
- 7:05 PM - Source IP addresses were blocked at the firewall.
- 7:30 PM - Web server and application logs were collected for review.
- 8:15 PM - Database audit logs were checked for unusual queries.
- 8:40 PM - Initial database review found no confirmed unauthorized `SELECT` queries.
- 9:00 PM - Development team opened a ticket to review input validation and parameterized queries.
- 9:30 PM - Follow-up vulnerability scan was scheduled.

### Log Snippets

- WAF Alert: path=/login pattern=SQLi severity=High action=monitor
- WAF Alert: path=/search pattern=SQLi severity=High action=blocked_after_rule_change
- Firewall Action: source_ip=203.0.113.xxx action=blocked
- Application Log: repeated invalid input submitted to login and search parameters
- Database Audit: no confirmed unauthorized SELECT queries found during initial review

### Known Impact

No confirmed data loss has been identified. The attack appears to have been mostly blocked by the web application firewall, but application logs must be reviewed to verify whether any request bypassed protection. The incident exposed a need to confirm input validation, parameterized queries, and database error handling in the customer portal.

### Remediation Steps

- Enabled blocking mode for the relevant WAF rule.
- Blocked attacking source IP addresses.
- Collected web server and application logs.
- Reviewed database audit logs.
- Opened development ticket for input validation and parameterized query review.
- Scheduled follow-up vulnerability scan.
- Reviewed whether database errors are hidden from users.

### Lessons Learned

The web application firewall helped reduce risk, but application security cannot depend only on WAF rules. Security and development teams should review input validation, parameterized queries, error handling, and the process for moving WAF rules from monitor mode to block mode.

### Open Questions

- Did any SQL injection request bypass the WAF before block mode was enabled?
- Are login and search inputs fully parameterized?
- Were any database errors exposed to the attacker?
- Should additional WAF rules be enabled before the next scan?
- Should the customer portal receive a focused secure code review?

## Recommended Demo Coverage

For the final presentation, use three scenarios:

- One technical report: Phishing account compromise.
- One executive report: Ransomware on the shared file server.
- One application or cloud report: SQL injection attempt or public cloud storage exposure.

## Screenshot Evidence To Save

- The prototype form before data entry.
- The prototype form filled with one sample incident.
- The generated report output.
- The section showing the model used and `mock mode: False` when using the real LLM.
- Any terminal output showing tests passing.
