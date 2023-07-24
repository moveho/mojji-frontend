pipeline {
    agent any

    stages {
        stage('Stop Local Server') {
            steps {
                script {
                    // Get the PID of the Python process
                    def pid = sh(script: 'pgrep -f "python3 app.py"', returnStdout: true).trim()
                    // If the process is running, stop it using sudo without password prompt
                    if (pid) {
                        sh "echo k8spass# | sudo -S kill ${pid}" // Replace <PASSWORD> with the sudo password
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
                dir('/var/lib/jenkins/workspace/mojji-deploy/Project') { // Replace with the actual path to your project directory on the remote server
                    sh 'pip3 install -r requirements.txt'
                    sh 'nohup python3 app.py > /dev/null 2>&1 &'
                }
            }
        }
    }
}

