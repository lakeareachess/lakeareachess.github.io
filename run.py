import schedule
import time
import os
schedule.every(300).seconds.do(os.system("update.bat"))
while True:
    schedule.run_pending()
    time.sleep(1)