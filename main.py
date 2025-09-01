from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os


def run_agent():
    try:
        test1 = os.environ["test1"]
    except:
        test1="cant found"
    print(test1)
    now = datetime.now()
    print(f"Running AI news agent at {now}")

run_agent()
