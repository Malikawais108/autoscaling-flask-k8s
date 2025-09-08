# Autoscaling Flask App on Kubernetes

This project demonstrates a Flask web application deployed on Kubernetes with real-time autoscaling using Horizontal Pod Autoscaler (HPA).

## 🔧 Tech Stack
- Python Flask
- Docker
- Kubernetes (Minikube)
- Metrics Server
- HPA (CPU-based scaling)

## 🚀 Features
- Auto-scales pods based on CPU usage
- `/load` endpoint simulates CPU stress
- Metrics Server integration for resource tracking
- Clean CI/CD-ready YAML configs

## 📦 Setup

```bash
# Start Minikube
minikube start

# Enable Metrics Server
kubectl apply -f metrics-server.yaml

# Build Docker image inside Minikube
eval $(minikube docker-env)
docker build -t flask-hpa ./docker

# Deploy app
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml

# Access app
minikube service flask-hpa-service
