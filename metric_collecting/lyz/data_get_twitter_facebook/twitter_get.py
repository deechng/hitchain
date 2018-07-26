#coding=utf-8
import requests
import pymysql
from bs4 import BeautifulSoup
import xlrd
import logging
import datetime
import time
import sys
sys.path.append("..")
from email_monitor import emailer

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='twitter_get.log',
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

dbname=''
user=''
passwd=''
host = ''

conn =  pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=dbname,charset='utf8')
conn.autocommit(1)
cur=conn.cursor()
insertSql = "insert into twitters_data(coin_id, name, tweets_num, following_num, followers_num, created_time) values ('%d', '%s', '%d', '%d', '%d', '%s')"
insertSql_null = "insert into twitters_data(coin_id, name, created_time) values ('%d', '%s', '%s')"

# url爬取，并且解析
def get_twitterdata(coin_url):
    if coin_url == "":
        return 0, 0, 0

    logging.info(coin_url)
    try:
        response = requests.get(coin_url).text
    except:
        logging.info("getUrlResponseFailed!: ", coin_url)
        return "EOF","EOF","EOF"
    soup_xml = BeautifulSoup(response, "lxml")
    # 加上此行，可以优化代码运行速度
    try:
        soup_tmp = soup_xml.find_all('ul', "ProfileNav-list")
        soup = soup_tmp[0]
    except:
        logging.info("不可用的链接")
        return "wr_url", "wr_url", "wr_url"

    try:
        tweets_li = soup.find_all('li', "ProfileNav-item ProfileNav-item--tweets is-active")
        if tweets_li.__len__() > 0:
            tweets_span = tweets_li[0].find_all(name='span', attrs={"ProfileNav-value"})
            tweets_num = int(tweets_span[0].attrs['data-count'])
        else:
            tweets_num = 0

        following_li = soup.find_all('li', "ProfileNav-item ProfileNav-item--following")
        if following_li.__len__() > 0:
            following_span = following_li[0].find_all(name='span', attrs={"ProfileNav-value"})
            following_num = int(following_span[0].attrs['data-count'])
        else:
            following_num = 0

        followers_li = soup.find_all('li', "ProfileNav-item ProfileNav-item--followers")
        if followers_li.__len__() > 0:
            followers_span = followers_li[0].find_all(name='span', attrs={"ProfileNav-value"})
            followers_num = int(followers_span[0].attrs['data-count'])
        else:
            followers_num = 0
    except:
        logging.info("网络异常，连接不上")
        emailer.email("爬取twitter网络异常")

    return tweets_num, following_num, followers_num


# 开始爬取
def start():
    re_extract_url_list = []
    re_extract_id_list = []
    re_extract_name_list = []

    select_sql = "select prj_id, name, twitter_url from prj_list"
    cur.execute(select_sql)
    cur_result = cur.fetchall()
    for result in cur_result:

        tweets_num, following_num, followers_num = get_twitterdata(result[2])
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tweets_num == "EOF":
            re_extract_id_list.append(result[0])
            re_extract_name_list.append(result[1])
            re_extract_url_list.append(result[2])

            continue
        if tweets_num == "wr_url":
            cur.execute(
                insertSql % (int(result[0]), str(result[1]), 0, 0, 0, dt))
            continue
        logging.info(str(int(result[0])) + "  " + str(result[1]) + "  " + str(tweets_num) + "  " + str(
            following_num) + "  " + str(followers_num))
        cur.execute(
            insertSql % (int(result[0]), str(result[1]), tweets_num, following_num, followers_num, dt))

    if re_extract_url_list.__len__() > 0:
        time.sleep(10)
        if(re_extract(re_extract_id_list, re_extract_name_list, re_extract_url_list)):
            logging.info("爬取结束")
        else:
            logging.info("爬取网络有问题")
    cur.close()

#重新爬取函数
def re_extract(coinIdList, coinNameList, coinUrlList):
    re_extract_flag = True
    coin_list_len = coinIdList.__len__()
    for i in range(coin_list_len):
        tweets_num, following_num, followers_num = get_twitterdata(coinUrlList[i])
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tweets_num == "EOF":
            logging.info("重新爬取失败" + str(int(coinIdList[i])) + "  " + str(coinNameList[i]) + "  " + str(tweets_num) + "  " + str(
                following_num) + "  " + str(followers_num))
            re_extract_flag = False
            continue
        logging.info(str(int(coinIdList[i])) + "  " + str(coinNameList[i]) + "  " + str(tweets_num) + "  " + str(
            following_num) + "  " + str(followers_num))
        cur.execute(
            insertSql % (int(coinIdList[i]), str(coinNameList[i]), tweets_num, following_num, followers_num, dt))
    return re_extract_flag

if __name__ == '__main__':
    logging.info("hello")
    start()


