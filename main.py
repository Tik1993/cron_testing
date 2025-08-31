from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def run_agent():
    now = datetime.now()
    print(f"Running AI news agent at {now}")

run_agent()
