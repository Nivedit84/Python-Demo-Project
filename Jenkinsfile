pipeline {
    agent any

    triggers {
        githubPush()  // Trigger pipeline on GitHub push (via webhook)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Nivedit84/Python-Demo-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run Flask App') {
            steps {
                // Stop and remove old container if running
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                
                // Run new container
                sh 'docker run -d --name flask-app -p 5000:5000 my-flask-app'
            }
        }
    }
}

