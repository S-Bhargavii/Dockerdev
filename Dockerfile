FROM ubuntu:focal 
WORKDIR /workspace/repo
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    eog\
    && pip3 install matplotlib\
    && apt-get clean

# CMD ["bash","-c","python3 program1.py && eog plot.png"]