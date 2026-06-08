pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'dockerd1new/flask-test-app'
        IMAGE_TAG    = "${BUILD_NUMBER}"
        DOCKER_HUB_CREDS = 'docker-hub-credentials-id'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '🧪 Installing requirements and running unit tests...'
                // Using a local Python environment to test the code logic
                sh 'pip install -r requirements.txt && pytest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Packaging Flask application into Docker image...'
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo '🚀 Uploading image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDS}", passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                    sh "echo ${DOCKER_HUB_PASSWORD} | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up local images...'
            sh "docker rmi -f ${DOCKER_IMAGE}:${IMAGE_TAG} || true"
            sh "docker rmi -f ${DOCKER_IMAGE}:latest || true"
        }
    }
}

