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
