pipeline {
    agent any

    environment {
        IMAGE_NAME = "healthcare-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Security Scan') {
            steps {
                bat 'security-scan.bat'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build --no-cache -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Load Into Minikube') {
            steps {
                bat "\"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe\" image load %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy Update') {
            steps {
                bat "kubectl set image deployment/healthcare-app healthcare-app=%IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Check Rollout') {
            steps {
                bat "kubectl rollout status deployment/healthcare-app"
            }
        }
    }
}