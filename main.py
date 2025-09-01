from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os


def run_agent():
    test1 = os.environ.get("test1", "not found")
    print(test1)
    now = datetime.now()
    print(f"Running AI news agent at {now}")

run_agent()
