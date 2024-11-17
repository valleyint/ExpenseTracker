package database

import (
	"time"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Db struct {
	db *gorm.DB
}

type Income struct {
	gorm.Model
	Tm    time.Time `gorm:"primaryKey"`
	Name  string    `gorm:"primaryKey"`
	Value float64
	// expense []*income `gorm:"many2many:expense_incomes;foreignKey"`
}

type Expense struct {
	gorm.Model
	Tm    time.Time `gorm:"primaryKey"`
	Name  string    `gorm:"primaryKey"`
	Value float64
	// incomes []*income `gorm:"many2many:income_expenses;"`
}

func CreateFianances() (*Db, error) {
	d := Db{}
	var err error

	d.db, err = gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	d.db.AutoMigrate(&Income{}, &Expense{})

	return &d, nil
}

func (d *Db) AddIncome(i Income) {
	if len(d.GetIncomeNameTime(i.Name,i.Tm)) == 0 {
		d.db.Create(&i)
	} else {
		d.db.Raw("UPDATE incomes SET value = ? WHERE tm = ?, name = ?",i.Value,i.Tm,i.Name)
	}
}

func (d *Db) AddExpense(e Expense) {
	if len(d.GetExpenseNameTime(e.Name,e.Tm)) == 0 {
		d.db.Create(&e)
	} else {
		d.db.Raw("UPDATE incomes SET value = ? WHERE tm = ?, name = ?",e.Value,e.Tm,e.Name)
	}
}

func (d *Db) GetIncome (name string) ([]Income) {
	var incomes []Income
	d.db.Raw("SELECT tm, name, value FROM incomes WHERE name = ?", name).Scan(incomes)
	return incomes
} 

func (d *Db) GetExpense (name string) ([]Expense) {
	var expenses []Expense
	d.db.Raw("SELECT tm, name, value FROM expenses WHERE name = ?", name).Scan(expenses)

	return expenses
}

func (d *Db) GetExpenseNameTime (name string, tm time.Time) ([]Expense) {
	var expenses []Expense
	d.db.Raw("SELECT tm, name, value FROM expenses WHERE name = ?, tm = ?", name).Scan(expenses)

	return expenses
}

func (d *Db) GetIncomeNameTime (name string, tm time.Time) ([]Expense) {
	var expenses []Expense
	d.db.Raw("SELECT tm, name, value FROM incomes WHERE name = ?, tm = ?", name).Scan(expenses)

	return expenses
}


func (d *Db) GetIncomeAtTime(tm time.Time) ([]Income) {
	var incomes []Income
	d.db.Raw("SELECT tm, name, value FROM incomes WHERE tm = ?", tm).Scan(incomes)
	return incomes
}

func (d *Db) GetExpenseAtTime(tm time.Time) ([]Expense) {
	var expenses []Expense
	d.db.Raw("SELECT tm, name, value FROM expenses WHERE tm = ?", tm).Scan(expenses)

	return expenses
}

func (d *Db) GetAtTime(tm time.Time) ([]Income, []Expense) {
	return d.GetIncomeAtTime(tm),d.GetExpenseAtTime(tm)
}
