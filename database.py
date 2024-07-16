from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs")).fetchall()
 # first_result = result[0]
 # first_result_dict = dict(first_result._mapping)
 # print(first_result_dict)
 # print(type(first_result_dict))


##here by default the result is in the form of sqlalchemy legacy rows,we need to convert into python dictionary

#result_dicts = []
#for row in result:
#  result_dicts.append(dict(row._mapping))

#print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs")).fetchall()
    jobs = []
    for row in result:
      jobs.append(dict(row._mapping))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs where id = {id}")).fetchall()
##if there are no rows in the table,for suppose if id is not present in the table,then table does not return any row,so len(result) will be 0,if we give id which is present in the table,then len(result) will be 1,so it return 1st row which is the only row in the table,so we can use this condition to check if result is empty or not.
    if len(result) == 0:
      return None
    else:
      return dict(result[0]._mapping)
  