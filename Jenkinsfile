import groovy.xml.*
import static java.util.UUID.randomUUID

println JENKINS_HOME
println JOB_NAME
println JOB_BASE_NAME



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

//def testName = "Jenkins"
//def numberOfBuild = '1'

def buildCases = [
    // Precommit
    "Build": [passedParser: this.&jsonTypePassedParser]
    
]
def testCases = [
    // Precommit
    "IOL_cdpc1": [passedParser: this.&jsonTypePassedParser],
    "Marvo_shpc1": [passedParser: this.&jsonTypePassedParser],
    "FIO_cdpc2": [passedParser: this.&jsonTypePassedParser]
]
def buildcases = ["Build"]

def testcases = ["IOL_cdpc1","Marvo_shpc1","FIO_cdpc2"]

timestamps{
//Nodelist.each{Node -> println "\r\n Test node is " + "$Node.name"
node('slave1'){
    // Mark the code checkout 'stage'....
    String copyPath = WORKSPACE
    stage('Build'){
        WORKSPACE
        writeFile(file: 'Test/1098R20_SDK_sdk_nvme_ramdrive_debug.log', text: "Test")
        writeFile(file: 'Test/ASIC_NVME_Ramdisk_0.log', text: "Test")
        writeFile(file: 'Test/C1_ATCM.log', text: "Test")
        def results = [:]
            buildcases.each { test ->
                println test
                def settings = buildCases[test]
                
                sh script: "mkdir -p testlogs/${test}"
                sh script: "tar -zPcv -f ${test}.tar.gz Test/*.log"
                //archiveArtifacts(artifacts: "${test}.tar.gz", excludes: null)
                sh script: "python2.7 checkfile.py"
                
                //Map currentTestResults = [ "Build": BuildStagePassedParser()]
                Map currentTestResults = [
                    (test): collectTestResults(                    
                        test,
                        settings.passedParser
                        )
                    ]
                results << currentTestResults    
            
                writeFile(file: 'ym_test.xml', text: resultsAsJUnit(currentTestResults))
                //Generate the Junit Report 
                //archiveArtifacts(artifacts: 'ocean_test.xml', excludes: null)
                step([
                    $class: 'JUnitResultArchiver',
                    testResults: '**/ym_test.xml'
                    ])
            }
            //Publish the Table      
            currentBuild.description = "<br /></strong>${resultsAsTable(results)}"
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
            
        IOL_cdpc1: {
            echo "hello cdpc1"
            sh script:"ssh $CD_1_SSH_ID 'cd /home/workspace;python3 test.py'"
            sh script: "mkdir -p testlogs/IOL_cdpc1"
            sh script: "scp $CD_1_SSH_ID:/home/workspace/Logs/*.log ./testlogs/IOL_cdpc1"
            
            //sh script: "ssh $CD_1_SSH_ID 'rm -rf /home/workspace/Logs/*.log'"
            //sh script: "scp $CD_2_SSH_ID:/home/workspace/FIO/fw_log.log ./testlogs/${test}"
            
            //archiveArtifacts artifacts: '*.txt', fingerprint: true   
        },
    
        Marvo_shpc1: {
        
            echo "hello shpc1!"
            
            sh script:"ssh $CD_1_SSH_ID 'cd /home/workspace;python3 test.py'"
            sh script: "mkdir -p testlogs/IOL_cdpc1"
            sh script: "scp $CD_1_SSH_ID:/home/workspace/Logs/*.log ./testlogs/IOL_cdpc1"
            //sh script:"ssh $SH_1_SSH_ID 'cd /home/workspace;python3 test.py'"
        },

        FIO_cdpc2: {
            echo "captrue uart log"
        
            //sh script:"ssh $CD_2_SSH_ID 'cd /home/workspace/FIO;python2.7 FIO_test.py -p 10.25.132.101'"
            echo "start fio test"
            sh script: "mkdir -p testlogs/FIO_cdpc2"
            sh script: "scp $CD_2_SSH_ID:/home/workspace/Logs/*.log ./testlogs/FIO_cdpc2"
            sh script: "scp $CD_2_SSH_ID:/home/workspace/FIO/fw_log.log ./testlogs/FIO_cdpc2"
            //sh script: "ssh $CD_2_SSH_ID 'rm -rf /home/workspace/Logs/*.log'"
            //sh script:"ssh $CD_2_SSH_ID 'cd /home/workspace;python iolinteract.py /home/cdpc1/iol_interact-9.0b/nvme/manage testcase >/home/workspace/logs/cd2_log.txt'"
        } 
        )   
        def results = [:]
                //sh "rm -rf *.log"
                //sh script: "ls /home/jenkins/workspace/Precommit_Test/*.log"
        testcases.each { test ->
            println test
            def settings = testCases[test]
                    
                        //sh script: "mkdir -p testlogs/${test}"
                        //sh script: "scp $CD_2_SSH_ID:/home/workspace/Logs/*.log ./testlogs/${test}"
                        //sh script: "scp $CD_2_SSH_ID:/home/workspace/FIO/fw_log.log ./testlogs/${test}"
                        //archiveArtifacts artifacts: '*.log', fingerprint: true   
                    
            sh script: "tar -zPcv -f ${test}.tar.gz testlogs/${test}/*.log"
                          
                
                //String copyPath = WORKSPACE
                
                //Map currentTestResults = [ "Test": regressionPassedParser()]    
                //Map currentTestResults = [ "Build": BuildStagePassedParser()]
            Map currentTestResults = [
                (test): collectTestResults(                    
                    test,
                    settings.passedParser
                    )
                ]
                results << currentTestResults   
                writeFile(file: 'ym_test.xml', text: resultsAsJUnit(currentTestResults))
                //Generate the Junit Report 
                //archiveArtifacts(artifacts: 'ocean_test.xml', excludes: null)
                step([
                    $class: 'JUnitResultArchiver',
                    testResults: '**/ym_test.xml'
                    ])

                }
                currentBuild.description = currentBuild.description + "<br /></strong>${resultsAsTable(results)}"
        
        
    }



}
}



