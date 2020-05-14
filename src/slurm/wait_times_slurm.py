import pyslurm
from datetime import datetime
import pandas as pd
import pwd

def get_wait(x):
  return datetime.now() - datetime.fromtimestamp(x)

def get_username_by_uid(uid):
   pwd.getpwuid(uid).pwd_name


def get_jobs_info():
  df = pd.DataFrame.from_dict(pyslurm.job().get()).T
  df['wait_time'] = df['submit_time'].apply(get_wait)
  df['user_name'] = df['user_id'].apply(get_username_by_uid)
  return df
  

def main():
  df = get_jobs_info()
  ## TODO check if job are not waiting for QOS

  print("Effective mean wait time: (with no QOS)")

  print("Quartiles:")
  print(df['wait_time'].quantile([0.25,0.5,0.85]))

  print("Mean wait time all active jobs:")
  print("%s with +/- %s " % (df['wait_time'].mean(),df['wait_time'].std()))

  ## What if there is lees than 10 jobs in the queue
  print("Top 10 wait time job without QOS")
  print(df.nlargest(10,'wait_time')[['user_name','wait_time','partition','job_state','state_reason', 'time_limit_str']])

  ## Number of job waiting for GPU

  ## User with most number of jobs
  
  

if __name__ == "__main__":
  main()
