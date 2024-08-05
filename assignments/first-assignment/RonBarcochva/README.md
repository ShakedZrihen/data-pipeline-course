1. run the docker compose in the background

```bash
docker-compose up -d
```

2. to see the postgres go to localhost:8080 enter 
```
server: db
username: postgres
password: example
database: postgres
```
3. go to localhost:3001/docs for the crud lambda
4. go to localhost:3002/docs for the scraper lambda
5. to see processor lambda wait some time and then run
```bash
docker logs lambda-processor
```