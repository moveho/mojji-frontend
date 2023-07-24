pipeline {
    agent any

    stages {
        stage('Stop Local Server') {
            steps {
                sh 'kill $(pgrep -f "python3 app.py")' // Send SIGTERM signal
                script {
                    sleep 1 // Wait for 1 minute for graceful shutdown (1 minute = 1)
                }
                sh 'kill -9 $(pgrep -f "python3 app.py")' // Forcefully terminate if still running
            }
        }

        stage('Deploy') {
            agent {
                label 'your_remote_server_label' // Replace with the label of the remote server agent
            }
            steps {
                dir('/path/to/your/project/directory') { // Replace with the actual path to your project directory on the remote server
                    sh 'pip3 install -r requirements.txt'
                    sh 'nohup python3 app.py > /dev/null 2>&1 &'
                }
            }
        }
    }
}

