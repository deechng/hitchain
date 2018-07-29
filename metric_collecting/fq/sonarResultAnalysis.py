import json

import datetime
import requests
import ConfigParser
import time
import pymysql


cf = ConfigParser.ConfigParser()
cf.read("config.conf")
root_url = "http://localhost:"+cf.get("sonar","sonar_port")+"/api"
issue_url = root_url + "/issues/search?componentKeys="
# issue_url_filter = "&severities=CRITICAL%2CMAJOR"
issue_url_filter = "&resolved=false&severities="
metrics_url = root_url + "/measures/component?"
conn = pymysql.connect(host=cf.get("DB","host"),
                       port=int(cf.get("DB","port")),
                       user=cf.get("DB","user"),
                       passwd=cf.get("DB","password"),
                       db=cf.get("DB","database"),
                       charset='utf8')

def filter(value):
    if value == 0:
        return value
    elif not value:
        return "null"
    else:
        return value


def getMetric(repoName,metricKeys):
    params = {"component":repoName,"metricKeys":metricKeys}
    r = ""
    while r == "":
        try:
            r = requests.get(metrics_url,params=params).json()
            break
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            continue

    try:
        return r["component"]["measures"][0]["value"]
    except:
        print ('No result')

def getMetricsOfRepo(repoName):
    loc = getMetric(repoName,"ncloc")
    duplication = getMetric(repoName,"duplicated_lines_density")
    return {"loc":loc,"duplication":duplication}



def getIssueResult(repoName,type):

    # params = {"project":repoName}
    r = ""
    while r == "":
        try:
            r = requests.get(issue_url+repoName+issue_url_filter+type)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            continue

    if not r.json():
        print("")
    else:
        return r.json()


def getIssueNumbers(json_result,repoName):
    # issues = []
    # count = 0
    if not json_result:
        print('No result')
    else:

        if not json_result['issues']:
            print('')
        else:
            # count = 0
            # if json_result["issues"]:
            #     for issue in json_result["issues"]:
            #         if issue["project"] == repoName and issue["severity"] in ["CRITICAL","MAJOR","BLOCKER"]:
            #             count += 1
            #
            # return count
            return json_result["total"]

    # for eachFileIssue in issues:
    #     for eachIssue in eachFileIssue:
    #         if eachIssue["project"] == repoName and eachIssue["status"] == "OPEN" \
    #                 and eachIssue["severity"] in ["CRITICAL","MAJOR","BLOCKER"] :
    #             count += 1
    # return count

def getIssueNumberOfRepo(repoName,tpye):
    return getIssueNumbers(getIssueResult(repoName,tpye),repoName)

def getAllIssueNumberOfRepo(repoName):
    return {
        "major":getIssueNumberOfRepo(repoName,"MAJOR"),
        "blocker":getIssueNumberOfRepo(repoName,"BLOCKER"),
        "critical":getIssueNumberOfRepo(repoName,"CRITICAL"),
        "minor":getIssueNumberOfRepo(repoName,"MINOR"),
        "info":getIssueNumberOfRepo(repoName,"INFO")
    }

def addSonarResult(issueNum,metrics,projId,repoName):
    with conn.cursor() as cur:

        issue_major = filter(issueNum["major"])
        issue_blocker = filter(issueNum["blocker"])
        issue_critical = filter(issueNum["critical"])
        issue_minor = filter(issueNum["minor"])
        issue_info = filter(issueNum["info"])
        loc = filter(metrics["loc"])
        duplication = metrics["duplication"]
        if duplication:
            duplication = float(duplication)/100
        duplication = filter(duplication)
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into sonar_repo_issues_num (`proj_id`,`issue_major`,`issue_blocker`,`issue_critical`," \
              "`issue_minor`,`issue_info`, `repo_name`, `create_time`, `loc`, `duplication`) values " \
              "(%s,%s,%s,%s,%s,%s,'%s','%s',%s, %s)" \
              % (projId,issue_major,issue_blocker,issue_critical,issue_minor,issue_info,repoName,dt,loc,duplication)
        print sql
        cur.execute(sql)
        conn.commit()

def getCloneRepos():
    with conn.cursor() as cur:
        sql = "select proj_name,repo_name,git_addr,proj_id,ps,is_clone from git_clone_pull_status"
        cur.execute(sql)
        return cur.fetchall()


def start():
    for repo in getCloneRepos():
        proName, repoName, gitAddr, projId, ps, isClone = repo
        if isClone:
            addSonarResult(getAllIssueNumberOfRepo(repoName),
                           getMetricsOfRepo(repoName),
                           projId,
                           repoName)
        else:
            issueNum = {
                "major": None,
                "blocker": None,
                "critical": None,
                "minor": None,
                "info": None
            }
            metrics = {
                "loc": None,
                "duplication": None
            }
            addSonarResult(issueNum,metrics,projId,repoName)
        # print getIssueNumbers(getIssueResult("bitcoin"),"bitcoin")

# print  getIssueNumberOfRepo("bitcoin","MAJOR")
#
# print getMetricsOfRepo("bitcoin")