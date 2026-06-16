from openai import OpenAI

from aar_generator.config import Settings
from aar_generator.prompts import SYSTEM_PROMPT


class LlmClient:
    def __init__(self, settings: Settings):
        self.settings = settings

    def generate(self, prompt: str) -> str:
        if self.settings.mock_llm or not self.settings.openai_api_key:
            return self._mock_report()

        client = OpenAI(api_key=self.settings.openai_api_key)
        response = client.responses.create(
            model=self.settings.openai_model,
            instructions=SYSTEM_PROMPT,
            input=prompt,
        )
        return response.output_text

    def _mock_report(self) -> str:
        # TODO: Week 7 - Replace this with multiple realistic demo incident fixtures.
        return """
## Executive Summary

This is a mock after-action report generated without calling the OpenAI API. It confirms that the prototype workflow is running.

## Incident Overview

- Incident data was accepted through the prototype form or API.
- The final version will generate this section from pasted timelines, logs, impact notes, and remediation steps.

## Timeline of Events

- TODO: Week 2 - Confirm the timeline input format the team wants to support.
- TODO: Week 4 - Normalize semi-structured timeline entries into consistent report bullets.

## Impact Assessment

- Impact details will be summarized from the user-provided incident notes.
- Unknown impact should remain clearly marked as unknown.

## Evidence and Log Observations

- Log snippets will be summarized without inventing missing context.

## 5 Whys Root Cause Analysis

1. Why did the incident occur? TODO: Derive from evidence.
2. Why was the issue not prevented? TODO: Identify control gaps.
3. Why was detection delayed? TODO: Compare timeline and monitoring.
4. Why was response limited? TODO: Review process and ownership.
5. Why can this happen again? TODO: List systemic gaps.

## Technical Root Cause

TODO: Week 3 - Improve prompt logic for technical root cause extraction.

## Process and Communication Gaps

TODO: Week 5 - Add reviewer feedback and revision support.

## Remediation Completed

TODO: Week 6 - Add export-ready formatting for final report delivery.

## Recommendations and Owners

- Assign each recommendation to an owner.
- Add due dates before final presentation.

## Open Questions

- Which facts require validation from logs, tickets, or stakeholders?

## Lessons Learned

- The prototype can run without model training.
- The next milestone is improving prompt quality and structured output validation.
""".strip()

