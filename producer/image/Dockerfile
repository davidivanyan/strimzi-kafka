FROM python:3.11-slim

WORKDIR /app

# Install kafka-python
RUN pip install kafka-python

# Copy producer script
COPY producer.py /app/producer.py

# Default command
CMD ["python", "/app/producer.py"]
