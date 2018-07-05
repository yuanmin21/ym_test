node('slave1'){
    // Mark the code checkout 'stage'....
    stage('Build'){

    // Get some code from a GitHub repository
    git([url: 'https://github.com/oceanchiou/Test.git', branch: 'master'])
    // Mark the code build 'stage'....
    }
   
    // Mark the code run 'stage'....
    stage('Test'){
 
    // Run the program
    sh 'python test.py'
    }
}
