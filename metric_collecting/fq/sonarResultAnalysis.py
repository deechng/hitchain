import json
import requests
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("config.conf")
root_url = "http://localhost:"+cf.get("sonar","sonar_port")+"/api"
issue_url = root_url + "/issues/search?componentKeys="
# issue_url_filter = "&severities=CRITICAL%2CMAJOR"
issue_url_filter = "&resolved=false&severities="
metrics_url = root_url + "/measures/component?"



def getMetric(repoName,metricKeys):
    params = {"component":repoName,"metricKeys":metricKeys}
    r = requests.get(metrics_url,params=params).json()
    try:
        return r["component"]["measures"][0]["value"]
    except:
        print ('No result')

def getMetricsOfRepo(repoName):
    loc = getMetric(repoName,"ncloc")
    return {"loc":loc}


def getIssueResult(repoName,type):

    # params = {"project":repoName}
    r = requests.get(issue_url+repoName+issue_url_filter+type)
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

# print getIssueNumbers(getIssueResult("bitcoin"),"bitcoin")

# print  getIssueNumberOfRepo("bitcoin","MAJOR")
#
# print getMetricsOfRepo("bitcoin")