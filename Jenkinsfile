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
        stage('deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/mojji-pipeline/Project') {
                    sh 'pip3 install -r requirements.txt'

                    // Use 'su' and 'nohup' to run the 'python3 app.py' command as the ubuntu user
                    sh 'sudo -u ubuntu python3 /home/ubuntu/environment/Project/app.py > app.log 2>&1 &'
                }
            }
        }
    }
}

