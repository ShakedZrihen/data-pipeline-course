# Warm Up and Docker assignment - Readme:

# Run: Warm up assignment
1. Install Python packages:
pip install fastapi
pip install -r requirements.txt
pip install pytest httpx

2. Set-up serverless framework and plugins:
npm install -g serverless
npm install -g npm 
npm init -y
npm install serverless-python-requirements
npm install serverless-python-requirements --save-dev

3. Run the app:
Locally by - 
uvicorn main:app --reload

Or serverless offline by one of the commands - 
npx serverless offline start
./node_modules/.bin/serverless offline start

4. Perform Unit-Testing by running the command: 
python -m pytest



Testing the API manually:
1. Run the server and go to http://localhost:3000/breaking-news to view all news.
2. Try the following examples:
http://localhost:3000/breaking-news?date=2024-07-30
http://localhost:3000/breaking-news?time=08:00
http://localhost:3000/breaking-news?date=2024-07-30&time=08:00
change manually date and time as desire. 


# Run: Docker for 2nd class assignment 
1. docker build -t kori-image
2. docker run -p 3000:3000 kori-image
3. open explorer and write: http://localhost:3000/breaking-news
