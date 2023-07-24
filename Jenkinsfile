pipeline {
    agent any

    stages {
        stage('Stop Local Server') {
            steps {
                sh 'sudo pkill -f "python3 app.py"'
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
                }
                // Introduce a sleep of 5 minutes using shell step
                sh 'sleep 5m'
                // After the sleep, stop the Python process on the remote server
                sh 'pkill -f "python3 app.py"'
            }
        }
    }
}

