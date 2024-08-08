## 1. Install Python Requirements

Open the Terminal and run the following command to install the necessary Python packages:

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
# 3.5 - open a new terminal for step 4.

4. run tests

```bash
pytest ./tests.py
```