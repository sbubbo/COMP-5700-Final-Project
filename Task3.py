# Pull data from pr_task_type and create CSV file with the following columns:
# - PRID: Data related to `id`
# - PRTITLE: Data related to `title`
# - PRREASON: Data related to `reason`
# - PRTYPE: Data related to `type`
# - CONFIDENCE: Data related to `confidence`

import csv
import json
import pandas as pd

pr_task_type_df = pd.read_parquet("hf://datasets/hao-li/AIDev/pr_task_type.parquet")

# Testing that pr_task_type_df is loaded correctly
#print(f"len(pr_task_type_df): {len(pr_task_type_df)}")

columns_to_keep = ['id', 'title', 'reason', 'type', 'confidence']
task_2 = pr_task_type_df[columns_to_keep]
task_2 = task_2.rename(columns={'id': 'PRID', 'title': 'PRTITLE', 'reason': 'PRREASON', 'type': 'PRTYPE', 'confidence': 'CONFIDENCE'})

task_2.to_csv("task_3_output.csv", index=False, quoting=csv.QUOTE_ALL)