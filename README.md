README.md

# Mining dataset AI Pull Requests

'Task2.py': script to extract and process Repository data
* REPOID: Data related to `id`
* LANG: Data related to `language`
* STARS: Data related to `stars`
* REPOURL: Data related to `url`

'Task4.py': script to extract and process Commit Details
* PRID: Data related to `pr_id`
* PRSHA: Data related to `sha`
* PRCOMMITMESSAGE: Data related to `message`
* PRFILE: Data related to `filename`
* PRSTATUS: Data related to `status`
* PRADDS: Data related to `additions`
* PRDELSS: Data related to `deletions`
* PRCHANGECOUNT: Data related to `changes`
* PRDIFF: Data related to `patch`. Please remove special characters in the diff to avoid string encoding errors. 

## Install Requirements
pip install pandas pyarrow huggingface_hub

## Data source
[hao-li/AIDev] (https://huggingface.co/datasets/hao-li/AIDev)
Tables used for task 2 and 4: 'all_repository', 'pr_commit_details'