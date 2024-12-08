#file -- db_alchemy.py

import sqlite3
import datetime

class Db:
    def __init__(self, db_file='test.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS incomes (
                tm TIMESTAMP,
                name TEXT,
                value REAL,
                PRIMARY KEY (tm,name)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                tm TIMESTAMP,
                name TEXT,
                value REAL,
                PRIMARY KEY (tm,name)
            )
        ''')
        self.conn.commit()

    def add_income(self,name,value, time):
        self.cursor.execute('''
            INSERT OR REPLACE INTO incomes (tm, name, value)
            VALUES (?, ?, ?)
        ''', (time, name, value))
        self.conn.commit()

    def add_expense(self,name,value,time):
        self.cursor.execute('''
            INSERT OR REPLACE INTO expenses (tm, name, value)
            VALUES (?, ?, ?)
        ''', (time, name, value))
        self.conn.commit()

    def update_income(self,name,value,time):
        self.cursor.execute('''
            UPDATE incomes 
            SET value = ?,tm = ?
            WHERE name = ?
        ''', (time, name, value))
        self.conn.commit()

    def update_expense(self,name,value,time):
        self.cursor.execute('''
            UPDATE expenses 
            SET value = ?,tm = ?
            WHERE name = ?
        ''', (time, name, value))
        self.conn.commit()

    def get_income(self, name):
        self.cursor.execute('SELECT * FROM incomes WHERE name = ?', (name,))
        return self.cursor.fetchall()

    def get_expense(self, name):
        self.cursor.execute('SELECT * FROM expenses WHERE name = ?', (name,))
        return self.cursor.fetchall()

    def get_income_by_name_time(self, name, tm):
        self.cursor.execute('SELECT * FROM incomes WHERE name = ? AND tm = ?', (name, tm))
        return self.cursor.fetchall()

    def get_expense_by_name_time(self, name, tm):
        self.cursor.execute('SELECT * FROM expenses WHERE name = ? AND tm = ?', (name, tm))
        return self.cursor.fetchall()

    def get_income_at_time(self, tm):
        self.cursor.execute('SELECT * FROM incomes WHERE tm = ?', (tm,))
        return self.cursor.fetchall()

    def get_expense_at_time(self, tm):
        self.cursor.execute('SELECT * FROM expenses WHERE tm = ?', (tm,))
        return self.cursor.fetchall()
    
    def delete_income (self, name,tm) :
        if tm == 0 :
            self.cursor.execute('DELETE FROM incomes WHERE name = ?', (name,))
        else :
            self.cursor.execute('DELETE FROM incomes WHERE name = ? AND tm = ?',(name,tm))
        return self.cursor.fetchall()

    def delete_expense (self, name,tm) :
        if tm == 0 :
            self.cursor.execute('DELETE FROM expenses WHERE name = ?', (name,))
        else :
            self.cursor.execute('DELETE FROM expenses WHERE name = ? AND tm = ?',(name,tm))
        return self.cursor.fetchall()

    
if __name__ == "__main__":
    db = Db()

    # Example usage
    income1 = {'tm': datetime.datetime.now(), 'name': 'Salary', 'value': 2000.0}
    income2 = {'tm': datetime.datetime.now(), 'name': 'Interest', 'value': 50.0}
    expense1 = {'tm': datetime.datetime.now(), 'name': 'Rent', 'value': 1000.0}

    # db.add_income(income1)
    # db.add_income(income2)  # Updates value if already exists (tm, name is primary key)
    # db.add_expense(expense1)
