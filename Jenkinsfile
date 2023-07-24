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

                    // Run the 'python3 app.py' command
                    sh 'python3 app.py'
                }
            }
        }
    }
}

