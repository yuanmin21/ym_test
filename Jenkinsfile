node('slave1'){
    // Mark the code checkout 'stage'....
    stage('Build'){

    // Get some code from a GitHub repository
    git([url: 'https://github.com/yuanmin21/ym_test.git', branch: 'master'])
    // Mark the code build 'stage'....
    }
   
    // Mark the code run 'stage'....
    stage('Test'){
	sh script:"ssh root@10.25.132.123 cd /home/workspace;python3 test.py"

    // Run the program
    sh 'python test.py'
    }
}
