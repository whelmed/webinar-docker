# Cloud Academy

## [Docker & Container Engine - Webinar](https://cloudacademy.com/webinars/docker-google-container-engine-21/)



To get up and running, you'll need to install the dependencies
This is a Flask, Python based application. So I recommend using virtualenv.

> ` > cd app`

> ` > pip install -t lib -r requirements.txt`

Also, the project name that is in the \*-file.yaml files will need to be edited to reflect your Google Cloud Platform project name.

The commands to follow along with the webinar are:

~~~~
# The directory...
cd PROJECT

# To Build
docker build -t webinar-flask:v2 .

# To Run -d = Daemon -p binds container port to host port then the tag name
docker run -d -p 5000:5000 webinar-flask

# Docker compose
docker-compose up web

# Rebuild
docker-compose up web --build

# Build for GKE with grc.io route
docker build -t gcr.io/ca-webinar/webinar-flask:v1 .

# First we need to push the container image to our GKE repo
gcloud docker push gcr.io/ca-webinar/webinar-flask:v1

# Set our zone
gcloud config set compute/zone us-central1-a
# Create the cluster
gcloud container clusters create webinar-cluster
# Get the credentials
gcloud container clusters get-credentials webinar-cluster


# Kubernetes - Create replication controller.
# Think of it kind of like an auto-scaling group.
kubectl create -f rc-file.yaml

# Kubernetes - Create A service. The LoadBalancer flag is important.
kubectl create -f service-file.yaml

# This can take a few minutes, get the public IP
kubectl get services webinar-service

# Delete this stuff
kubectl delete service webinar-service && kubectl delete rc webinar-flask-rc

# Show the replication controllers
kubectl get rc

# Update the RC.
kubectl rolling-update webinar-flask-rc --filename rc-fileV8.yaml

# Work with the local UI.
kubectl proxy



# Docker stop and remove all
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
~~~~
