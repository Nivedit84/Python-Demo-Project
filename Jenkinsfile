pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    
    environment {
        DOCKER_CONTAINER_NAME = 'python-app'
        DOCKER_IMAGE = 'my-python-app'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Nivedit84/Python-Demo-Project.git'
            }
        }

    stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE .
                '''
            }
        }

    stage('Run Docker Container') {
            steps {
                sh '''
                docker stop $DOCKER_CONTAINER_NAME || true
                docker rm $DOCKER_CONTAINER_NAME || true
                docker run -d --name $DOCKER_CONTAINER_NAME -p 5000:5000 $DOCKER_IMAGE
                '''
            }
        }
    }
}
