# Columns:
# - ID: ID of the pull request 
# - AGENT: The name of the agent that was used to create the pull request 
# - TYPE: The type of the pull request 
# - CONFIDENCE: The confidence of the pull request 
# - SECURITY: A Boolean flag (1/0) that will report the status of the security status of the pull request. 
#             If security-related keywords appear in a body or title of the pull request, then the value will 
#             be 1, 0 otherwise. Use the keywords from the list in `References`
# Security keywords: race, racy, buffer, overflow, stack, integer, signedness, underflow, improper, unauthenticated, 
#                    gain access, permission, cross site, css, xss, denial service, dos, crash, deadlock, injection, request forgery, csrf, 
#                    xsrf, forged, security, vulnerability, vulnerable, exploit, attack, bypass, backdoor, threat, expose, breach, violate, 
#                    fatal, blacklist, overrun, and insecure.

import csv
import pandas as pd
import os

# --- Task 5 ---

security_keywords = [
    "race", "racy", "buffer", "overflow", "stack", "integer", "signedness",
    "underflow", "improper", "unauthenticated", "gain access", "permission",
    "cross site", "css", "xss", "denial service", "dos", "crash", "deadlock",
    "injection", "request forgery", "csrf", "xsrf", "forged", "security",
    "vulnerability", "vulnerable", "exploit", "attack", "bypass", "backdoor",
    "threat", "expose", "breach", "violate", "fatal", "blacklist", "overrun",
    "insecure"
]
security_keywords = [kw.lower() for kw in security_keywords]

# ---------------------------
# LOAD RELEVANT CSV FILES
# ---------------------------
pulls = pd.read_csv("task_1_output.csv")         # TITLE, ID, AGENTNAME, BODYSTRING, ...
types = pd.read_csv("task_3_output.csv")              # PRID, PRTITLE, PRREASON, PRTYPE, CONFIDENCE

# ---------------------------
# MERGE ON PR ID
# ---------------------------
merged = pulls.merge(
    types,
    left_on="ID",
    right_on="PRID",
    how="left"
)

# ---------------------------
# FUNCTION FOR SECURITY CHECK
# ---------------------------
def has_security_keyword(title, body):
    text = f"{str(title)} {str(body)}".lower()
    return 1 if any(kw in text for kw in security_keywords) else 0

# ---------------------------
# APPLY SECURITY FLAG
# ---------------------------
merged["SECURITY"] = merged.apply(
    lambda row: has_security_keyword(row["TITLE"], row["BODYSTRING"]),
    axis=1
)

# ---------------------------
# RENAME COLUMNS FOR FINAL OUTPUT
# ---------------------------
merged.rename(columns={
    "ID": "ID",
    "AGENTNAME": "AGENT",
    "PRTYPE": "TYPE",
    "CONFIDENCE": "CONFIDENCE"
}, inplace=True)

# ---------------------------
# CHOOSE ONLY FINAL COLUMNS
# ---------------------------
final_df = merged[["ID", "AGENT", "TYPE", "CONFIDENCE", "SECURITY"]]

# ---------------------------
# WRITE OUTPUT
# ---------------------------
output_file = "task_5_output.csv"
final_df.to_csv(output_file, index=False)

print(f"Task 5 Output saved to {output_file}")