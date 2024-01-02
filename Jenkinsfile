pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
                DOCKER_CERT_PATH='/tmp'
	}

	stages {
                stage('Pull GitHub repos'){
                    steps{
                    git branch: 'main', url: 'https://github.com/Khaq0312/Devops_project.git'
                    }
                }
		// stage('Login') {

		// 	steps {
		// 		sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
		// 	}
		// }
		stage('Build') {

			steps {
				sh 'docker build -t hmkhang/jenkins .'
			}
		}
		
		
		stage('View Images') {

			steps {
				sh 'docker images'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push hmkhang/jenkins'
			}
		}
		
		stage('Remove current container if it exists') {

			steps {
				sh 'docker rm -f jenkins-mmt || true'
			}
		}
		
		stage('Run in Container') {

			steps {
				sh 'docker run --publish 3000:3000 --name jenkins-mmt -d --rm hmkhang/jenkins:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
