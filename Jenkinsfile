pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    pwd
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
