from aar_generator.config import Settings
from aar_generator.llm_client import LlmClient
from aar_generator.report_service import ReportService
from aar_generator.schemas import AudienceStyle, IncidentInput


class FakeModel:
    id = "teacher-model-from-list"


class FakeModels:
    def list(self):
        class ModelList:
            data = [FakeModel()]

        return ModelList()


class FakeClient:
    models = FakeModels()


def build_incident() -> IncidentInput:
    return IncidentInput(
        title="Unauthorized VPN access",
        incident_type="Account compromise",
        incident_date="2026-06-11",
        audience=AudienceStyle.technical,
        detection_source="SIEM impossible travel alert",
        affected_assets="VPN account and remote access service",
        incident_summary="Suspicious VPN activity was detected for one user account after an impossible travel alert.",
        timeline="09:15 alert fired\n09:30 account disabled\n10:00 password reset completed",
        log_snippets="vpn_login user=mike source=unknown",
        remediation_steps="Disabled account, reset password, reviewed VPN logs, and opened follow-up ticket.",
        known_impact="No confirmed data loss at this stage.",
        lessons_learned="MFA status should be checked earlier during triage.",
        open_questions="Need to confirm whether MFA was challenged.",
    )


def test_llm_client_auto_model_uses_first_available_model():
    client = LlmClient(Settings(openai_model="auto"))

    assert client.resolve_model(FakeClient()) == "teacher-model-from-list"


def test_report_service_returns_mock_report():
    settings = Settings(mock_llm=True, openai_model="test-model")
    service = ReportService(settings)

    result = service.generate_report(build_incident())

    assert result.mock_mode is True
    assert result.model_used == "test-model"
    assert "5 Whys Root Cause Analysis" in result.report_markdown
    assert "Account compromise" in result.report_markdown
    assert "SIEM impossible travel alert" in result.report_markdown
    assert "VPN account and remote access service" in result.report_markdown
    assert "Need to confirm whether MFA was challenged." in result.report_markdown
    assert "Incident type: Account compromise" in result.report_markdown
    assert "Audience style: Technical" in result.report_markdown
    assert "Assign an incident owner" in result.report_markdown
    assert "Assign the security operations team" in result.report_markdown
    assert "Assign a process owner" in result.report_markdown
    assert "Garrett:" not in result.report_markdown
    assert "Mike:" not in result.report_markdown
    assert "Brittany:" not in result.report_markdown


def test_report_service_falls_back_to_mock_report_when_api_fails(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="auto")
    service = ReportService(settings)

    def fail_generate(prompt):
        raise RuntimeError("model access failed")

    monkeypatch.setattr(service.llm_client, "generate", fail_generate)

    result = service.generate_report(build_incident())

    assert result.mock_mode is True
    assert "5 Whys Root Cause Analysis" in result.report_markdown
    assert "Recommendations and Owners" in result.report_markdown
    assert "Account compromise" in result.report_markdown
    assert "SIEM impossible travel alert" in result.report_markdown


def test_report_service_cleans_repetitive_gap_and_task_bullet_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_repetitive_labels(prompt):
        return """
## Process and Communication Gaps

- **Gap:** MFA effectiveness needs confirmation.
- Gap: Escalation timing needs review.

## Remediation Completed

- **Task:** Disabled the affected account.
- Task: Reset the user password.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_repetitive_labels)

    result = service.generate_report(build_incident())

    assert "- MFA effectiveness needs confirmation." in result.report_markdown
    assert "- Escalation timing needs review." in result.report_markdown
    assert "- Disabled the affected account." in result.report_markdown
    assert "- Reset the user password." in result.report_markdown
    assert "Gap:" not in result.report_markdown
    assert "Task:" not in result.report_markdown


def test_report_service_cleans_repeated_security_team_bullet_intro(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_repeated_intro(prompt):
        return """
## Remediation Completed

- The security team disabled the affected account.
- The security team revoked active Microsoft 365 sessions.
- The security team reset the user password.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_repeated_intro)

    result = service.generate_report(build_incident())

    assert "- Disabled the affected account." in result.report_markdown
    assert "- Revoked active Microsoft 365 sessions." in result.report_markdown
    assert "- Reset the user password." in result.report_markdown
    assert "The security team" not in result.report_markdown


