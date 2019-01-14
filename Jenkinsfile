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
   }
}
