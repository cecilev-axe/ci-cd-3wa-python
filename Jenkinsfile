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
                    pip install --user flask
                    python3 index.py
                '''
            }
        }
    }
}
