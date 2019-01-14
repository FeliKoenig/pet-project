pipeline {
  agent any
     environment {
     }
  stages {
     stage('Jenkins Test') {
       steps {
         bat 'python --version'
       }
       post{
         always {
             echo 'npm environment setup comleted'
         }
       }

     }
   }
}
