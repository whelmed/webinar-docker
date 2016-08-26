# This is base image we're going to use to build our app.
# If we don't have it locally, it goes out to the trusted Docker registry
# and downloads it.
FROM ubuntu:latest

# Adds a new layer that will update apt
RUN apt-get update -y

# Adds a new layer that will add in all the python libs
RUN apt-get install -y python-pip python-dev build-essential

# We want to bring our code into the image
COPY ./app /app

# The WORKDIR instruction sets the working directory for any
# RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow
WORKDIR /app

# Install any Python dependencies.
RUN pip install -r requirements.txt

# Change the entrypoint from /bin/sh to python.
# Allowing any commands to be python scripts.
ENTRYPOINT ["python"]

# The python script to run.
# This really should be run behind in a WSGI container of some sort.
# However, this is fine for a Webinar.
CMD ["app.py"]
