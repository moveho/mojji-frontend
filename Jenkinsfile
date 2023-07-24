pipeline {
    agent any

    stages {
        stage('change dir') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                }
            }
        }
        stage('deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    sh 'python3 app.py'
                }
            }
        }
    }
}

