pipeline {
    agent {
        docker {
            image 'python:3.11' // Run Python in Docker
        }
    }

    environment {
        GITHUB_REPO = 'https://github.com/Nivedit84/Python-Demo-Project'
        DOCKER_CONTAINER_NAME = 'my_python_app'
        APP_PORT = '5000' // Port your app uses
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: "${GITHUB_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my_python_app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh '''
                    docker stop ${DOCKER_CONTAINER_NAME} || true
                    docker rm ${DOCKER_CONTAINER_NAME} || true
                    '''
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh '''
                    docker run -d --name ${DOCKER_CONTAINER_NAME} -p 5000:${APP_PORT} my_python_app
                    '''
                }
            }
        }
    }
}
