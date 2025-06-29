FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /home/user/app

# Create directories and set permissions
RUN mkdir -p /home/user/app/user_uploads /home/user/app/chat_history /home/user/app/.files \
    && chown -R 1000:1000 /home/user/app \
    && chmod -R u+rwX /home/user/app

# Set environment variable for Chainlit files
ENV CHAINLIT_FILES_DIR=/home/user/app/user_uploads

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port used by Chainlit
EXPOSE 7860

# Launch Chainlit app
CMD ["chainlit", "run", "main.py", "-w", "--port", "7860", "--host", "0.0.0.0"]