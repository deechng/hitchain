#coding=utf-8
import pymysql
import xlrd
import xlwt

# dbname='lyz'
# user='root'
# passwd='111111'
# host = '10.107.10.110'

dbname='ossean_coin_rank'
user='root'
passwd='ossean@rank@123'
host = 'localhost'

conn =  pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=dbname,charset='utf8')
conn.autocommit(1)
cur=conn.cursor()

def read_coinProjectList():

    excelData = xlrd.open_workbook(u'bitinfo.xlsx')
    sheet0 = excelData.sheet_by_index(0)

    coinTwitterUrlList = sheet0.col_values(9)
    del coinTwitterUrlList[0]

    coinGithubUrlList = sheet0.col_values(7)
    del coinGithubUrlList[0]


    coinfacebookUrlList =sheet0.col_values(8)
    del coinfacebookUrlList[0]

    coinIdList = sheet0.col_values(0)
    del coinIdList[0]
    coinNameList = sheet0.col_values(1)
    del coinNameList[0]

    print(coinNameList[0],coinfacebookUrlList[0],coinIdList[0],coinGithubUrlList[0],coinTwitterUrlList[0])

    insert_sql = "insert into prj_list(prj_id, name, github_url, facebook_url, twitter_url ) values(%d,'%s','%s', '%s', '%s')"


    list_len = coinIdList.__len__()
    for i in range(list_len):
        id = coinIdList[i]
        name = coinNameList[i]
        githubUrl = coinGithubUrlList[i]
        facebookUrl = coinfacebookUrlList[i]
        twitterUrl = coinTwitterUrlList[i]
        cur.execute(insert_sql % (id, name, githubUrl, facebookUrl, twitterUrl))
    cur.close()


if __name__ == '__main__':
    read_coinProjectList()

