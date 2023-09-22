# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 for the Gradio app
EXPOSE 7860

# Run the command to start the Gradio app
# CMD ["python", "app.py]
ENTRYPOINT python app.py