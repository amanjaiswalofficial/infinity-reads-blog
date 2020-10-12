# Build an image starting with the Python 3.7 image
FROM python:3.7-alpine

# Set the working directory to /blog/infinity-reads-blog
WORKDIR /usr/blog/infinity-reads-blog/

# Set the environment variables used by flask
ENV FLASK_APP=app

# Set the flask host
ENV FLASK_RUN_HOST=0.0.0.0

# Copy the requirements.txt to /usr/blog/infinity-reads-blog/
COPY ./requirements.txt /usr/blog/infinity-reads-blog/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port
EXPOSE 5000

# run the command to start the app
CMD ["flask", "run"]
