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
print(f"len(pr_task_type_df): {len(pr_task_type_df)}")

columns_to_keep = ['id', 'title', 'reason', 'type', 'confidence']

pr_task_type_df.to_csv("pr_task_type.csv", columns=columns_to_keep, index=False, quoting=csv.QUOTE_ALL)