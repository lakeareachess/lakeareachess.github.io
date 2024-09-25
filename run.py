import schedule
import time
import os
def run():
    os.system("update.bat")
schedule.every(300).seconds.do(run)
while True:
    schedule.run_pending()
    time.sleep(1)