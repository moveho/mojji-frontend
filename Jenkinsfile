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
        stage('Stop Local Server') {
            steps {
                // Get the PID of the Python process and stop it
                script {
                    def pid = sh(script: 'pgrep -f "python3 app.py"', returnStdout: true).trim()
                    if (pid) {
                        sh "sudo -S kill ${pid}"
                    } else {
                        echo "Python app is not running."
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    // Install required Python dependencies
                    sh 'pip3 install -r requirements.txt'

                    // Use tmux to run the 'python3 app.py' command in the background
                    sh 'tmux new-session -d -s my_app_session "python3 app.py"'
                }
            }
        }
    }
}

