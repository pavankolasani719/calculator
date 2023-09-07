pipeline {
    agent any

    environment {
        // Define the Python executable path
        //PYTHON_EXEC = 'C:\\Users\\PavanKumarKolasani\\AppData\\Local\\Temp\\python.exe'
		//PYTHON_EXEC = 'C:\\Users\\PavanKumarKolasani\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe'
		PYTHON_EXEC = 'C:\\Users\\PavanKumarKolasani\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/pavankolasani719/calculator.git']]])
            }
        }

        stage('Build and Test') {
            steps {
                // Install project dependencies
                bat "${PYTHON_EXEC} -m pip install -r requirements.txt"

                // Run Python tests
                bat "${PYTHON_EXEC} -m unittest discover -s tests -p '*_test.py'"
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                bat 'docker build -t calculator-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Run the Docker container and expose it on port 8089
                bat 'docker run -d -p 8089:8088 calculator-app'
            }
        }
    }

    post {
        always {
            // Clean up Docker containers and images
            bat 'for /f %i in (\'docker ps -q\') do docker stop %i'
            bat 'docker rm $(docker ps -aq)'
            bat 'docker rmi calculator-app'
        }
    }
}
