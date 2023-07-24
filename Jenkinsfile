pipeline {
    agent any

    stages {
        stage('Stop Local Server') {
            steps {
                sh 'pkill -f "python3 app.py"'
            }
        }

        stage('Deploy') {
            agent {
                label 'your_remote_server_label' // Replace with the label of the remote server agent
            }
            steps {
                dir('/var/lib/jenkins/workspace/mojji-deploy/Project') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'nohup python3 app.py > /dev/null 2>&1 &'
                    sleep 5m
                }
            }
        }
    }
}

