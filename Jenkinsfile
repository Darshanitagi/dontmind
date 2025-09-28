pipeline {
    agent any

    stages {
        stage('Create EC2 Instance') {
            steps {
                script {
                    // Ensure Python and Boto3 are available
                    sh 'pip install boto3'

                    // Execute the Python script
                    sh 'python create_ec2.py'
                }
            }
        }
    }
}
