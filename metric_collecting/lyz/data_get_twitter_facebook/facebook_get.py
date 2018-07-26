#coding=utf-8
import xlrd
import requests
import pymysql
import datetime
import logging
import math
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='facebook_get.log',
                filemode='w')

logging.getLogger("requests").setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# dbname=''
# user=''
# passwd=''
# host = ''
#
dbname=''
user=''
passwd=''
host = ''

conn =  pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=dbname,charset='utf8')
conn.autocommit(1)
cur=conn.cursor()

def get_fbdata(link):

    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text)
        res = soup.find_all(name='div', attrs={"class": "_4bl9"})
        return res
    except:
        print("getUrlResponseFailed!: ", link)
        return "error"

def insert_value(id, name,likenum,watchnum ):
    insert_sql="insert into facebook_data(coin_id,fb_name,likes_num,watches_num,created_time) VALUES(%d,\'%s\',%d,%d,\'%s\')"
    dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(insert_sql%(id, name,likenum,watchnum,dt ))

def convert_value(numstring):
    tmpnum=numstring.split(",")
    total=0
    for i in range(len(tmpnum)):
        total+=int(tmpnum[i])*math.pow(1000,len(tmpnum)-i-1)
    return total

def read_coinPrjectList():
    path = 'bitinfo.xlsx'
    data = xlrd.open_workbook(path)
    sheets = data.sheets()
    sheet_1_by_name = data.sheet_by_name(u'Sheet1')
    n_of_rows = sheet_1_by_name.nrows

    return n_of_rows,sheet_1_by_name
def start():
    select_sql = "select prj_id, name, facebook_url from prj_list"
    cur.execute(select_sql)
    cur_result = cur.fetchall()
    cnt = 0

    for result in cur_result:
        id = result[0]
        name = result[1]
        link = result[2]

        if len(link) != 0:
            cnt += 1
            res=get_fbdata(link)
            if res=='error':
                continue
            else:
                try:
                    if len(res) >= 3:
                        likenum = convert_value(res[1].text.split(" ")[0])
                        watchnum = convert_value(res[2].text.split(" ")[0])
                        insert_value(id, name, likenum, watchnum)
                        logging.info("...............value obtained!..............")

                except:
                    pass
        else:
            insert_value(id, name, 0, 0)
            logging.info("...............value equals 0..............")
    logging.info('Non-zero number %d' % (cnt))
    cur.close()
    logging.info("...............finished..............")




if __name__=='__main__':

    logging.info("...............fb data start..............")
    start()