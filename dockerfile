FROM python:3.9


COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

WORKDIR /app

# Expose the port the app runs on
EXPOSE 8000



CMD [ "uvicorn", "app:app",  "--host", "0.0.0.0", "--port", "8000"]