def test_report_service_cleans_repeated_security_team_plain_line_intro(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_repeated_plain_intro(prompt):
        return """
## Remediation Completed

The security team disabled the affected account.
The security team revoked active Microsoft 365 sessions.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_repeated_plain_intro)

    result = service.generate_report(build_incident())

    assert "Disabled the affected account." in result.report_markdown
    assert "Revoked active Microsoft 365 sessions." in result.report_markdown
    assert "The security team" not in result.report_markdown


def test_report_service_removes_chat_style_closing_offer(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_chat_closing(prompt):
        return """
## Open Questions

- Was MFA challenged during the suspicious login?
- Did the attacker access SharePoint files?

If you share additional log fields (MFA sign-in result, exact rule removal time, SharePoint audit entries, and any authentication events for other users), I can revise this draft to tighten conclusions and reduce assumptions.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_chat_closing)

    result = service.generate_report(build_incident())

    assert "Was MFA challenged during the suspicious login?" in result.report_markdown
    assert "Did the attacker access SharePoint files?" in result.report_markdown
    assert "If you share additional" not in result.report_markdown
    assert "I can revise this draft" not in result.report_markdown


def test_report_service_removes_repeated_open_question_lead_in_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_open_question_labels(prompt):
        return """
## Open Questions

- How long was the forwarding rule active before removal?
Open item: Provided logs show creation at 8:31 AM and removal at 10:15 AM.

- Was MFA challenged during the suspicious login?
Assumption: MFA may not have prevented the sign-in, but the logs do not show the MFA result.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_open_question_labels)

    result = service.generate_report(build_incident())

    assert "Provided logs show creation at 8:31 AM and removal at 10:15 AM." in result.report_markdown
    assert "MFA may not have prevented the sign-in" in result.report_markdown
    assert "Open item:" not in result.report_markdown
    assert "Assumption:" not in result.report_markdown


def test_report_service_shortens_evidence_note_label(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_evidence_note_labels(prompt):
        return """
## Open Questions

- Was MFA challenged during the suspicious login?
Evidence note: MFA registration was reviewed, but authentication result details are missing.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_evidence_note_labels)

    result = service.generate_report(build_incident())

    assert "Evidence: MFA registration was reviewed" in result.report_markdown
    assert "Evidence note:" not in result.report_markdown


def test_report_service_cleans_broken_smart_quote_encoding(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_broken_quotes(prompt):
        return """
## Impact Assessment

SharePoint audit activity was marked as â€œreview pending,â€ and the employeeâ€™s report started the investigation. Attack path: phish â†’ sign-in.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_broken_quotes)

    result = service.generate_report(build_incident())

    assert '"review pending,"' in result.report_markdown
    assert "employee's report" in result.report_markdown
    assert "phish -> sign-in" in result.report_markdown


def test_report_service_rewrites_five_whys_without_why_number_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_why_number_labels(prompt):
        return """
## 5 Whys Root Cause Analysis

- Why 1: Why were shared documents encrypted?
- Why 2: Why did ransomware-like software execute on WORKSTATION-22?
- Why 3: Why was the workstation compromise not prevented earlier?
Because ransomware-like software executed on WORKSTATION-22.
Because the workstation was compromised before encryption activity.
Because endpoint controls did not stop execution before file encryption attempts.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_why_number_labels)

    result = service.generate_report(build_incident())

    assert "1. Why were shared documents encrypted? Because ransomware-like software executed" in result.report_markdown
    assert "2. Why did ransomware-like software execute on WORKSTATION-22? Because the workstation was compromised" in result.report_markdown
    assert "- Why 1:" not in result.report_markdown
    assert "Why 2:" not in result.report_markdown


