import db_alchemy as db
import time

d = db.Db()
d.create_tables()
d.add_expense("aex",100,time.time())
d.add_income("ain",100,time.time())

print(d.get_income('ain'),d.get_expense('aex'),sep='\n')