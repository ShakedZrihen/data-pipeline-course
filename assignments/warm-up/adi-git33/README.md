# Adi's warm-up assignment

1. install python requirements

```bash
pip install -r requirements.txt
```

2. install serverless (node) requirements

```bash
npm install
```

3. run it as serverless-offline application:

```bash
./node_modules/.bin/serverless offline start
```

or run it as a stand-alone server

```bash
uvicorn app:app --reload --port 8000
```

4. for tests (using the fasapi localhost url, checking on serverless requires a changing the port to 3000)

```bash
cd tests
pytest breaking_news_test.py
```

