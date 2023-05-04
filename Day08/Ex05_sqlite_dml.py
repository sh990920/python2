'''
파일명: Ex05-sqlite-dml.py
'''
import sqlite3
from datetime import datetime

hire_date = datetime.strptime('2022-03-01', '%Y-%m-%d').strftime('%Y-%m-%d')

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 데이터 삽입
sql = "INSERT INTO employees (first_name, last_name, email, hire_date, job_id, salary, department_id) " \
  "VALUES (?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('John', 'Doe', 'johndoe1@example.com', '2022-03-01', 'IT_PROG', 5000, 90))
conn.commit()
cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()



# 데이터 조회 
sql = "SELECT * FROM employees WHERE employee_id=?"
cur.execute(sql, (1,))
rows = cur.fetchall()
print("============1============")
print(rows)

cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 전체 조회
sql = "SELECT * FROM employees "
cur.execute(sql)
rows = cur.fetchall()
print("============2 전체조회============")
print(rows)

cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 데이터 수정
sql = "UPDATE employees SET salary=? WHERE employee_id =?"
cur.execute(sql, (5500, 1))
conn.commit()

cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 데이터 조회 
sql = "SELECT * FROM employees WHERE employee_id=?"
cur.execute(sql, (1,))
rows = cur.fetchall()
print("============3============")
print(rows)

cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()


# 데이터 삭제
sql = "DELETE FROM employees"
cur.execute(sql)
conn.commit()
cur.close()
conn.close()

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 전체 조회
sql = "SELECT * FROM employees "
cur.execute(sql)
rows = cur.fetchall()
print("============4 전체조회============")
print(rows)

cur.close()
conn.close()
