pipeline {
    agent {label 'JAVA'}
    triggers {
        pollSCM('* * * * * ')
    }
    stages {
        stage('git checkout') {
            steps {
                git url: 'https://github.com/Sampathgoud20/spring-petclinic.git' ,
                    branch: 'main'
            }
        }
        stage('build and scan') {
            steps {
                withCredentials([string(credentialsId: 'sonar-id' , variable: 'SONAT_TOKEN')]){
                withSonarQubeEnv('SONAR'){
                sh '''mvn package sonar:sonar \
                -Dsonar.projectkey=Sampathgoud20_spring-petclinic \
                -Dsonar.organization=sampathgoud20 \
                -Dsonar.host.url=https://sonarcloud.io \
                -Dsonar.login=$SONAR_TOKEN'''
            }
          }
    
        }
    }
  }
}