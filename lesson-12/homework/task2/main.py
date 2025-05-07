from scraping import fetch_jobs
from db import add_new_jobs
from db import get_jobs
from db import update_jobs

fetched_jobs = fetch_jobs()
db_jobs = get_jobs()

updated_jobs = []
new_jobs = []

for fetched in fetched_jobs:
    is_new = True
    for db_job in db_jobs:
        if db_job[0] == fetched[0] and db_job[1] == fetched[1] and db_job[2] == fetched[2]:
            if db_job[3] != fetched[3] or db_job[4] != fetched[4]:
                updated_jobs.append(fetched)
            is_new = False
            break
    if is_new:
        new_jobs.append(fetched)

print(f"Jobs fetched: {len(fetched_jobs)}")
print(f"Jobs db: {len(db_jobs)}")
print(f"Jobs new: {len(new_jobs)}")
print(f"Jobs updated: {len(updated_jobs)}")

if len(updated_jobs) != 0: update_jobs(updated_jobs)
if len(new_jobs) != 0: add_new_jobs(new_jobs)

