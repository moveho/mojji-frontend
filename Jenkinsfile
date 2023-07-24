pipeline {
    agent any

    stages {
        stage('change dir') {
            steps {
                dir('/home/ubuntu/environment/Project') {
                }
            }
        }
        stage('deploy') {
            steps {
                dir('/home/ubuntu/environment/Project') {
                    sh 'python3 app.py'
                }
            }
        }
    }
}

