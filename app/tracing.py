import sys
import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

_initialized = False

def setup_tracing():
    global _initialized
    if _initialized:
        return trace.get_tracer(__name__)
    _initialized = True

    sys.stderr.write(">>> [TRACING] setup_tracing() called\n")
    sys.stderr.flush()

    # Create a real SDK TracerProvider
    resource = Resource.create({"service.name": "adk-jaeger-demo"})
    provider = TracerProvider(resource=resource)

    # Console exporter — debug: see spans in terminal
    provider.add_span_processor(
        SimpleSpanProcessor(ConsoleSpanExporter())
    )

    # OTLP HTTP exporter — sends to Jaeger
    provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint="http://localhost:4318/v1/traces"
            )
        )
    )

    # Set as the global provider
    trace.set_tracer_provider(provider)

    current = trace.get_tracer_provider()
    sys.stderr.write(f">>> [TRACING] Provider type: {type(current).__name__}\n")
    sys.stderr.flush()

    return trace.get_tracer(__name__)