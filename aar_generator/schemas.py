from enum import Enum

from pydantic import BaseModel, Field


class AudienceStyle(str, Enum):
    technical = "technical"
    executive = "executive"


class IncidentInput(BaseModel):
    title: str = Field(..., min_length=3, max_length=160)
    incident_type: str = Field(default="")
    incident_date: str = Field(..., min_length=4, max_length=40)
    audience: AudienceStyle = AudienceStyle.technical
    detection_source: str = Field(default="")
    affected_assets: str = Field(default="")
    incident_summary: str = Field(..., min_length=20)
    timeline: str = Field(..., min_length=20)
    log_snippets: str = Field(default="")
    remediation_steps: str = Field(..., min_length=10)
    known_impact: str = Field(default="")
    lessons_learned: str = Field(default="")
    open_questions: str = Field(default="")


class ReportResponse(BaseModel):
    title: str
    audience: AudienceStyle
    model_used: str
    mock_mode: bool
    report_markdown: str

