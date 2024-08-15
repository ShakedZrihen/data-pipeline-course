# Warmup exercise 

before we start make sure to run these following commands:
```angular2svg
pip install -r requirements.txt
```
```angular2svg
npm install
```
### to run the server locally run:
```angular2svg
uvicorn app:app
```
### to run serverless locally, run:
```angular2svg
serverless offline start
```
### to run WarmUp unit tests run:
```angular2svg
pytest
```

## API Examples:
1. `/health`
```angular2svg
{
  "message": "Hi I am healthy"
}
```
2. `/breaking-news`
```angular2svg
{
  "2024-07-31": [
    {
      "09:49:35": "Report 1"
    },
    {
      "09:37:33": "Report 2"
    }]
}
```
3. ` /breaking-news?<date>`
```angular2svg
{
  "09:49:35": "Report 1,
  "09:37:33": "Report 2",
  "09:34:14": "Report 3",
  "09:33:16": "Report 4,
}
```
4. ` /breaking-news?<time>`
```angular2svg
{
    "2024-07-31":"Report"
}
```
5` /breaking-news?<date>&<time>`
```angular2svg

    "Report"

```

