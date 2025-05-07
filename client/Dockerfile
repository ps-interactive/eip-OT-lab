FROM ubuntu:22.04

# Install Python and dependencies
RUN apt update && apt install -y python3-pip
RUN pip3 install pycomm3

# Copy test script
COPY test_client.py /opt/test_client.py

CMD ["python3", "/opt/test_client.py"]