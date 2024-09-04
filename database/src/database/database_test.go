package database_test

import (
	"expensetracker/database"
	"fmt"
	"testing"
	"time"
)

func TestDatabase(t *testing.T) {
	d, err := database.CreateFianances()
	if err != nil {
		panic(err)
	}

	now := time.Now()
	for loop := 0; loop < 10; loop++ {
		d.AddExpense(database.Expense{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64(loop)})
		d.AddIncome(database.Income{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64((loop)) * 2})
	}

	for loop := 0; loop < 10; loop++ {
		fmt.Println(d.GetAtTime(now.Add(time.Duration(int64(time.Second) * int64(loop)))))
		fmt.Println()
	}
}

func TestDBSimple(t *testing.T) {
	d, err := database.CreateFianances()
	if err != nil {
		panic(err)
	}

	now := time.Now()
	for loop := 0; loop < 5; loop++ {
		d.AddExpense(database.Expense{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64(loop)})
		d.AddIncome(database.Income{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64((loop)) * 2})
	}

	//fmt.Println(d.GetAllIncome())
}
