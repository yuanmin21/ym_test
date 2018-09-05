#!/usr/bin/env groovy

import org.jenkinsci.plugins.pipeline.utility.steps.fs.FileWrapper
import com.cwctravel.hudson.plugins.extended_choice_parameter.ExtendedChoiceParameterDefinition
import java.net.URLEncoder
import java.util.regex.Matcher
import groovy.transform.Field
import javax.ws.rs.core.UriBuilder
import groovy.xml.*
import static java.util.UUID.randomUUID

def slave1Config = [
    "0" : ['SSH_ID': env.SOC1_0_SSH_ID,'APC_IP': env.SOC1_0_APC_IP,  'APC_SLOT': env.SOC1_0_APC_SLOT,'TARGET_IP': env.SOC1_0_TARGET_IP,'TCP_IP':env.SOC1_0_TCP_IP],
    "1" : ['SSH_ID': env.SOC1_1_SSH_ID,'APC_IP': env.SOC1_1_APC_IP,  'APC_SLOT': env.SOC1_1_APC_SLOT,'TARGET_IP': env.SOC1_1_TARGET_IP,'TCP_IP':env.SOC1_1_TCP_IP]
]
def slave2Config = [
    "0" : ['SSH_ID': env.SOC2_0_SSH_ID,'APC_IP': env.SOC2_0_APC_IP,  'APC_SLOT': env.SOC2_0_APC_SLOT,'TARGET_IP': env.SOC2_0_TARGET_IP,'TCP_IP':env.SOC2_0_TCP_IP],
    "1" : ['SSH_ID': env.SOC2_1_SSH_ID,'APC_IP': env.SOC2_1_APC_IP,  'APC_SLOT': env.SOC2_1_APC_SLOT,'TARGET_IP': env.SOC2_1_TARGET_IP,'TCP_IP':env.SOC2_1_TCP_IP],
    "2" : ['SSH_ID': env.SOC2_2_SSH_ID,'APC_IP': env.SOC2_2_APC_IP,  'APC_SLOT': env.SOC2_2_APC_SLOT,'TARGET_IP': env.SOC2_2_TARGET_IP,'TCP_IP':env.SOC2_2_TCP_IP]
]
def configMap = [ (env.SOC1_SLAVENAME) : slave1Config, (env.SOC2_SLAVENAME) : slave2Config]

