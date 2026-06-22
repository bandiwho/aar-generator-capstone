from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from aar_generator.config import get_settings
from aar_generator.report_service import ReportService
from aar_generator.schemas import AudienceStyle, IncidentInput, ReportResponse

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Security Incident AAR Generator",
    description="Polished Team 1 prototype for generating security incident after-action report drafts.",
    version="0.2.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/health")
def health() -> dict[str, str | bool]:
    settings = get_settings()
    return {
        "status": "ok",
        "environment": settings.app_env,
        "mock_mode": settings.mock_llm or not settings.openai_api_key,
        "model": settings.openai_model,
    }


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "audiences": [style.value for style in AudienceStyle],
            "result": None,
            "error": None,
        },
    )


@app.post("/generate", response_model=ReportResponse)
def generate_report(payload: IncidentInput) -> ReportResponse:
    service = ReportService(get_settings())
    return service.generate_report(payload)


@app.post("/generate-form", response_class=HTMLResponse)
def generate_report_form(
    request: Request,
    title: str = Form(...),
    incident_date: str = Form(...),
    audience: AudienceStyle = Form(...),
    detection_source: str = Form(""),
    affected_assets: str = Form(""),
    incident_summary: str = Form(...),
    timeline: str = Form(...),
    log_snippets: str = Form(""),
    remediation_steps: str = Form(...),
    known_impact: str = Form(""),
    lessons_learned: str = Form(""),
    open_questions: str = Form(""),
) -> HTMLResponse:
    try:
        incident = IncidentInput(
            title=title,
            incident_date=incident_date,
            audience=audience,
            detection_source=detection_source,
            affected_assets=affected_assets,
            incident_summary=incident_summary,
            timeline=timeline,
            log_snippets=log_snippets,
            remediation_steps=remediation_steps,
            known_impact=known_impact,
            lessons_learned=lessons_learned,
            open_questions=open_questions,
        )
        result = ReportService(get_settings()).generate_report(incident)
        error = None
    except Exception as exc:
        # TODO: Week 6 - Replace broad display with user-safe error handling and server logging.
        result = None
        error = str(exc)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "audiences": [style.value for style in AudienceStyle],
            "result": result,
            "error": error,
        },
    )
