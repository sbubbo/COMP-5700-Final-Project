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

print(f"len(pr_task_type_df): {len(pr_task_type_df)}")