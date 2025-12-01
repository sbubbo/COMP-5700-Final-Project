# Pull data from all_pull_requests and create CSV file with the following columns:
# - TITLE: Data related to `title`
# - ID: Data related to `id`
# - AGENTNAME: Data related to `agent`
# - BODYSTRING: Data related to `body`
# - REPOID: Data related to `repo_id`
# - REPOURL: Data related to `repo_url` 

import csv
import json
import pandas as pd

all_pr_df = pd.read_parquet("hf://datasets/hao-li/AIDev/all_pull_request.parquet")

# Testing that all_pr_df is loaded correctly
#print(f"len(all_pr_df): {len(all_pr_df)}")

columns_to_keep = ['title', 'id', 'agent', 'body', 'repo_id', 'repo_url']
task_1 = all_pr_df[columns_to_keep]
task_1 = task_1.rename(columns={'title': 'TITLE', 'id': 'ID', 'agent': 'AGENTNAME', 'body': 'BODYSTRING', 'repo_id': 'REPOID', 'repo_url': 'REPOURL'})

task_1.to_csv("task_1_output.csv", index=False, quoting=csv.QUOTE_ALL)