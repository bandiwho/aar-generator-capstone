from openai import OpenAI

from aar_generator.config import Settings
from aar_generator.prompts import SYSTEM_PROMPT


class LlmClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.last_model_used: str | None = None

    def resolve_model(self, client: OpenAI) -> str:
        configured_model = self.settings.openai_model.strip()
        if configured_model.lower() != "auto":
            return configured_model

        models = client.models.list()
        return models.data[0].id

    def generate(self, prompt: str) -> str:
        if self.settings.mock_llm or not self.settings.openai_api_key:
            return self._mock_report()

        client = OpenAI(api_key=self.settings.openai_api_key)
        model = self.resolve_model(client)
        self.last_model_used = model
        response = client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=prompt,
        )
        return response.output_text

    def _mock_report(self) -> str:
        return """
## Report Summary

This is a mock after-action report generated without calling the OpenAI API. It confirms that the prototype workflow is running.

## Incident Overview

- Incident data was accepted through the prototype form or API.
- The report draft should be reviewed against the submitted timeline, logs, impact notes, and remediation steps.

## Timeline of Events

- Review the submitted incident timeline and confirm that each event has a clear time, action, and outcome.
- Normalize semi-structured timeline entries into readable report bullets before final submission.

## Impact Assessment

- Impact details will be summarized from the user-provided incident notes.
- Unknown impact should remain clearly marked as unknown.

## Evidence and Log Observations

- Log snippets will be summarized without inventing missing context.

## 5 Whys Root Cause Analysis

1. Why did the incident occur? Review the available evidence and identify the most likely initiating event.
2. Why was the issue not prevented? Identify control gaps that allowed the incident to progress.
3. Why was detection delayed? Compare the timeline against monitoring, alerting, and reporting evidence.
4. Why was response limited? Review process ownership, escalation steps, and available response evidence.
5. Why can this happen again? List systemic gaps that should become tracked recommendations.

## Technical Root Cause

The technical root cause should be stated only when supported by evidence from logs, timeline details, and response notes.

## Process and Communication Gaps

- Confirm whether roles, escalation paths, and documentation steps were clear during the response.
- Add reviewer feedback before treating this report as final evidence.

## Remediation Completed

Remediation actions should be listed clearly, grouped by containment, recovery, validation, and follow-up where possible.

## Recommendations and Owners

- Assign each recommendation to an owner.
- Add due dates before final presentation.

## Open Questions

- Which facts require validation from logs, tickets, or stakeholders?

## Lessons Learned

- The prototype can run without model training.
- The next milestone is improving prompt quality and structured output validation.
""".strip()

