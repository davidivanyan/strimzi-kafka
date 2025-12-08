import os
import json
import time
import random
from kafka import KafkaProducer

TOPIC = os.getenv("KAFKA_TOPIC", "default-topic")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka-kafka-bootstrap:9093")

CERT_DIR = "/certs"
CA = f"{CERT_DIR}/ca.crt"
CERT = f"{CERT_DIR}/user.crt"
KEY = f"{CERT_DIR}/user.key"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    security_protocol="SSL",
    ssl_cafile=CA,
    ssl_certfile=CERT,
    ssl_keyfile=KEY,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print(f"Producing messages to topic: {TOPIC}")

while True:
    message = {
        "id": random.randint(1, 999999),
        "value": random.random(),
        "timestamp": time.time()
    }

    producer.send(TOPIC, message)
    producer.flush()
    print("Sent:", message)
    time.sleep(1)
