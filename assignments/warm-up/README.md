# Warm up

As a data engineer, we want to be able to expose our collected data to the users

## Requirement

Build simple web api using python and Flask-API that will expose our collected data from ynet

the api should expose the following routes:

1. /health - will return 200 if the api is up
2. /flash - will return all flashes back in the following format

```json
{
    "date": ["hour: flash"]
}
```

3. /flash/date - will return all flashes from specific date in the following format

```json
{
    "hour": "flash"
}
```

> **_NOTE:_**  Please try to avoid using `github copilot` and `chat-gpt` for this task 😇

## DoD

In your personal folder should be the code with:

1. requirement.txt - all packages needed in order to run the code
2. README.md - instruction how i can run the code
3. swagger - with all required routes: [readmore about swagger](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)

