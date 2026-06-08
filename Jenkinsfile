pipeline {
    agent any

    environment {

        DOCKER_IMAGE = 'dockerd1new/flask-test-app'
        DOCKER_HUB_CREDS = 'docker-hub-credentials-id'
    }

    stages {
        stage('Part 1: Compile & Package') {
            steps {
                cleanWs() 
                
                echo 'Pulling fresh codebase copy from GitHub...'
                checkout scm

                echo 'Executing application python testing layers...'
                sh 'pip install --no-cache-dir --break-system-packages -r requirements.txt && pytest test_app.py'

                echo 'Building image with a secure static format...'
                
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Part 2: Authenticate & Deploy') {
            steps {
                echo '🚀 Pushing the confirmed static image up to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: "${DOCKER_HUB_CREDS}", 
                    passwordVariable: 'DOCKER_HUB_PASSWORD', 
                    usernameVariable: 'DOCKER_HUB_USERNAME'
                )]) {
                    sh "echo \$DOCKER_HUB_PASSWORD | docker login -u \$DOCKER_HUB_USERNAME --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }

    post {
        always {
            cleanWs() 
        }
        success {
            echo '✅ Pipeline Automation Complete! Your updated app is now live on Docker Hub.'
        }
        failure {
            echo '❌ Pipeline Execution Failed. Review the terminal execution details above to debug.'
        }
    }
}

