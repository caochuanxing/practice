Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.7.2' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
