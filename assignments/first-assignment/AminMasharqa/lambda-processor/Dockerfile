FROM python:3.11

# Set the working directory
WORKDIR /app=lambda-crud

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the handler script
COPY handler.py .

# Expose port 8000
EXPOSE 8002

# Command to run the FastAPI app
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8002"]