def toDo = [
    /* Build with tests */
    //[ name: '1098R20_Internal_E2e_Bics2_Nvme',              soc: '1098R20',  customer: 'Internal',      target: 'E2e_Bics2_Nvme',                configId: '0',  build: 'windows-build', test: env.SOC2_SLAVENAME],

    /* Build only */
    //Eldora
    /* [ name: '1093R21_Internal_E2e_tfx132',           soc: '1093R21',         customer: 'Internal',      target: 'E2e_tfx132',                    configId: '0',  build: 'windows-build' ],
    [ name: '1093R21_Internal_E2e_tfx132_Mst',       soc: '1093R21',         customer: 'Internal',      target: 'E2e_tfx132_Mst',                configId: '0',  build: 'windows-build' ],
    //Zao
    [ name: '1098_Internal_E2e_Bics2_Nvme',                soc: '1098',      customer: 'Internal',      target: 'E2e_Bics2_Nvme',                configId: '0',  build: 'windows-build'],
    [ name: '1098_Internal_E2e_Bics3_Nvme',                soc: '1098',      customer: 'Internal',      target: 'E2e_Bics3_Nvme',                configId: '0',  build: 'windows-build' ],
    [ name: '1098_Internal_E2e_Bics2_Nvme_4MediaSpaces',   soc: '1098',      customer: 'Internal',      target: 'E2e_Bics2_Nvme_4MediaSpaces',   configId: '0',  build: 'windows-build' ],
    [ name: '1098_Internal_E2e_Bics2_Nvme_Historylog',     soc: '1098',      customer: 'Internal',      target: 'E2e_Bics2_Nvme_Historylog',     configId: '0',  build: 'windows-build' ],
    [ name: '1098_Standard_E2e_Bics2',                     soc: '1098',      customer: 'Standard',      target: 'E2e_Bics2',                     configId: '0',  build: 'windows-build' ],


    //ZaoR20
    [ name: '1098R20_Internal_E2e_Bics2_Nvme_4MediaSpaces', soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics2_Nvme_4MediaSpaces',  configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Internal_E2e_Bics2_Nvme_Historylog',   soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics2_Nvme_Historylog',    configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Internal_E2e_Bics2_Sata',              soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics2_Sata',               configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Internal_E2e_Bics3_Nvme',              soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics3_Nvme',               configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Internal_Bics2_Nvme_Mst_Lite',         soc: '1098R20',      customer: 'Internal',     target: 'Bics2_Nvme_Mst_Lite',          configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Internal_E2e_Bics2_Nvme_Mst',          soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics2_Nvme_Mst',           configId: '0',   build: 'windows-build' ],
    [ name: '1098R20_Standard_Ramdrive0',                   soc: '1098R20',      customer: 'Standard',     target: 'Ramdrive0',                    configId: '0',   build: 'windows-build' ],*/
    [ name: 'Alamere_Jenkins_01',                   soc: '1098R20',      customer: 'Standard',     target: 'E2e_Bics2',                    configId: '0',   build: 'windows-build', test: env.SOC2_SLAVENAME ],
    [ name: 'Alamere_Jenkins_02',              soc: '1098R20',      customer: 'Internal',     target: 'E2e_Bics2_Nvme',               configId: '1',   build: 'windows-build', test: env.SOC2_SLAVENAME ],
]

def stageCases = [
    // Precommit
    "Flash_fw": [passedParser: this.&jsonTypePassedParser], 
    //"FIO": [passedParser: this.&jsonTypePassedParser], 
    //"marvo": [passedParser: this.&jsonTypePassedParser],
    "IOL": [passedParser: this.&jsonTypePassedParser]
]
def testcases = ["Flash_fw","IOL"]
//def testcases = ["Flash_fw"]
    
def testTasks = [:]

