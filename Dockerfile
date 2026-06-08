FROM python:3.11-slim
WORKDIR /app

# Copy dependency list and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Open port 5000 for web traffic
EXPOSE 5000
CMD ["python", "app.py"]

