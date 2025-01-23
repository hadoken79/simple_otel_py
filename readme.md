# Opentelemetry integration with python 

This module allows for a simple integration of python code with open telementry.
It assumes you have an opentelemetry collector running. It will pass traces, metrics and logs to the console and the collector.

## Usage

Install with pip:

```python
pip install git+
```
Pass the endpoint of your otlp collector to the constructor. You can then get a tracer, meter or logger.

```python
otlp_endpoint = os.getenv("OTLP_COLLECTOR_ENDPOINT")

# Initialize OpenTelemetry helper
ot_ = OpenTelemetryHelper(name="my.identifier", otlp_collector_endpoint=otlp_endpoint)

# Set up logging, metrics, and tracing
logger = ot_helper.get_logger()
meter = ot_helper.init_metrics()
tracer = ot_helper.init_tracing()
````

