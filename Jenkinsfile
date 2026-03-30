pipeline {
    agent any

    environment {
        SONARQUBE = 'My Sonar Server'
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/RAKSHANSP/Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building project..."
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    bat """
                    sonar-scanner ^
                    -Dsonar.projectKey=calculator ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }

    }
}
