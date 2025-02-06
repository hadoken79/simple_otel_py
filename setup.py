from setuptools import setup, find_packages

setup(
    name="opentelemetry_helper",
    version="0.1.0",
    description="A helper for OpenTelemetry integration with your existing collector",
    author="Linus Pauls",
    author_email="hadoken79@protonmail.com",
    url="https://github.com/hadoken79/simple_otel_py",
    packages=find_packages(), 
    python_requires=">=3.7",
    install_requires=[
    "opentelemetry-sdk==1.29.0", # check with requirements.txt
    "opentelemetry-api==1.29.0",
    "opentelemetry-instrumentation-logging==0.50b0",
    "opentelemetry-instrumentation-requests==0.50b0",
    "opentelemetry-exporter-richconsole==0.50b0",
    "opentelemetry-exporter-otlp-proto-grpc==1.29.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)