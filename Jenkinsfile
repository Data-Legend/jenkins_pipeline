pipeline{
    agent any
    environment{
        VENV = 'venv'
        DOCKER_IMAGE = 'flask-hello-app'
        DOCKER_CONTAINER = 'flask-hello-container'
    }
    stages{
        stage('Checkout Out'){
            steps{
                git branch: 'main', url: 'https://github.com/Data-Legend/jenkins_pipeline.git'
            }
        }
        stage('Set up VENV'){
            steps{
                sh 'python3 -m venv venv'
                sh 'venv/bin/python -m pip install --upgrade pip'
                sh 'venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Run the tests'){
            steps{
                sh 'venv/bin/python -m pytest test_app.py -v'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t ${DOCKER_IMAGE}:latest .'
            }
        }
        stage('Deploy Container'){
            steps{
                sh 'docker rm -f ${DOCKER_CONTAINER} || true'
                sh 'docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}:latest'
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully! App is running at http://localhost:5000'
        }
        failure{
            echo 'Pipeline failed. Check the logs above for details.'
        }
    }
}
