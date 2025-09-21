# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "weather_app/wf.py", "--server.port=8501", "--server.address=0.0.0.0"]
