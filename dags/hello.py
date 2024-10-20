from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Suriya',
    'start_date': datetime(2024, 10,19),
    'catchup': False
}

dag = DAG('hello_world',
          default_args=default_args,
          schedule=timedelta(days=1))

t1 = BashOperator(task_id="hello",
                  bash_command='echo "Hello World!"',
                  dag=dag)

t2 = BashOperator(task_id="kubernetes",
                  bash_command='echo "Hello kubernetes!"',
                  dag=dag)

t1 >> t2
