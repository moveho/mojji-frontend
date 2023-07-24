pipeline {
    agent any

    stages {
        stage('change dir') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    // Your steps within this directory
                }
            }
        }
        stage('deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    // Install required Python dependencies
                    sh 'pip3 install -r requirements.txt'
                    sh 'sh cicd.sh &'
                    sleep 30s
                    sh 'kill $(pgrep -f "python3 app.py")'
                }
            }
        }
    }
}

