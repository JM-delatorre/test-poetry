def COLOR_MAP = [
    'SUCCESS': 'good',
    'FAILURE': 'danger',
]

pipeline {

    agent {
      kubernetes {
            defaultContainer 'kubernetes-agent'
            yamlFile "./kubernetes-agent.yaml"
            retries 2
      }
    }

    stages {
      stage('Load project') {

        steps {
          container('kubernetes-agent') {
            script {
            // Read the content of env.groovy file and store it in a variable
            def envFileContent = readFile "./env.groovy"
            // Print the content of the file to Jenkins console
            println "Content of env.groovy:\n${envFileContent}"
            // Load the Groovy script
            load "./env.groovy"
          }
          slackSend channel: "${SLACK_CHANNEL}",
                    color: "warning",
                    message: "*LAUNCHING:* @channel Jenkins is launching into ${ENVIRONMENT} the following job #${env.BUILD_NUMBER} for project *${env.JOB_NAME}* (${env.BUILD_URL}). Please pending changes."
        }
          

        }
      }

      stage('Build artifact') {
        steps {
            script {
                // Build the artifact
                echo "Building the artifact..."
                sh '''
                  pipx ensurepath
                '''
                sh 'pipx install poetry==1.2.0'

                sh 'ls -l'

                sh 'poetry install'

                sh 'poetry self add poetry-plugin-lambda-build'
                    
                sh 'poetry self add poetry-plugin-export'

                sh 'poetry build-lambda'
                sh 'ls -l'
            }
          }
      }

      stage('Deploy artifact') {
        steps {
          script {
            // Deploy the artifact
            echo "Deploying the artifact..."

          }
          withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CREDENTIALS}"]]) {
            
          } 
        }
      }
    }
    // Post-build actions
    post {
        success {
            sh 'echo success'

            slackSend channel: "${SLACK_CHANNEL}",
                      color: COLOR_MAP[currentBuild.currentResult],
                      message: "*${currentBuild.currentResult}:* @channel Jenkins has completed successfully the following job #${env.BUILD_NUMBER} for project *${env.JOB_NAME}* (${env.BUILD_URL}) after ${currentBuild.durationString}. Please test changes in ${ENVIRONMENT}."

        }

        failure {
            sh 'echo failed'

            slackSend channel: "${SLACK_CHANNEL}",
                      color: COLOR_MAP[currentBuild.currentResult],
                      message: "*${currentBuild.currentResult}:* @channel Jenkins has failed to deploy the following job #${env.BUILD_NUMBER} for project *${env.JOB_NAME}* (${env.BUILD_URL}) after ${currentBuild.durationString}. Please check now."

        }
    }

}