toDo.each { task ->
    testTasks["$task.name"] = {
        node("slave1") {     
            git([url: 'https://github.com/yuanmin21/ym_test.git', branch: 'master'])
            withEnv( //add variable into environment
                ["SSH_ID=${configMap[task.test][task.configId]['SSH_ID']}",
                "TCP_IP=${configMap[task.test][task.configId]['TCP_IP']}"]){                         
                echo "SSH_ID is ${SSH_ID}"
                echo "TCP_IP is ${TCP_IP}"              
                def results = [:]
                testcases.each { test ->
                    def settings = stageCases[test]
                    try{
                        // Run the different testing.
                        //stage("$task.name ${test} testing"){
                            switch (test) {
                                case "Flash_fw":
                                        timeout(time: 5, unit: 'MINUTES') {
                                            sh script: "ssh ${SSH_ID} 'cd /home/workspace/script; sudo python3 online_flash_fw.py -f 1098R20_Internal_E2e_Bics2_Nvme.dfw -d tcp://${TCP_IP} -p marvell'"
                                        }
                                        sh script: "scp -r ${SSH_ID}:/home/workspace/Flash_fw ${WORKSPACE}"
                                        sh script: "ssh ${SSH_ID} 'sudo rm -Rf /home/workspace/Flash_fw'"
                                        sh script: "ssh ${SSH_ID} 'sudo reboot'"
                                        rebootTest(5)
                                        break

                                
                                case "FIO":
                                    SSH_ID1
                                    sh script: "ssh ${SSH_ID}@${TCP_IP} 'cd /home/svt/fio_script; python3 fio.py fio_test.ini tcp://10.85.149.105 marvell'"
                                    sh script: "scp -r ${SSH_ID}@${TCP_IP}:/home/svt/fio_script/Logs/FIO/ root@10.18.134.101:/home/jenkins/workspace/Alamere_Test"
                                    sh script: "ssh ${SSH_ID}@${TCP_IP} 'rm -r /home/svt/fio_script/Logs/FIO'"
                                    break

                                case "IOL":
                                    SSH_ID2
                                    

                                    sh script: "ssh ${SSH_ID}@${TCP_IP} 'cd /home/svt/fio_script; sudo  python3 IOL_test.py /home/svt/iol_interact-9.0b/nvme/manage/ testcases -d tcp://${TCP_IP} -p marvell'"
                                    sh script: "scp -r ${SSH_ID}@${TCP_IP}:/home/svt/fio_script/Logs/FIO/ root@10.18.134.101:/home/jenkins/workspace/Alamere_Test"
                                    sh script: "ssh ${SSH_ID}@${TCP_IP} 'rm -r /home/svt/fio_script/Logs/FIO'"

                                    break
                                
                                case "marvo":
                                    timeout(time: 3, unit: 'HOURS') {
                                        sh script: "ssh ${SSH_ID} 'cd /home/svt/marvo; xvfb-run -a python3 Marvo.py /home/svt/marvo /home/svt/marvo/PCIe tcp://${TCP_IP} marvell'"
                                    }
                                    sh script: "scp -r ${SSH_ID}:/home/svt/marvo/Logs/marvo ${WORKSPACE}"
                                    sh script: "ssh ${SSH_ID} 'rm -r /home/svt/marvo/Logs/marvo'"
                                    break
                            }
                        //}                    
                        // Collect all test results as a map 
                        Map currentTestResults = [
                            (test): collectTestResults(                    
                                test,
                                settings.passedParser,
                                task.name,
                                )
                            ]
                        results << currentTestResults    
                        //echo "results is ${results}"
                        writeFile(file: 'test.xml', text: resultsAsJUnit(currentTestResults, task.name))
                        // Generate the Junit Report 
                        //archiveArtifacts(artifacts: '${test}.xml', excludes: null)
                        step([
                            $class: 'JUnitResultArchiver',
                            testResults: '**/test.xml'
                            ])                    
                    } catch(e) {
                            /* Error Handling
                               When test is failed, upload the log onto Jenkins server.                            
                            */
                            echo "Testing failed due to $e"
                            switch (test) {
                                case "FIO":
                                    sh script: "scp -r ${SSH_ID}:/home/svt/fio_script/Logs/FIO/ ${WORKSPACE}"
                                    sh script: "ssh ${SSH_ID} 'rm -r /home/svt/fio_script/Logs/FIO'"
                                    break
                                case "marvo":
                                    sh script: "scp -r ${SSH_ID}:/home/svt/marvo/Logs/marvo ${WORKSPACE}"
                                    sh script: "ssh ${SSH_ID} 'rm -r /home/svt/marvo/Logs/marvo'"
                                    break
                            }
                            sh script: "tar -zPcv -f ${test}.tar.gz ${test}/*.log"
                            // Store the zips as a tar file
                            archiveArtifacts artifacts: "${test}.tar.gz", allowEmptyArchive: true
                            // Cleanup
                            sh "rm -rf ${test}/ ${test}.tar.gz"                            
                            currentBuild.description = """<br /><a style="text-decoration: none; background-color:red; color:white" href="${env.BUILD_URL}artifact/${buildLog}"><b>Test failed: ${test}</b></a>"""
                        }finally {
                            // If there is no error, upload the test result table.    
                            // Publish the result table on the status overview.       
                            currentBuild.description = currentBuild.description + "<br /></strong>${resultsAsTable(results, task.name)}"                               
                            echo "tag"
                        } 
                }
            }                 
        }
    }
}        
          
timestamps {
    stage("Build") {
        echo "After Build"
        
        //currentBuild.description = "Fake Build Stage"        
    }
    stage("Test") {
        parallel testTasks
    }
}

