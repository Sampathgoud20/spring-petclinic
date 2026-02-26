pipeline {
    agent { label 'JAVA' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Sonar Scan') {
            steps {
                withCredentials([
                    string(credentialsId: 'sonar-id', variable: 'SONAR_TOKEN')
                ]) {
                    withSonarQubeEnv('SONAR') {
                        sh '''
                        mvn clean package sonar:sonar \
                          -Dsonar.projectKey=Sampathgoud20_spring-petclinic \
                          -Dsonar.organization=sampathgoud20 \
                          -Dsonar.host.url=https://sonarcloud.io \
                          -Dsonar.login=$SONAR_TOKEN
                        '''
                    }
                }
            }
        }
    }

post {
        always{
            archiveArtifacts artifacts: '**/*.jar'
            junit '**/surefire-reports/*.xml'

        }
    }
}