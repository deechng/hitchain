# -*- coding: utf-8 -*
import ConfigParser
import git
import helper
import pymysql
import time
import shutil
import re


cf = ConfigParser.ConfigParser()
cf.read("config.conf")

conn = pymysql.connect(host=cf.get("DB","host"),
                       port=int(cf.get("DB","port")),
                       user=cf.get("DB","user"),
                       passwd=cf.get("DB","password"),
                       db=cf.get("DB","database"),
                       charset='utf8')

def gitClone(repoCloneDir,repo):
    proName, repoName, gitAddr, ps = repo
    helper.mkdir(repoCloneDir)
    r=""
    while r =="":
        try:
            helper.mkdir(repoCloneDir+"/"+re.sub('\s','',proName))
            git.Git(repoCloneDir+"/"+re.sub('\s','',proName)).clone(gitAddr)
            r = "done"
        except:
            print ("clone repo:"+repoName+" failed")
            shutil.rmtree(repoCloneDir+"/"+repoName)
            time.sleep(5)
            continue

    if ps == "C":
        helper.configSonarPropertyC(repoName)
    else:
        helper.configSonarProperty(repoName)

    updateCloneStatus(proName, repoName)


def getCloneRepos():
    with conn.cursor() as cur:
        sql = "select proj_name,repo_name,git_addr,ps from git_clone_pull_status where git_addr is not null"
        cur.execute(sql)
        return cur.fetchall()

def updateCloneStatus(proName,repoName):
    with conn.cursor() as cur:
        # if repoName != "go-ethereum":
        #     sql = "update git_clone_pull_status set is_clone = 1 where proj_name = '%s' and repo_name = '%s'" % \
        #           (proName,repoName)
        # else:
        #     sql = "update git_clone_pull_status set is_clone = 0 where proj_name = '%s' and repo_name = '%s'" % \
        #           (proName, repoName)
        sql = "update git_clone_pull_status set is_clone = 1 where proj_name = '%s' and repo_name = '%s'" % \
              (proName, repoName)
        cur.execute(sql)
        conn.commit()


def CloneProcess():
    # repoListFile = cf.get("server", "repoList")
    for repo in getCloneRepos():
        # proName,repoName,gitAddr = repo
        gitClone(cf.get("server","gitCloneAddr"),repo)


if __name__ == "__main__":
    CloneProcess()