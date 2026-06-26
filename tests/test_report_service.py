from aar_generator.llm_client import LlmClient
from aar_generator.config import Settings
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


def test_llm_client_auto_model_uses_first_available_model():
    client = LlmClient(Settings(openai_model="auto"))

    assert client.resolve_model(FakeClient()) == "teacher-model-from-list"


def test_report_service_returns_mock_report():
    settings = Settings(mock_llm=True, openai_model="test-model")
    service = ReportService(settings)
    incident = IncidentInput(
        title="Unauthorized VPN access",
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

    result = service.generate_report(incident)

    assert result.mock_mode is True
    assert result.model_used == "test-model"
    assert "5 Whys Root Cause Analysis" in result.report_markdown
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
    incident = IncidentInput(
        title="Unauthorized VPN access",
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

    def fail_generate(prompt):
        raise RuntimeError("model access failed")

    monkeypatch.setattr(service.llm_client, "generate", fail_generate)

    result = service.generate_report(incident)

    assert result.mock_mode is True
    assert "5 Whys Root Cause Analysis" in result.report_markdown
    assert "Recommendations and Owners" in result.report_markdown
