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
                withCredentials([string(credentialsid: 'sonar-id' , variable: 'SONAT-TOKEN')]){
                withoutSonarQubeEnv('SONAR'){
                sh '''muv package sonar:sonar \
                -Dsonar.projectkey=Sampathgoud20_spring-petclinic \
                -Dsonar.organization=sampathgoud20 \
                -Dsonor.host.url=https://sonarcloud.io \
                -Dsonor.login=$SONAR_TOKEN'''
            }
          }
    
        }
    }
  }
}