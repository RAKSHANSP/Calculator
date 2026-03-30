pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo "Building project..."
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('My Sonar Server') {
                        bat """
                        ${scannerHome}\\bin\\sonar-scanner.bat ^
                        -Dsonar.projectKey=calculator ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=http://localhost:9000
                        """
                    }
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
