FROM ubuntu:22.04

# Install dependencies
RUN apt update && apt install -y \
    git build-essential cmake python3-pip \
    libmodbus-dev libpcap-dev wget curl

# Clone and build OpenPLC
RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git /opt/openplc && \
    cd /opt/openplc && \
    ./install.sh

# Copy the PLC program into the OpenPLC programs directory
COPY traffic_lights.st /opt/openplc/webserver/st_files/traffic_lights.st

# Set the traffic_lights.st as the active program
RUN cd /opt/openplc/webserver && \
    python3 manage.py shell -c "\
import plc; \
plc.compile_st_program('traffic_lights.st'); \
plc.set_active_program('traffic_lights.st')"

# Expose necessary ports
EXPOSE 44818 502

# Set entrypoint
ENTRYPOINT ["/opt/openplc/start_openplc.sh"]