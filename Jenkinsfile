pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'calculator:latest'
        PYTHON_EXEC = 'python'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                bat label: 'Install Python Dependencies', script: "${PYTHON_EXEC} -m pip install -r requirements.txt"
                bat label: 'Run Tests', script: "${PYTHON_EXEC} manage.py test"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat label: 'Build Docker Image', script: "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def dockerRunCmd = "docker run -p 8089:80 -d ${DOCKER_IMAGE}"
                    bat label: 'Run Docker Container', script: dockerRunCmd
                    echo "Docker container is running."
                }
            }
        }
    }

    post {
        always {
            bat label: 'Stop All Docker Containers', script: 'docker stop $(docker ps -q)'
        }
    }
}
