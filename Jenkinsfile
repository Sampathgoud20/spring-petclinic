pipeline {
    agent { label 'JAVA' }
    environment {
        image_name = "nginx"
        tag_name = "1.29"
        ECR_REPO = "612070058498.dkr.ecr.ap-south-1.amazonaws.com/dev/java"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        // stage('git url'){
        //     steps{
        //         sh ''' git clone "https://github.com/Sampathgoud20/spring-petclinic.git" '''
        //     }
        // }
        

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
      stage('Build App') {
         steps {
             sh 'mvn clean package -DskipTests -Dcheckstyle.skip'
           }
     }
      stage("docker image build" ){
        steps{
            sh """ docker image build -t ${image_name}:${tag_name} . """
       }
    }
     
        stage("Trivy Scan") {
            steps {
                sh """
                mkdir -p reports

                echo "Scanning image: ${image_name}:${tag_name}"
                

                # Run scan
                trivy image \
                 --exit-code 0 \
                  --severity HIGH,CRITICAL \
                  -f json \
                  -o reports/trivy-result.json \
                   ${image_name}:${tag_name}

                   if [ -f trivy-json-to-xml.py ]; then
                    python3 trivy-json-to-xml.py
                  else
                    echo "Script missing!"
                fi

                echo "Files in reports:"
                ls -l reports
                """

            }
        }
        stage("trivy scan image push to ecr"){
         steps{
            sh """ aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 612070058498.dkr.ecr.ap-south-1.amazonaws.com && \
        docker tag ${image_name}:${tag_name} 612070058498.dkr.ecr.ap-south-1.amazonaws.com/dev/java:latest
        docker push 612070058498.dkr.ecr.ap-south-1.amazonaws.com/dev/java:latest
        """
      }
    }
     stage('deploy to k8s for dev'){
        steps{
            withCredentials([file[credentialsId : 'eksctl', variable : 'KUBECONGIG']])
            sh ''' kubectl apply -f deployment/. '''
            }
        }
   
   
    
    }
    //  post {
    //    always {
    //      archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
    //      }
    //     }
    

// post {
//         always{
//             archiveArtifacts artifacts: '**/*.jar'
//             junit '**/surefire-reports/*.xml'

//         }
//     }
}