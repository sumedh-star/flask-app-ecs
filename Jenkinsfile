pipeline {
    agent any

    stages {
        stage("code clone") {
            steps {
                git url : "https://github.com/sumedh-star/flask-app-ecs.git" , branch : "main"
                echo "code clone successfully"
            }
        }
        stage ("build"){
            steps {
               sh "docker build -t red:latest ."
               echo "docker build successfully"
            }
        }
        stage ("deploy"){
            steps{
                sh "docker run -d -p 80:80 red"
                echo "application deployed successfully"
            }
        }
        
    }
}
