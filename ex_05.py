from ex_04_selecty import *

from ex_03 import *
conn = create_connection("database.db")
a=select_all(conn, "projects")
print(a)

b=select_all(conn, "tasks")
print(b)



# wszystkie zadania dla projektu o id 1

c=select_where(conn, "tasks", projekt_id=1)
print(c)
# wszystkie zadania ze statusem ended

d=select_where(conn, "tasks", status="ended")
print(d)
