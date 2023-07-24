pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Add build steps here if needed
            }
        }
        stage('Test') {
            steps {
                // Add test steps here if needed
            }
        }
        stage('Deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'sh cicd.sh &'
                    sleep 5m
                    sh 'kill $(pgrep -f "python3 app.py")'
                }
            }
        }
    }
    post {
        always {
            // Clean up any resources if needed
        }
    }
}

