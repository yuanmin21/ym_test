import groovy.xml.*
import static java.util.UUID.randomUUID


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

def testName = "Jenkins"
def numberOfBuild = '1'
//timestamps
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

            sh script: "scp $CD_1_SSH_ID:/home/workspace/logs/*txt ./"
            //sh script: "socat pty,link=./ttyV0,b115200,ispeed=115200,raw,echo=0,waitslave tcp:10.25.132.101:5555"
        
            
            archiveArtifacts artifacts: '*.txt', fingerprint: true   
        },
    
        Marvo_shpc1: {
        
            echo "hello shpc1!"
            //sh script:"ssh $SH_1_SSH_ID 'cd /home/workspace;python3 test.py'"
        },

        IOL_cdpc2: {
            echo "captrue uart log"
          
            //sh script:"ssh $CD_2_SSH_ID 'cd /home/workspace/dfvs/user_case/testcases/;python2.7 test.py -p 10.25.132.101'"
            echo "start fio test"
            
            //sh script:"ssh $CD_2_SSH_ID 'cd /home/workspace;python iolinteract.py /home/cdpc1/iol_interact-9.0b/nvme/manage testcase >/home/workspace/logs/cd2_log.txt'"

            sh script: "scp $CD_2_SSH_ID:/home/workspace//dfvs/user_case/Logs/*log ./"
            sh script: "scp $CD_2_SSH_ID:/home/workspace/dfvs/user_case/testcases/*.log ./"
            archiveArtifacts artifacts: '*.log', fingerprint: true   
        }

        )
    }
    Map builds = ["build_1":'passed', "build_2":'failed']
    Map currentTestResults = [
                  "build_1": collectTestResults('/home/jenkins/workspace/Precommit_Test/×.log')
                ]
    stage("GenerateXML") {
            currentBuild.description = "Test"
            writeFile(file: 'ym_test.xml', text: resultsAsJUnit(currentTestResults))
            sh script: "ls"
             // publish html
            sh script: "pwd"
            archiveArtifacts(artifacts: 'ym_test.xml', excludes: null)
            step([
                  $class: 'JUnitResultArchiver',
                  testResults: '**/ym_test.xml'
                ])
    }

    //sh script:"ssh root@10.25.132.123 cd /home/workspace;python3 test.py"
    
    
    
    // Run the program
    //sh 'python test.py'

}


// Helper functions
def collectTestResults(logFile) {
  // Initialize empty result map
  def resultMap = [:]
  String  testName   = (logFile =~ /(\w*)\.log/)[0][1]
  boolean testPassed = readFile(logFile).contains("=== Test Passed OK ===")
  resultMap << [(testName): testPassed]
  return resultMap
}

@NonCPS
String resultsAsJUnit(def testResults) {
    StringWriter  stringWriter  = new StringWriter()
    MarkupBuilder markupBuilder = new MarkupBuilder(stringWriter)
    // All those delegate calls here are messing up the elegancy of the MarkupBuilder
    // but are needed due to https://issues.jenkins-ci.org/browse/JENKINS-32766
    markupBuilder.testsuites {
        delegate.testsuite(name: "testName", tests: testResults.size(), failures: "1") {
            delegate.testcase(name: "testName", build_number: "1")            
        }
    }  
  return stringWriter.toString()
}
