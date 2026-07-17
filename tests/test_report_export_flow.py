from fastapi.testclient import TestClient

from aar_generator.main import app


def test_generated_report_page_shows_practical_export_options():
    client = TestClient(app)

    response = client.post(
        "/generate-form",
        data={
            "title": "Unauthorized VPN access",
            "incident_type": "Account compromise",
            "incident_date": "2026-06-11",
            "audience": "technical",
            "detection_source": "SIEM impossible travel alert",
            "affected_assets": "VPN account and remote access service",
            "incident_summary": "Suspicious VPN activity was detected for one user account after an impossible travel alert.",
            "timeline": "09:15 alert fired\n09:30 account disabled\n10:00 password reset completed",
            "log_snippets": "vpn_login user=mike source=unknown",
            "remediation_steps": "Disabled account, reset password, reviewed VPN logs, and opened follow-up ticket.",
            "known_impact": "No confirmed data loss at this stage.",
            "lessons_learned": "MFA status should be checked earlier during triage.",
            "open_questions": "Need to confirm whether MFA was challenged.",
        },
    )

    assert response.status_code == 200
    assert "Copy and export" in response.text
    assert "Editable Text" in response.text
    assert "HTML" in response.text
    assert "Save as PDF" in response.text
    assert "Generated Report Preview" in response.text
    assert 'class="secondary-button new-incident-button" id="new-incident"' in response.text
    assert 'data-incident-date="2026-06-11"' in response.text
    assert 'data-report-audience="technical"' in response.text
    assert "normalizeReportText" in response.text
    assert '.replaceAll("â†’", "->")' in response.text
    assert "buildPlainTextFromRenderedReport" in response.text
    assert "buildMarkdownFromRenderedReport" in response.text
    assert '.replace(/^\\d+\\.\\s*/, "")' in response.text
    assert 'listElement.getAttribute("start")' in response.text
    assert "Number.parseInt(numbered[1], 10)" in response.text
    assert 'buildReportFilename("md")' in response.text
    assert 'buildReportFilename("html")' in response.text