/**
 * Return the collected test result from every test case.
 * @param test The test means the different stage.
 * @param passedParser The function is used to check the selected file whether it includes required keyword. 
 */
def collectTestResults(String test, Closure passedParser, String Testname) {
    String copyPath = "$env.ARTIFACTS_COPY_PATH"    
    
    // Initialize empty result map.
    def resultMap = [:]

    // Gather all the logfiles produced.    
    def logFiles = sh (
            script: "ls ${test}/summary.log",
            returnStdout:true
            ).readLines()

    // Extract the test name and result from each logfile.    
    logFiles.each { logFile ->
        passedParser(logFile, resultMap)
    }

    sh script: "tar -zPcv -f ${test}_${Testname}.tar.gz ${test}/*.log"
    // Store the zips as a tar file
    archiveArtifacts artifacts: "${test}_${Testname}.tar.gz", allowEmptyArchive: true

    // Cleanup
    sh "rm -rf ${test}/ ${test}_${Testname}.tar.gz"

    // Return the accumulated result.
    return resultMap
}

/**
 * Return the collected test result is stored as a map from every test case. 
 * Parser for test results.
 * @param logFile The logFile means the different stage.
 * @param resultMap The resultMap is a map, recording the required file exists. 
 */

def jsonTypePassedParser(logFile, resultMap) {   
    String  testName
    boolean testPassed 
    readFile(logFile).split("\n").each { line ->
        testName = line.subSequence(0,line.lastIndexOf(":"))   
        testPassed = line.contains("Pass")
        resultMap << [(testName): testPassed]
        println resultMap
    }    
    return resultMap  
}
/**
 * Return the generated table based on different testcases and transferred to html format.
 * @param testResults The testResults means the result is stored as a map and aims to display on the jenkins. 
 */
 
@NonCPS
String resultsAsTable(def testResults, String TestName) {
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
                            echo "test name is ${TestName}"
                            delegate.strong("[Stage] ${test}")
                            delegate.a("Logs", href: "${env.BUILD_URL}/artifact/" + "${test}_${TestName}.tar.gz")
                        }
                    }
                    testResult.each { testName, testPassed ->
                        delegate.delegate.delegate.tr {
                            delegate.td("$testName ${TestName}", class: testPassed ? 'passed' : 'failed')
                        }
                    }
                }
            }
        }
    }
    return stringWriter.toString()
}

/**
 * Return the generated xml format report based on different testcases.
 * @param testResults The testResults means the result is stored as a map and aims to display on the jenkins. 
 */

@NonCPS
String resultsAsJUnit(def testResults, String TestName) {
    StringWriter  stringWriter  = new StringWriter()
    MarkupBuilder markupBuilder = new MarkupBuilder(stringWriter)
    // All those delegate calls here are messing up the elegancy of the MarkupBuilder
    // but are needed due to https://issues.jenkins-ci.org/browse/JENKINS-32766
    markupBuilder.testsuites {
        testResults.each{ test, testresult ->
            echo "test name is ${TestName}"
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


def rebootTest(retryCount){
  def errorCode = -1
  def uartFound = -1
  def retry = retryCount
  while((errorCode != 0  && uartFound == -1) && retry > 0){
    echo "-------------reboot-------"
    sh script:"ssh $SSH_ID 'sudo shutdown now'",returnStatus:true
    sh 'python3 $WORKSPACE/rebootTarget.py $APC_IP $APC_SLOT $TARGET_IP $SSH_ID'
    errorCode = sh script:'ssh $SSH_ID sudo modprobe nvme; ssh $SSH_ID ls /dev/nv*',returnStatus:true
    cmdString = sh script:'ssh pi@$TCP_IP lsusb', returnStdout:true
    uartFound = cmdString.indexOf("UART")
    retry = retry - 1
  }
  if(retry <= 0){
    currentBuild.result = "FAILED"
    error("Could not detect nvme device or uart device")
  }
}