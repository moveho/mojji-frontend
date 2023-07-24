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
                    if (pid) {
                        sh "sudo -S kill ${pid}"
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

                    // Run the 'python3 app.py' command in the background using '&'
                    sh 'nohup python3 app.py > /dev/null 2>&1 &'
                }
            }
        }
    }
}
