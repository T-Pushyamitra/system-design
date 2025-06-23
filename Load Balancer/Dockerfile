# Step 1: Use official Python image
FROM python:3.9

# Step 2: Set work directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy source code
COPY . .

# Step 5: Expose FastAPI port
EXPOSE 8000

# Step 6: Run the app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
