# ✅ Use python:3.10-slim as the base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from app folder
COPY app/ .

# Default command
CMD ["python", "extract_outline.py"]
