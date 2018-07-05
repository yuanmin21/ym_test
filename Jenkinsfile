node{
    // Mark the code checkout 'stage'....
    stage('Build'){

    // Get some code from a GitHub repository
    git([url: 'https://github.com/oceanchiou/Test.git', branch: 'master'])
    // Mark the code build 'stage'....
    }
   
    // Mark the code run 'stage'....
    stage('Test'){
	node('slave1') 
    // Run the program
    sh 'python test.py'
    }
}
