# Or Bitan Warm-up

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
serverless offline start
```
or run it as a stand-alone server

```bash
fastapi dev app.py      
```

Test - run the following command:
    
```bash
pytest
```