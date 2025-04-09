pipeline {
    agent any

    stages {
        stage('build') {
            agent {
                docker {
                    image 'python'
                    reuseNode true
                }
            }
            steps {
                sh '''                 
                    pip install flask
                    python3 index.py
                '''
            }
        }
    }
}
