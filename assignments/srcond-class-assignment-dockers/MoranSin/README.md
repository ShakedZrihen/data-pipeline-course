# Moran's Warm-up

1. build docker's image with latest updates

```bash
docker build -t second-class-pipelines:latest .
```

2. run the docker image locally

```bash
docker run -p 127.0.0.1:8000:8000 second-class-pipelines:latest .
```