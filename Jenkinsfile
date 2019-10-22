/**********************************************************************************
 * JenkinsFile for inmoov
 *
 * for adjusting build number for specific branch build
 * Jenkins.instance.getItemByFullName("inmoov-multibranch/develop").updateNextBuildNumber(185)
 *  
 * CHANGE build.properties TO BUILD AND DEPLOY A NEW BUILD
 *
 ***********************************************************************************/
properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/inmoov/'], pipelineTriggers([[$class: 'PeriodicFolderTrigger', interval: '2m']])])

node ('ubuntu') { // use any node

def fullversion = '1.1.' + ${env.BUILD_NUMBER}

environment {
    version = fullversion
}

// def props = []

// node ('ubuntu') {  // use labels to direct build
   // withEnv(javaEnv) {
   
   // def mvnHome
   stage('preparation') { // for display purposes
      // Get some code from a GitHub repository
      checkout scm
      // git 'https://github.com/MyRobotLab/inmoov.git'
      // git url: 'https://github.com/MyRobotLab/inmoov.git', branch: 'develop'
      // props = readProperties file: 'build.properties'
      // echo "props ${props}"
      
      sh 'git rev-parse --abbrev-ref HEAD > GIT_BRANCH'
      git_branch = readFile('GIT_BRANCH').trim()
      echo git_branch
    
      sh 'git rev-parse HEAD > GIT_COMMIT'
      git_commit = readFile('GIT_COMMIT').trim()
      echo git_commit
    
      echo git_commit
      echo "git_commit=$git_commit"
      // Run the maven build
      if (isUnix()) {
      // -o == offline      
         
         sh('printenv | sort')
         sh "'ant' -Dversion=${env.version}"
      } else {
        //  bat(/"${mvnHome}\bin\mvn" -Dbuild.number=${env.BUILD_NUMBER} -Dgit_commit=$git_commit -Dgit_branch=$git_branch -Dmaven.test.failure.ignore -q clean compile  /)
        bat(/"ant" -Dbuild.number=${env.version}/)
      }
   }

   stage('publish') {
   
    
   	def server = Artifactory.server 'repo' 
   	def uploadSpec = """{
                        "files": [
                                    {
                                        "pattern": "dist/inmoov-${env.version}.zip",
                                        "target": "inmoov/fr/inmoov/${env.version}/"
                                    }
                                    ]
                                }"""
		server.upload(uploadSpec)

	}
}