def test_report_service_pairs_recommendations_with_owners(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_separated_recommendation_owners(prompt):
        return """
## Recommendations and Owners

### Identity & Authentication

- Enforce phishing-resistant authentication for all users.
- Require step-up MFA for sign-ins from unfamiliar IPs.

**Owner:** Identity Security / IAM Team
**Owner:** IAM + Cloud Security Engineering

### Email & Mailbox Security Controls

- Implement automated detection for high-risk mailbox rule changes.

Owner: Exchange/M365 Security Operations
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_separated_recommendation_owners)

    result = service.generate_report(build_incident())

    assert "- Enforce phishing-resistant authentication for all users. **Owner:** Identity Security / IAM Team" in result.report_markdown
    assert "- Require step-up MFA for sign-ins from unfamiliar IPs. **Owner:** IAM + Cloud Security Engineering" in result.report_markdown
    assert "- Implement automated detection for high-risk mailbox rule changes. **Owner:** Exchange/M365 Security Operations" in result.report_markdown
    assert "\n**Owner:**" not in result.report_markdown
    assert "\nOwner:" not in result.report_markdown


def test_report_service_repairs_broken_inline_owner_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_broken_inline_owner_labels(prompt):
        return """
## Recommendations and Owners

- Enforce phishing-resistant authentication for all users. Owner:** Identity & Access Management Team
- Complete SharePoint access auditing. **Owner: Microsoft 365 Governance Team

## 5 Whys Root Cause Analysis

5. Why were detection and prevention controls not triggered earlier enough to stop mailbox actions? Because mailbox rule monitoring needs improvement.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_broken_inline_owner_labels)

    result = service.generate_report(build_incident())

    assert " Owner:**" not in result.report_markdown
    assert "**Owner: Microsoft" not in result.report_markdown
    assert "- Enforce phishing-resistant authentication for all users. **Owner:** Identity & Access Management Team" in result.report_markdown
    assert "- Complete SharePoint access auditing. **Owner:** Microsoft 365 Governance Team" in result.report_markdown
    assert "Why did detection and prevention controls not trigger early enough to stop mailbox actions?" in result.report_markdown


def test_report_service_cleans_numbered_heading_recommendation_owner_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_numbered_heading_and_trailing_owner_markers(prompt):
        return """
## 11. Recommendations and Owners

- Enforce phishing-resistant authentication, **Owner:** Identity Security Engineering Team**.
- Add mailbox rule monitoring, **Owner:** Microsoft 365 Security Operations Team**.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_numbered_heading_and_trailing_owner_markers)

    result = service.generate_report(build_incident())

    assert "**Owner:** Identity Security Engineering Team." in result.report_markdown
    assert "**Owner:** Microsoft 365 Security Operations Team." in result.report_markdown
    assert "Team**" not in result.report_markdown


def test_report_service_cleans_broken_evidence_dash_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_broken_evidence_dash_labels(prompt):
        return """
## Impact Assessment

**Confirmed impacts based on available Evidence: - The **brittany.employee mailbox** was accessed via an **unfamiliar sign-in**.

## Evidence and Log Observations

- **Azure AD Sign-in Evidence: - A successful Office365 sign-in occurred for **brittany.employee** from an **unfamiliar IP address**.
- **Defender alert Evidence: - A **high-severity alert** indicated that the user clicked a phishing URL.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_broken_evidence_dash_labels)

    result = service.generate_report(build_incident())

    assert "**Confirmed impacts based on available Evidence:** The **brittany.employee mailbox**" in result.report_markdown
    assert "- **Azure AD Sign-in Evidence:** A successful Office365 sign-in occurred for **brittany.employee**" in result.report_markdown
    assert "- **Defender alert Evidence:** A **high-severity alert** indicated" in result.report_markdown
    assert "Evidence: -" not in result.report_markdown


def test_report_service_rewrites_five_whys_heading_answers(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_heading_answers(prompt):
        return """
## 5 Whys Root Cause Analysis

### Why 1: Why did the Microsoft 365 account get compromised?
- Because the employee entered credentials into a fake Microsoft 365 login page.
### Why 2: Why were the credentials usable by the attacker?
- Because the sign-in process did not stop the attacker.
### Why 3: Why was the sign-in not blocked?
- Because MFA behavior is not confirmed.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_heading_answers)

    result = service.generate_report(build_incident())

    assert "1. Why did the Microsoft 365 account get compromised? Because the employee entered credentials" in result.report_markdown
    assert "2. Why were the credentials usable by the attacker? Because the sign-in process" in result.report_markdown
    assert "### Why 1:" not in result.report_markdown


def test_report_service_rewrites_numbered_bold_five_whys_answers(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_numbered_bold_questions(prompt):
        return """
## 5 Whys Root Cause Analysis

1. **Why was the account compromised?**
Because the employee entered credentials into a fake Microsoft 365 login page.
2. **Why did the attacker gain usable access?**
Because the sign-in resulted in a successful session.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_numbered_bold_questions)

    result = service.generate_report(build_incident())

    assert "1. Why was the account compromised? Because the employee entered credentials" in result.report_markdown
    assert "2. Why did the attacker gain usable access? Because the sign-in resulted" in result.report_markdown
    assert "**Why was the account compromised?**\nBecause" not in result.report_markdown


