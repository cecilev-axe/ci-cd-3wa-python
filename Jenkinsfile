pipeline {
    agent any

    stages {
        stage('build') {
            agent {
                docker {
                    image 'docker'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    pip3 install flask
                    python3 index.py
                '''
            }
        }
    }
}