// Helper functions
def collectTestResults(String test, Closure passedParser) {
    // Initialize empty result map
    def resultMap = [:]

    // Gather all the logfiles produced
    String copyPath = WORKSPACE
    def logFiles = sh (
            script: "ls " + copyPath + "/testlogs/${test}/*summary.log",
            returnStdout:true
            ).readLines()

    // Extract the test name and result from each logfile    
    logFiles.each { logFile ->
        passedParser(logFile, resultMap)
    }
    // Store the zips as a tar file
    archiveArtifacts artifacts: "${test}.tar.gz", allowEmptyArchive: true

    // Cleanup
    sh "rm -rf testlogs/${test} ${test}.tar.gz"

    // Return the accumulated result
    return resultMap
}

// Parser for regression test results
def regressionPassedParser() {   
    String  testName
    boolean testPassed 
    def resultMap = [:]
    def logFiles = sh (
            script: "ls /home/jenkins/workspace/Precommit_Test/summary.log",
            returnStdout:true
            ).readLines()
    
    logFiles.each{ logFile -> 
        readFile(logFile).split("\n").each { line ->
            //println line
            //testName   = (logFile =~ /(\w*)\.log/)[0][1]
            testName = line.subSequence(0,line.lastIndexOf(":"))   
            //println testName
            //currentTestSet = RegexSupport.lastMatcher[0][1]
            //println currentTestSet 
            testPassed = line.contains("PASS")
            resultMap << [(testName): testPassed]
            println resultMap
        }
    }
    return resultMap  
  
}

// Parser for regression test results
def jsonTypePassedParser(logFile, resultMap) {   
    String  testName
    boolean testPassed 
    readFile(logFile).split("\n").each { line ->
        testName = line.subSequence(0,line.lastIndexOf(":"))   
        testPassed = line.contains("PASS")
        resultMap << [(testName): testPassed]
        println resultMap
    }    
    return resultMap  
}

def logParser(logFile) {
  // Initialize empty result map
  def logMap = [:]
  String  testName = (logFile =~ /(\w*)\.log/)[0][1]
  logMap << [(testName): logFile]
  return logMap
}

@NonCPS
String resultsAsTable(def testResults) {
  StringWriter  stringWriter  = new StringWriter()
  MarkupBuilder markupBuilder = new MarkupBuilder(stringWriter)

  // All those delegate calls here are messing up the elegancy of the MarkupBuilder
  // but are needed due to https://issues.jenkins-ci.org/browse/JENKINS-32766
  markupBuilder.html {
    delegate.body {
      delegate.style(".passed { color: #468847; background-color: #dff0d8; border-color: #d6e9c6; } .failed { color: #b94a48; background-color: #f2dede; border-color: #eed3d7; }", type: 'text/css')
      delegate.table {
        testResults.each { test, testResult ->
            delegate.delegate.tr {
                        delegate.td {
                            delegate.strong("[Stage] $test ")
                            //delegate.strong("$test")
                            delegate.a("$test Logs", href: "${env.BUILD_URL}/artifact/" + "${test}.tar.gz")
                        }
                    }
            testResult.each { testName, testPassed ->
            delegate.delegate.delegate.tr {
              delegate.td("$testName", class: testPassed ? 'passed' : 'failed')
            }
          }
        }
      }
    }
  }

  return stringWriter.toString()
}



@NonCPS
String resultsAsJUnit(def testResults) {
    StringWriter  stringWriter  = new StringWriter()
    MarkupBuilder markupBuilder = new MarkupBuilder(stringWriter)
    // All those delegate calls here are messing up the elegancy of the MarkupBuilder
    // but are needed due to https://issues.jenkins-ci.org/browse/JENKINS-32766
    markupBuilder.testsuites {
        testResults.each{ test, testresult ->
            delegate.delegate.testsuite(name: testresult.testName, tests: testresult.size(), failures: testresult.values().count(false)) {
                testresult.each{ testName, testPassed ->
                    delegate.delegate.testcase(name: testName) {
                        if(!testPassed){
                            echo "${testResults.testPassed}"
                            delegate.failure()
                        }
                    }
                }
            }
        }
    }  
  return stringWriter.toString()
}

