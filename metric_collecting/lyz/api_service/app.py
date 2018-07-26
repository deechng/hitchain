#coding=utf-8

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import pymysql
import datetime

app = Flask(__name__)
access_token = ['']

#数据库配置
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

def re_conn():
    global conn
    global cur
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=dbname, charset='utf8')
    conn.autocommit(1)
    cur = conn.cursor()


#**********获取所有结果、单个项目方法**********
# 获取所有结果
def get_all_ranking_result():
    try:
        conn.ping()
    except:
        print("*****************连接断开重新连接")
        re_conn()

    select_sql_1 = "select prj_id, name, github_url, facebook_url, twitter_url from prj_list"
    select_sql_2 = "select score, rank, rank_date, m1_inf, m2_maturity, m3_quality, m4_team_healty, m5_activatin, m6_trend" \
                   " from daily_rank where prj_id = '%d' order by rank_date desc limit 1"

    cur.execute(select_sql_1)
    coin_list = cur.fetchall()

    all_ranking_result = []
    print("dan")

    for coin in coin_list:
        each_prj_ranking_result = {}
        each_prj_ranking_result['id'] = coin[0]
        each_prj_ranking_result['coin_name'] = coin[1]
        each_prj_ranking_result['repo_url'] = coin[2]
        each_prj_ranking_result['facebook_url'] = coin[3]
        each_prj_ranking_result['twitter_url'] = coin[4]
        # print(select_sql_2 % (coin[0]))
        cur.execute(select_sql_2 % (coin[0]))
        # print(select_sql_2 % (coin[0]))
        result = cur.fetchall()
        if result.__len__() == 0:
            print("未找到对应的结果",coin[0],coin[1])
            continue
        else:
            daiay_rank_result = result[0]

        each_prj_ranking_result['score'] = daiay_rank_result[0]
        each_prj_ranking_result['rank'] = daiay_rank_result[1]
        each_prj_ranking_result['rank_date'] = daiay_rank_result[2].strftime("%Y-%m-%d")
        # print(type(daiay_rank_result[2]))
        each_prj_ranking_result['m1_inf'] = daiay_rank_result[3]
        each_prj_ranking_result['m2_maturity'] = daiay_rank_result[4]
        each_prj_ranking_result['m3_quality'] = daiay_rank_result[5]
        each_prj_ranking_result['m4_team_healthy'] = daiay_rank_result[6]
        each_prj_ranking_result['m5_activeness'] = daiay_rank_result[7]
        each_prj_ranking_result['m6_trend'] = daiay_rank_result[8]

        all_ranking_result.append(each_prj_ranking_result)

    return all_ranking_result


#获取单个项目
def get_prj_ranking_result(prj_id, start_time, end_time):
    try:
        conn.ping()
    except:
        re_conn()

    select_sql_1 = "select prj_id, name, github_url, facebook_url, twitter_url from prj_list where prj_id = '%s'"
    select_sql_2 = "select score, rank, rank_date, m1_inf, m2_maturity, m3_quality, m4_team_healty, m5_activatin, m6_trend" \
                   " from daily_rank where prj_id = '%s' and rank_date > '%s' and rank_date < '%s' order by rank_date desc limit 1"
    print("nihao")
    print(select_sql_1 % prj_id)

    cur.execute(select_sql_1 % prj_id)
    # print(select_sql_1 % prj_id)
    print("wobuhao")
    coin = cur.fetchall()[0]

    prj_ranking_result = []
    each_prj_ranking_result = {}
    print("dan")
    each_prj_ranking_result['id'] = coin[0]
    each_prj_ranking_result['coin_name'] = coin[1]
    each_prj_ranking_result['repo_url'] = coin[2]
    each_prj_ranking_result['facebook_url'] = coin[3]
    each_prj_ranking_result['twitter_url'] = coin[4]
    cur.execute(select_sql_2 % (prj_id, start_time, end_time))
    print(select_sql_2 % (coin[0], start_time, end_time))
    result = cur.fetchall()
    if result.__len__() == 0:
        print("未找到对应的结果", coin[0], coin[1], start_time, end_time)
        abort(404)
    else:
        daiay_rank_result = result[0]

    each_prj_ranking_result['score'] = daiay_rank_result[0]
    each_prj_ranking_result['rank'] = daiay_rank_result[1]
    each_prj_ranking_result['rank_date'] = daiay_rank_result[2].strftime("%Y-%m-%d")
    # print(type(daiay_rank_result[2]))
    each_prj_ranking_result['m1_inf'] = daiay_rank_result[3]
    each_prj_ranking_result['m2_maturity'] = daiay_rank_result[4]
    each_prj_ranking_result['m3_quality'] = daiay_rank_result[5]
    each_prj_ranking_result['m4_team_healthy'] = daiay_rank_result[6]
    each_prj_ranking_result['m5_activeness'] = daiay_rank_result[7]
    each_prj_ranking_result['m6_trend'] = daiay_rank_result[8]

    prj_ranking_result.append(each_prj_ranking_result)


    return prj_ranking_result

#**********接口url**********
#获取所有项目前一天排名情况
@app.route('/coin/api/all_ranking', methods=['GET'])
def get_all_ranking():
    try:
        for re_arg in request.args:
            if request.args[re_arg] in access_token:
                # 返回所有项目排行列表
                all_ranking_result = get_all_ranking_result()
                return jsonify(all_ranking_result), 201
            else:
                abort(404)
    except:
        abort(404)

#获取单个项目指定时间排名情况
@app.route('/coin/api/prj_ranking', methods=['GET'])
def get_prj_ranking():
    try:
        prj_id = request.args['prj_id']
        start_time = request.args['start_time']
        end_time = request.args['end_time']
        # 防止有多的参数
        for re_arg in request.args:
            if 'prj_id' == re_arg or 'start_time' == re_arg or 'end_time' == re_arg:
                # 返回列表
                if request.args['access_token'] in access_token:
                    prj_ranking_result = get_prj_ranking_result(prj_id, start_time, end_time)

                    return jsonify(prj_ranking_result), 201
                else:
                    abort(404)

            else:
                abort(404)
    except:
        abort(404)

#根据项目名查找对应项目基本情况
@app.route('/coin/api/id', methods=['get'])
def get_id():
    try:
        conn.ping()
    except:
        re_conn()

    try:
        select_sql = "select prj_id, name, github_url, facebook_url, twitter_url from prj_list where name = '%s'"
        coin_list = []
        coin_name = request.args['name']
        print(request.args['access_token'])
        if request.args['access_token'] in access_token:
            cur.execute(select_sql % coin_name)
            coin = {}
            cur_result = cur.fetchall()[0]

            each_coin_result = {}
            each_coin_result['prj_id'] = cur_result[0]
            each_coin_result['name'] = cur_result[1]
            each_coin_result['repo_url'] = cur_result[2]
            each_coin_result['facebook_url'] = cur_result[3]
            each_coin_result['twitter_url'] = cur_result[4]

            coin[coin_name] = each_coin_result
            coin_list.append(coin)

            print(coin_list)

            return jsonify(coin_list), 201
        else:
            abort(404)
    except:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

