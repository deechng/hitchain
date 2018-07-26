import json
import requests
import ConfigParser
import time

cf = ConfigParser.ConfigParser()
cf.read("config.conf")
root_url = "http://localhost:"+cf.get("sonar","sonar_port")+"/api"
issue_url = root_url + "/issues/search?componentKeys="
# issue_url_filter = "&severities=CRITICAL%2CMAJOR"
issue_url_filter = "&resolved=false&severities="
metrics_url = root_url + "/measures/component?"



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


        # print getIssueNumbers(getIssueResult("bitcoin"),"bitcoin")

# print  getIssueNumberOfRepo("bitcoin","MAJOR")
#
# print getMetricsOfRepo("bitcoin")