def test_report_service_interleaves_numbered_heading_five_whys_answers(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_numbered_heading_five_whys(prompt):
        return """
## 7. 5 Whys Root Cause Analysis

1. **Why was the account compromised?**
2. **Why could the attacker authenticate after credential submission?**
Because credentials were entered into a fake Microsoft 365 login page.
Because the attacker was able to establish a successful session.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_numbered_heading_five_whys)

    result = service.generate_report(build_incident())

    assert "1. Why was the account compromised? Because credentials were entered" in result.report_markdown
    assert "2. Why could the attacker authenticate after credential submission? Because the attacker was able" in result.report_markdown
    assert "**Why was the account compromised?**" not in result.report_markdown


def test_report_service_normalizes_sample_account_typo(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_account_typo(prompt):
        return "The Microsoft 365 account for britanny.employee was compromised."

    monkeypatch.setattr(service.llm_client, "generate", generate_with_account_typo)

    result = service.generate_report(build_incident())

    assert "brittany.employee" in result.report_markdown
    assert "britanny.employee" not in result.report_markdown


def test_report_service_pairs_alternating_open_question_evidence(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_alternating_open_question_evidence(prompt):
        return """
## Open Questions

- Was MFA challenged, bypassed, or not enabled during the suspicious login?
Evidence: MFA registration was reviewed after compromise, but the exact sign-in outcome is missing.
- Did the attacker access or download SharePoint files?
Evidence: SharePoint audit review is pending.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_alternating_open_question_evidence)

    result = service.generate_report(build_incident())

    assert "- Was MFA challenged, bypassed, or not enabled during the suspicious login?\n  Evidence: MFA registration was reviewed" in result.report_markdown
    assert "- Did the attacker access or download SharePoint files?\n  Evidence: SharePoint audit review is pending." in result.report_markdown


def test_report_service_splits_inline_open_question_evidence_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_inline_open_question_evidence(prompt):
        return """
## Open Questions

- Was MFA challenged, bypassed, or not enabled during the suspicious login?Evidence:** Provided logs show success but not MFA outcome.
- Did the attacker access or download SharePoint files?**Evidence:** SharePoint review is pending.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_inline_open_question_evidence)

    result = service.generate_report(build_incident())

    assert "- Was MFA challenged, bypassed, or not enabled during the suspicious login?\n  Evidence: Provided logs show success" in result.report_markdown
    assert "- Did the attacker access or download SharePoint files?\n  Evidence: SharePoint review is pending." in result.report_markdown
    assert "?Evidence" not in result.report_markdown
    assert "Evidence:**" not in result.report_markdown


def test_report_service_splits_bold_open_question_evidence_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_bold_inline_open_question_evidence(prompt):
        return """
## Open Questions

- **Was MFA challenged, bypassed, or not enabled during the suspicious login?Evidence: The report states MFA registration was reviewed, but it does not state whether MFA succeeded at the **8:26 AM** sign-in.
- **Did the attacker access or download SharePoint files during the compromise window?Evidence: SharePoint audit review is explicitly marked as **pending** for file access after the login time.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_bold_inline_open_question_evidence)

    result = service.generate_report(build_incident())

    assert "- Was MFA challenged, bypassed, or not enabled during the suspicious login?\n  Evidence: The report states MFA registration was reviewed" in result.report_markdown
    assert "- Did the attacker access or download SharePoint files during the compromise window?\n  Evidence: SharePoint audit review is explicitly marked as **pending**" in result.report_markdown
    assert "?Evidence" not in result.report_markdown
    assert "login?Evidence" not in result.report_markdown


