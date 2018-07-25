# -*- coding: utf-8 -*

import ConfigParser
import helper
import pymysql
import pull
import os
import sonarScan
import sonarResultAnalysis
import datetime
import shutil


# 代码clone
# git.Git("pythonClone/").clone("https://github.com/alecive/FlatWoken.git")

# 代码pull
# repo = git.Repo('pythonClone/FlatWoken')
# o = repo.remotes.origin
# o.pull()

cf = ConfigParser.ConfigParser()
cf.read("config.conf")

conn = pymysql.connect(host=cf.get("DB","host"),
                       port=int(cf.get("DB","port")),
                       user=cf.get("DB","user"),
                       passwd=cf.get("DB","password"),
                       db=cf.get("DB","database"),
                       charset='utf8')

# 拉代码
# clone.CloneProcess()
def filter(value):
    if value == 0:
        return value
    elif not value:
        return "null"
    else:
        return value

def addSonarResult(issueNum,metrics,projId,repoName):
    with conn.cursor() as cur:

        issue_major = filter(issueNum["major"])
        issue_blocker = filter(issueNum["blocker"])
        issue_critical = filter(issueNum["critical"])
        issue_minor = filter(issueNum["minor"])
        issue_info = filter(issueNum["info"])
        loc = filter(metrics["loc"])
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into sonar_repo_issues_num (`proj_id`,`issue_major`,`issue_blocker`,`issue_critical`," \
              "`issue_minor`,`issue_info`, `repo_name`, `create_time`, `loc`) values (%s,%s,%s,%s,%s,%s,'%s','%s',%s)" \
              % (projId,issue_major,issue_blocker,issue_critical,issue_minor,issue_info,repoName,dt,loc)
        print sql
        cur.execute(sql)
        conn.commit()

def start():
    # pull.PullProcess()
    sourcePathBase = os.getcwd() + "/" + cf.get("server", "gitCloneAddr")
    targetPathBase = os.getcwd() + "/" + cf.get("server", "sonarTempAddr")
    for repo in pull.getCloneRepos():
        proName, repoName, gitAddr, projId = repo
        sourcePath = sourcePathBase + "/" + repoName
        targetPath = targetPathBase + "/" + repoName
        helper.mkdir(targetPath)
        helper.copyFiles(sourcePath, targetPath)

        sonarScan.runSonarScanner(targetPath)

        shutil.rmtree(targetPath)

        addSonarResult(sonarResultAnalysis.getAllIssueNumberOfRepo(repoName),
                       sonarResultAnalysis.getMetricsOfRepo(repoName),
                       projId,
                       repoName)

if __name__ == "__main__":
    start()








