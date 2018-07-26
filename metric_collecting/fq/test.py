import ConfigParser
import os
import shutil
import helper
import pymysql
import datetime

cf = ConfigParser.ConfigParser()
cf.read("config.conf")

# helper.mkdir("temp")

# shutil.copy2("repoClone","temp")
# shutil.rmtree("sonarTemp\\bitcoin")


conn = pymysql.connect(host=cf.get("DB","host"),
                       port=int(cf.get("DB","port")),
                       user=cf.get("DB","user"),
                       passwd=cf.get("DB","password"),
                       db=cf.get("DB","database"),
                       charset='utf8')

issueNum = {
    "major":10,
    "blocker":11,
    "critical":12,
    "minor":13,
    "info":14
}
metrics = {
    "loc":100,
    "duplication":20
}

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
        duplication = filter(metrics["duplication"])/100
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into sonar_repo_issues_num (`proj_id`,`issue_major`,`issue_blocker`,`issue_critical`," \
              "`issue_minor`,`issue_info`, `repo_name`, `create_time`, `loc`, `duplication`) values " \
              "(%s,%s,%s,%s,%s,%s,'%s','%s',%s, %s)" \
              % (projId,issue_major,issue_blocker,issue_critical,issue_minor,issue_info,repoName,dt,loc,duplication)
        print sql
        cur.execute(sql)
        conn.commit()

addSonarResult(issueNum,metrics,1,"bitcoin")

# print 20*1.0/100