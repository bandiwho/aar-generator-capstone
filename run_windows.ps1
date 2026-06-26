$env:HOST = "0.0.0.0"
$env:PORT = "7860"

# Optional: uncomment these two lines when you are ready to use the OpenAI API.
# $env:OPENAI_API_KEY = "replace_with_your_api_key"
# $env:OPENAI_MODEL = "auto"

python -m uvicorn aar_generator.main:app --reload --host $env:HOST --port $env:PORT
