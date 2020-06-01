import pyslurm
import pandas as pd
from tabulate import tabulate

from datetime import datetime
import argparse
import pwd

def get_wait(x):
  """Get time difference between timestamp and now

  Paramaters
  ----------
  str
      Timestamp with the format of Slurm

  Returns
  -------
  deltatime
     difference time
  """
  return datetime.now() - datetime.fromtimestamp(x)


def get_username_by_uid(uid):
  """Get user name by uid of the system

  Paramaters
  ----------
  str
      uid

  Returns
  -------
  str
     user name
  """

  return pwd.getpwuid(uid).pw_name


def get_jobs_info():
  """Get information of jobs in the queue
    
    Returns
    -------
    Dataframe
        Information of the jobs in the queue with wait time and user name
  """

  df = pd.DataFrame.from_dict(pyslurm.job().get()).T
  df['wait_time'] = df['submit_time'].apply(get_wait)
  df['user_name'] = df['user_id'].apply(get_username_by_uid)
  return df

  
def get_jobs_waiting_partition(jobs, p=None, reasons=None):
  """Return the number of jobs waiting in a specific queue

  Parameters
  ----------
  df: DataFrame
    data frame with the information of the jobs
  p: str
    name of the partition. If none is specified, all queues are taking into account
  raesons: list(str)
    names of the reasons that are valid. If none is specified all reasons are valid.
    the name of the reason must match with the ones in slurm. 
    

  Returns
  -------
  Dataframe
     Selected jobs
  """
  selected_jobs = pd.DataFrame()
  # Selected by partition
  if(p is not None):
    selected_jobs = jobs[jobs['partition'] == p]
   
  # A job that is waiting is a jobs that is not running
  selected_jobs = selected_jobs[~(selected_jobs['job_state'] == 'RUNNING')]
  
  # Selected valid reasons
  if(reasons is not None and len(reasons) > 0):
    selected_jobs = selected_jobs[selected_jobs['state_reason'].isin(reasons)]
  return selected_jobs

def printTabulate(df, headers='keys', tablefmt='psql'):
  """Wrapper to print df using tabulate
  """
  if(isinstance(df, pd.Series)):
    print(df.to_string())
    return
  print(tabulate(df, headers=headers, tablefmt=tablefmt))


def main():
  parser = argparse.ArgumentParser(prog='squeue-apolo',
                                   description='''
                                               A custom utility to get information 
                                               about Apolo's queue state''',
                                   epilog='''
                                   Only jobs waiting for valid reasons are take into
                                   account to display information. Valid reasons are:
                                   Resources, Priority and Reservation; not QOS reasons''')
  args = parser.parse_args()
  ## TODO use args to create special behavior

  df = get_jobs_info() 
  
  print("Mean wait time of all active jobs:")
  print("%s with +/- %s" % (df['wait_time'].mean(),df['wait_time'].std()))
  print()

  print("Quartiles:")
  printTabulate(df['wait_time'].quantile([0.25,0.5,0.85]))
  print()

  print("Top 10 wait time jobs")
  printTabulate(df.nlargest(10,'wait_time')[['user_name','wait_time','partition','job_state','state_reason', 'time_limit_str']])
  print()

  valid_reasons_to_wait = ['Resources', 'Reservation', 'Priority']
  n_accel_waiting_jobs = len(get_jobs_waiting_partition(df, 'accel', valid_reasons_to_wait))
  n_accel_2_waiting_jobs =  len(get_jobs_waiting_partition(df, 'accel-2', valid_reasons_to_wait))

  print("Number of Jobs Waiting for GPU")
  print("Accel:    %i" % n_accel_waiting_jobs)
  print("Accel-2:  %i" % n_accel_2_waiting_jobs)
  print("Total:    %i" % (n_accel_waiting_jobs + n_accel_2_waiting_jobs))
  print()
  print("Top 5 users by number of active jobs")
  printTabulate(df.groupby('user_name')['job_id'].agg('count').nlargest(5))
  print()
  print("Generated at: %s" % datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

  
if __name__ == "__main__":
  main()
