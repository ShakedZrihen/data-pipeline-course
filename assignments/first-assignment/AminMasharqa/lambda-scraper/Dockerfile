FROM python:3.11-slim

# Set the working directory to the correct folder
WORKDIR /app=lambda-scraper

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the handler script
COPY handler.py .

# Expose the port FastAPI will run on
EXPOSE 8003

# Command to run the FastAPI app
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8003"]
