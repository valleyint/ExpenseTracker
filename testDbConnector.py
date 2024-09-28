import sys
import db
import time

d = db.db(outfile=sys.stdout,infile=sys.stdin)

now = time.time()

d.createIncome(name="testIncome",value=100000,time=now)
d.createExpense(name="testIncome",value=50000,time=now)

#print(d.getExpenseAtTime(time=now))