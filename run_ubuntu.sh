#!/usr/bin/env bash
export HOST=0.0.0.0
export PORT=7860

# Optional: uncomment these two lines when you are ready to use the OpenAI API.
# export OPENAI_API_KEY="replace_with_your_api_key"
# export OPENAI_MODEL="auto"

python3 -m uvicorn aar_generator.main:app --reload --host "$HOST" --port "$PORT"
