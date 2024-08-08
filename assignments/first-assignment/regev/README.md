# Shaki Warm-up

1. install python requirements

```bash
pip install -r requirements.txt
```

2. install serverless (node) requirements

```bash
nvm use # to config the specific node version
npm i
```

3. run it as serverless-offline application:

```bash
./node_modules/.bin/serverless offline start
```

or run it as a stand-alone server

```bash
uvicorn app:app --reload
```

commands are available:

1.curl http://127.0.0.1:8000/health
2.curl http://127.0.0.1:8000/breaking-news
3.curl "http://127.0.0.1:8000/breaking-news?date=" ""
4.curl "http://127.0.0.1:8000/breaking-news?time=" ""
5.curl "http://127.0.0.1:8000/breaking-news?date=" "-27&time=" ""
