#coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import facebook_get

# 输出时间
def job():
    facebook_get.start()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=22, minute=29)
scheduler.start()