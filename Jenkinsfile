pipeline {
    agent any

    stages {
        stage('Stop Local Server') {
            steps {
                script {
                    // Get the PID of the Python process
                    def pid = sh(script: 'pgrep -f "python3 app.py"', returnStdout: true).trim()
                    // If the process is running, stop it using sudo
                    if (pid) {
                        sh "sudo kill ${pid}" // Send SIGTERM signal
                        sleep 1 // Wait for 1 second for graceful shutdown
                        sh "sudo kill -9 ${pid}" // Forcefully terminate if still running
                    } else {
                        echo "Python app is not running."
                    }
                }
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

