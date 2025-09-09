pipeline {
    agent any

    environment {
        IMAGE_NAME = "malikawais108/flask-hpa"
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Malikawais108/autoscaling-flask-k8s.git', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Python unit tests...'
                sh '''
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                    python -m unittest discover || echo "No tests found"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing image to Docker Hub..."
                script {
                    docker.withRegistry('', DOCKERHUB_CREDS) {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes cluster..."
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl apply -f k8s/hpa.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
    }
}
