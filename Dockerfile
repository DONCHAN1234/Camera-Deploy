FROM python:3.12

# Install distutils
RUN apt-get update && apt-get install -y python3-distutils

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
