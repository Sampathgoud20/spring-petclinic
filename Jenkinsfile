pipeline {
    agent { label 'JAVA' }
    environment {
        image_name=nginx
        tag_name=1.29

    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('git url'){
            steps{
                sh ''' git clone "https://github.com/Sampathgoud20/spring-petclinic.git" '''
            }
        }
        

        // stage('Build & Sonar Scan') {
        //     steps {
        //         withCredentials([
        //             string(credentialsId: 'sonar-id', variable: 'SONAR_TOKEN')
        //         ]) {
        //             withSonarQubeEnv('SONAR') {
        //                 sh '''
        //                 mvn clean package sonar:sonar \
        //                   -Dsonar.projectKey=Sampathgoud20_spring-petclinic \
        //                   -Dsonar.organization=sampathgoud20 \
        //                   -Dsonar.host.url=https://sonarcloud.io \
        //                   -Dsonar.login=$SONAR_TOKEN
        //                 '''
        //             }
        //         }
        //     }
        // }
      stage("docker image build" ){
        steps{
            sh """ docker image build -t ${image_name}:${tag_name} . """
        }
      }
      stage("trivy scan image push to ecr"){
        steps{
            sh """ aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 612070058498.dkr.ecr.ap-south-1.amazonaws.com && \
                   trivy image ${image_name}:${tag_name}  && \
                   docker tag ${image_name}:${tag_name} 612070058498.dkr.ecr.ap-south-1.amazonaws.com/dev/java:latest && \
                   docker push 612070058498.dkr.ecr.ap-south-1.amazonaws.com/dev/java:latest """
        }
      }
    
    }

// post {
//         always{
//             archiveArtifacts artifacts: '**/*.jar'
//             junit '**/surefire-reports/*.xml'

//         }
//     }
}