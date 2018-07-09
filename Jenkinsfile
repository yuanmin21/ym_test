def CD_1_SSH_ID=env.CD_1_SSH_ID
def SH_1_SSH_ID=env.SH_1_SSH_ID
def CD_2_SSH_ID=env.CD_2_SSH_ID
println CD_1_SSH_ID
println SH_1_SSH_ID
println CD_2_SSH_ID
def Nodelist = [
    [name : CD_1_SSH_ID], 
    [name : SH_1_SSH_ID],
    [name : CD_2_SSH_ID]
]

//Nodelist.each{Node -> println "\r\n Test node is " + "$Node.name"
node('slave1'){
    // Mark the code checkout 'stage'....
    stage('Build and Chekout'){

    // Get some code from a GitHub repository
    //git([url: 'https://github.com/yuanmin21/ym_test.git', branch: 'master'])
    // Mark the code build 'stage'....
    }
    stage('Get the test node info'){

    println CD_1_SSH_ID
    println SH_1_SSH_ID
    println CD_2_SSH_ID
    }
    // Mark the code run 'stage'....
    stage('Test at Multi PC'){
	    parallel (
        fio_cdpc1: {
            echo "hello cdpc1"
            sh script:"ssh $CD_1_SSH_ID 'cd /home/workspace;python3 test.py'"
        },
    
        Marvo_shpc1: {
        
            echo "hello shpc1!"
            sh script:"ssh $SH_1_SSH_ID 'cd /home/workspace;python3 test.py'"
        },

        IOL_cdpc2: {
            echo "hello cdpc2"
            sh script:"ssh $CD_2_SSH_ID 'cd /home/workspace;python3 test.py'"
        }

        )
    }

    //sh script:"ssh root@10.25.132.123 cd /home/workspace;python3 test.py"
    
    
    
    // Run the program
    //sh 'python test.py'

}
