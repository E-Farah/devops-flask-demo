# Step 1: Base image
FROM python:3.9-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy only requirements first (caches Docker layers)
COPY requirements.txt .

# Step 4: Install dependencies (no cache)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the app
COPY . .

# Step 6: Expose Flask port
EXPOSE 5000

# Step 7: Run the app
CMD ["python", "app.py"]