pipeline {
agent any

environment {
SSH_CRED_ID = 'your-ssh-credential-id' // Jenkins Credential ID
EC2_IP = 'your-ec2-public-ip'
PROJECT_DIR = '/home/ec2-user/my-python-app'
}

stages {
stage('Clone Repository') {
steps {
git branch: 'main', url: 'git@github.com:your-username/your-repo.git'
}
}

stage('Install Dependencies') {
steps {
sh 'pip3 install -r requirements.txt'
}
}

stage('Deploy to EC2') {
steps {
sshagent(credentials: [SSH_CRED_ID]) {
sh """
ssh -o StrictHostKeyChecking=no ec2-user@${EC2_IP} << 'EOF'
# Stop running app if exists
pkill -f my_app.py || true
# Remove old files
rm -rf ${PROJECT_DIR}
# Create project directory
mkdir -p ${PROJECT_DIR}
exit
EOF
"""
// Copy new files to EC2
sh """
scp -o StrictHostKeyChecking=no -r * ec2-user@${EC2_IP}:${PROJECT_DIR}/
"""
// Restart the application
sh """
ssh -o StrictHostKeyChecking=no ec2-user@${EC2_IP} << 'EOF'
# Start the application
nohup python3 ${PROJECT_DIR}/my_app.py > app.log 2>&1 &
exit
EOF
"""
}
}
}
}
}
