FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# ✅ Set a safe writable directory
WORKDIR /home/user/app

# Copy your project files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port used by Chainlit
EXPOSE 7860

# Launch Chainlit app
CMD ["chainlit", "run", "main.py", "-w", "--port", "7860", "--host", "0.0.0.0"]

