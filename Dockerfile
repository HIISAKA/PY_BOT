# Use Python 3.14 as the base image
FROM python:3.14

# Install system dependencies for voice support and Git
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libffi-dev \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libopus-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /bot

# Clone the GitHub repository
RUN git clone https://github.com/HIISAKA/PY_BOT ./

# Change to the cloned directory (if needed)
# WORKDIR /bot/your_repo  # Uncomment and update if necessary

# Copy the requirements.txt file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script into the container
COPY entrypoint.sh /bot/
RUN chmod +x /bot/entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/bin/bash", "/bot/entrypoint.sh"]