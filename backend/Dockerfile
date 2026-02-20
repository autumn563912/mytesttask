FROM debian:13.3
RUN apt-get update && \
    apt-get install python3.13 -yq --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN groupadd --gid 2000 workgroup && \
    useradd --uid 2000 --gid workgroup --shell /bin/bash --create-home backend
USER backend
WORKDIR /home/backend
COPY app.py .
EXPOSE 8080
HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost:8080 || exit 1
ENTRYPOINT ["python3.13", "app.py"]