def test_report_service_cleans_unclosed_bold_open_question_evidence_labels(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_unclosed_bold_open_question_evidence(prompt):
        return """
## 13. Open Questions

- **Was MFA challenged, bypassed, or not enabled during the suspicious login?Evidence: The incident notes password reset and MFA registration review, but does not state the MFA outcome.
- **Did the attacker access or download SharePoint files after the suspicious login time?Evidence: SharePoint audit review is explicitly pending.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_unclosed_bold_open_question_evidence)

    result = service.generate_report(build_incident())

    assert "- Was MFA challenged, bypassed, or not enabled during the suspicious login?\n  Evidence: The incident notes password reset" in result.report_markdown
    assert "- Did the attacker access or download SharePoint files after the suspicious login time?\n  Evidence: SharePoint audit review is explicitly pending." in result.report_markdown
    assert "- **Was MFA" not in result.report_markdown
    assert "?Evidence" not in result.report_markdown


def test_report_service_removes_dangling_bold_markers_from_open_question_evidence(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_dangling_open_question_evidence_bold(prompt):
        return """
## 13. Open Questions

- Did any other users enter credentials into the phishing page?Evidence: Message trace shows the phishing email was delivered to 14 recipients**, but no evidence is provided confirming whether any of them submitted credentials.
- How long was the forwarding rule active before removal?Evidence: Exchange audit shows rule creation at 8:31 AM, and rule removal is noted at 10:15 AM**, but exact timestamps for the removal event are not included.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_dangling_open_question_evidence_bold)

    result = service.generate_report(build_incident())

    assert "- Did any other users enter credentials into the phishing page?\n  Evidence: Message trace shows the phishing email was delivered to 14 recipients, but no evidence" in result.report_markdown
    assert "- How long was the forwarding rule active before removal?\n  Evidence: Exchange audit shows rule creation at 8:31 AM, and rule removal is noted at 10:15 AM, but exact timestamps" in result.report_markdown
    assert "recipients**" not in result.report_markdown
    assert "10:15 AM**" not in result.report_markdown


def test_report_service_pairs_open_question_evidence_with_each_question(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_separated_open_question_evidence(prompt):
        return """
## Open Questions

- How did the ransomware execute on WORKSTATION-22?
- Was the initial entry point phishing, malicious download, or exposed remote access?
- Were any files copied out before encryption started?
Evidence: Timeline confirms ransomware behavior but not the initial infection vector.
Evidence: Windows Security Log shows shared drive access but not the entry method.
Evidence: No outbound transfer logs are included in the provided snippets.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_separated_open_question_evidence)

    result = service.generate_report(build_incident())

    assert "- How did the ransomware execute on WORKSTATION-22?\n  Evidence: Timeline confirms ransomware behavior" in result.report_markdown
    assert "- Was the initial entry point phishing, malicious download, or exposed remote access?\n  Evidence: Windows Security Log" in result.report_markdown
    assert "- Were any files copied out before encryption started?\n  Evidence: No outbound transfer logs" in result.report_markdown
    assert "â€œ" not in result.report_markdown
    assert "â€™" not in result.report_markdown
    assert "â†’" not in result.report_markdown


def test_report_service_pairs_numbered_heading_open_question_evidence(monkeypatch):
    settings = Settings(mock_llm=False, openai_api_key="test-key", openai_model="test-model")
    service = ReportService(settings)

    def generate_with_numbered_heading_open_questions(prompt):
        return """
## 13. Open Questions

- Was MFA challenged, bypassed, or not enabled during the suspicious login?
- Did the attacker access or download SharePoint files?
Evidence: MFA registration was reviewed, but the outcome is missing.
Evidence: SharePoint audit review is pending.
""".strip()

    monkeypatch.setattr(service.llm_client, "generate", generate_with_numbered_heading_open_questions)

    result = service.generate_report(build_incident())

    assert "- Was MFA challenged, bypassed, or not enabled during the suspicious login?\n  Evidence: MFA registration was reviewed" in result.report_markdown
    assert "- Did the attacker access or download SharePoint files?\n  Evidence: SharePoint audit review is pending." in result.report_markdown
