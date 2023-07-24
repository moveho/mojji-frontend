pipeline {
    agent any

    stages {
        stage('change dir') {
            steps {
	        cd /home/ubuntu/environment/Project
            }
        }
        stage('deploy') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}

