cd ai_labs

conda activate myenv
cd /Users/bhupeshthakur/PythonProject/ai_labs

# Clear stale cache
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null

# Set OTEL env vars — ADK's runner will use these automatically
export OTEL_SERVICE_NAME="adk-jaeger-demo"
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://localhost:4318/v1/traces"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"

adk web .