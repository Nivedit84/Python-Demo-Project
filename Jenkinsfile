node {
    stage('Clone Repository') {
        git branch: 'main', url: 'https://github.com/Nivedit84/Python-Demo-Project.git'
    }

    stage('Run Inside Docker') {
        docker.image('python:3.9').inside {
            sh '''
            pip install -r requirements.txt
            python -m unittest discover
            '''
        }
    }

    stage('Build Docker Image') {
        sh '''
        docker build -t my-python-app .
        '''
    }

    stage('Run Docker Container') {
        sh '''
        docker stop python-app || true
        docker rm python-app || true
        docker run -d --name python-app -p 5000:5000 my-python-app
        '''
    }
}
