$env:HOST = "0.0.0.0"
$env:PORT = "7860"
$ProjectPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

# Optional: uncomment these two lines when you are ready to use the OpenAI API.
# $env:OPENAI_API_KEY = "replace_with_your_api_key"
# $env:OPENAI_MODEL = "auto"

& $ProjectPython -m uvicorn aar_generator.main:app --host $env:HOST --port $env:PORT
