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
                 // Créer un environnement virtuel Python
                    python3 -m venv venv
                    
                    // Activer l'environnement virtuel
                    . venv/bin/activate
                    
                    // Installer les dépendances
                    pip install -r requirements.txt
                    
                    pip3 install flask
                    python3 index.py
                '''
            }
        }
    }
}
