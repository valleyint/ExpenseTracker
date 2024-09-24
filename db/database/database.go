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
	d.db.Create(&i)
}

func (d *Db) AddExpense(e Expense) {
	d.db.Create(&e)
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
