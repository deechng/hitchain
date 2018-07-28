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
import clone
import time
import re


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

def getCloneRepos():
    with conn.cursor() as cur:
        sql = "select proj_name,repo_name,git_addr,proj_id,ps,is_clone from git_clone_pull_status"
        cur.execute(sql)
        return cur.fetchall()



def start():
    # pull.PullProcess()
    clone.CloneProcess()
    sourcePathBase = os.getcwd() + "/" + cf.get("server", "gitCloneAddr")
    targetPathBase = os.getcwd() + "/" + cf.get("server", "sonarTempAddr")
    for repo in getCloneRepos():
        proName, repoName, gitAddr, projId, ps, isClone = repo
        if isClone:
            sourcePath = sourcePathBase + "/" + re.sub('\s','',proName) + "/" + repoName
            targetPath = targetPathBase + "/" + re.sub('\s','',proName) + "/" + repoName
            helper.mkdir(targetPath)
            helper.copyFiles(sourcePath, targetPath)

            if ps == "C":
                sonarScan.runSonarScannerC(targetPath)
            else:
                sonarScan.runSonarScanner(targetPath)
            time.sleep(10)
            shutil.rmtree(targetPath)
            shutil.rmtree(sourcePath)
    time.sleep(60)
    sonarResultAnalysis.start()

def scannerOneRepo(repoName):
    sourcePathBase = os.getcwd() + "/" + cf.get("server", "gitCloneAddr")
    targetPathBase = os.getcwd() + "/" + cf.get("server", "sonarTempAddr")
    sourcePath = sourcePathBase + "/" + repoName
    targetPath = targetPathBase + "/" + repoName
    helper.mkdir(targetPath)
    helper.copyFiles(sourcePath, targetPath)

    sonarScan.runSonarScanner(targetPath)

    shutil.rmtree(targetPath)

def scannerOneRepoC(repoName):
    sourcePathBase = os.getcwd() + "/" + cf.get("server", "gitCloneAddr")
    targetPathBase = os.getcwd() + "/" + cf.get("server", "sonarTempAddr")
    sourcePath = sourcePathBase + "/" + repoName
    targetPath = targetPathBase + "/" + repoName
    helper.mkdir(targetPath)
    helper.copyFiles(sourcePath, targetPath)

    sonarScan.runSonarScannerC(targetPath)

    # shutil.rmtree(targetPath)

def scannerRepoList(repoNameList):
    sourcePathBase = os.getcwd() + "/" + cf.get("server", "gitCloneAddr")
    targetPathBase = os.getcwd() + "/" + cf.get("server", "sonarTempAddr")
    for repoName in repoNameList:
        sourcePath = sourcePathBase + "/" + repoName
        targetPath = targetPathBase + "/" + repoName
        helper.mkdir(targetPath)
        helper.copyFiles(sourcePath, targetPath)

        sonarScan.runSonarScanner(targetPath)

        shutil.rmtree(targetPath)

if __name__ == "__main__":
    start()








