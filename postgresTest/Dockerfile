# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /django_admin

# Set the working directory to /django_admin
WORKDIR /django_admin

# Copy the current directory contents into the container at /django_admin
ADD . /django_admin/

# Install any needed packages specified in requirements
RUN pip install -r requirements