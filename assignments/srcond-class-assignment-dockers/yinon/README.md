
1. build the docker image

```bash
docker build -t test:latest .
```

2. run the docker image

```bash
docker run -p 127.0.0.1:3000:3000 test:latest
```