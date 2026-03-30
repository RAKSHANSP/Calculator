pipeline {
    agent any

    tools {
        sonarScanner 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RAKSHANSP/Calculator.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    bat 'sonar-scanner'
                }
            }
        }
    }
}
