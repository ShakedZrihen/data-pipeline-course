# Warm up

As a data engineer, we want to be able to expose our collected data to the users

## Requirement

Build simple web api using python and [Fast-API](https://fastapi.tiangolo.com/tutorial/) that will expose our collected data from ynet

the api should expose the following routes:

1. `/health` - will return 200 if the api is up
2. `/breaking-news` - will return all breaking news in the following format

```json
{
  "date": [{ "hour": "news" }]
}
```

3. `/breaking-news?date=<date>&time=<time>` - will return all breaking news from specific date or time in the following format

for only date:

```json
{
  "hour": "news"
}
```

for only time:

```json
{
  "date": "news in specific time (if exists)"
}
```

for both date and time:

```json
"news in specific date and time (if exists), 404 if not exist"
```

> **_NOTE:_** Please try to avoid using `github copilot` and `chat-gpt` for this task 😇

keep in mind that your code should be as clean as you can and follows the [SOLID](https://realpython.com/solid-principles-python/) principles

### Additional Requirement

The server should run as an AWS Lambda function using the Serverless Framework.

you can read [this](https://pgrzesik.com/posts/fastapi-lambda-serverless/) for help

### Dev requirements

1. handle error correctly
2. add at least 1 unit-test using [pytest](https://docs.pytest.org/en/7.1.x/example/simple.html)
3. follow [SOLID](https://realpython.com/solid-principles-python/) principles

## DoD

In your personal folder should be the code with:

1. `requirement.txt` - All packages needed to run the code.
2. `serverless.yml` - Configuration file for deploying the server as a Lambda function using the Serverless Framework and serverless local [read more about serverless framework](https://www.serverless.com/framework/docs/getting-started).
3. `README.md` - Instructions on how to run the code.
4. Swagger documentation should work under `<server-endpoint>/docs`
