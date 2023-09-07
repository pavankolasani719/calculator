pipeline {
    agent any
    
    stages {
        stage('Build and Test') {
            steps {
                script {
                    def imageName = "calculator-app:${env.BUILD_ID}"
                    sh "docker build -t $imageName ."
                    sh "docker run -p 8089:8088 $imageName &"
                    def appRunning = sh(script: 'curl -sSf http://localhost:8089', returnStatus: true)
                    if (appRunning != 0) {
                        error "Application failed to start"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh "docker stop \$(docker ps -q --filter ancestor=calculator-app)"
                    sh "docker run -d -p 8089:8088 calculator-app:${env.BUILD_ID}"
                }
            }
        }
    }
    post {
        always {
            sh "docker stop \$(docker ps -q --filter ancestor=calculator-app)"
        }
    }
}
