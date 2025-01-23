# Opentelemetry integration with python 

This module allows for a simple integration of python code with open telementry.
It assumes you have an opentelemetry collector running. It will pass traces, metrics and logs to the console and the collector.

## Usage

Install with pip:

```python
pip install git+https://github.com/hadoken79/opentelemetry_helper.git
```
Pass the endpoint of your otlp collector to the constructor. You can then get a tracer, meter or logger.

```python
import opentelemetry_helper

otlp_endpoint = os.getenv("OTLP_COLLECTOR_ENDPOINT")

# Initialize OpenTelemetry helper
ot_ = opentelemetry_helper(name="my.identifier", otlp_collector_endpoint=otlp_endpoint)

# Set up logging, metrics, and tracing
logger = ot_.get_logger()
meter = ot_.init_metrics()
tracer = ot_.init_tracing()

# start building metrics
email_counter = meter.create_counter("email_count", description="Counts the number of emails sent")

...
email_counter.add(1)

# or traces
@tracer.start_as_current_span("send email")

````

