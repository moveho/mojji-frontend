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
                // Get the PID of the Python process
                script {
                    def pid = sh(script: 'pgrep -f "python3 app.py"', returnStdout: true).trim()
                    // If the process is running, stop it using sudo without password prompt
                    if (pid) {
                        sh sudo -S kill ${pid}" // Replace <PASSWORD> with the sudo password
                    } else {
                        echo "Python app is not running."
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    // Install required Python dependencies
                    sh 'pip3 install -r requirements.txt'

                    // Run the 'python3 app.py' command in the background
                    sh 'nohup python3 app.py > /dev/null 2>&1 &'
                }
            }
        }
    }
}

