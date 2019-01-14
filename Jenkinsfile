pipeline {
  agent any
     environment {
       MY_PATH= 'C:\\Users\\felic\\Documents\\DataScience-Master\\1_Semester\\SoftwareEngineering'
     }
  stages {
     stage('Jenkins Test') {
       steps {
         bat 'echo hello world'
       }
       post{
         always {
             echo 'npm environment setup comleted'
         }
       }
     }
      stage('Sonarcloud') {
         steps {
           bat 'C:\\Users\\felic\\Documents\\DataScience-Master\\1_Semester\\SoftwareEngineering\\sonar-scanner-cli-3.2.0.1227-windows\\sonar-scanner-3.2.0.1227-windows\\bin\\sonar-scanner.bat -D"sonar.projectKey=FeliKoenig_pet-project" -D"sonar.organization=felikoenig-github" -D"sonar.sources=." -D"sonar.host.url=https://sonarcloud.io" -D"sonar.login=8ee1d198bcc706a235c922cbd8202cf8db2dcbf8"'
       }
     }
   }
}
