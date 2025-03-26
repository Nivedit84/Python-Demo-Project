pipeline {
    agent {
        docker {
            image 'python:3.11' // Use Python Docker image for building
        }
    }

    environment {
        GITHUB_REPO = 'https://github.com/Nivedit84/Python-Demo-Project'
        DOCKER_CONTAINER_NAME = 'my_python_app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: "${GITHUB_REPO}"
            }
        }

        stage('Create Docker Image') {
            steps {
                sh 'docker build -t my_python_app .' // Build Docker image
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

        stage('Deploy to EC2') {
            steps {
                script {
                    sh '''
                    docker run -d --name ${DOCKER_CONTAINER_NAME} -p 5000:5000 my_python_app
                    '''
                }
            }
        }
    }
}
