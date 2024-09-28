package database

import (
	"fmt"
	"testing"
	"time"
)

func TestDatabase (t *testing.T) {
	d, err := CreateFianances()
	if err != nil {
		panic(err)
	}

	now := time.Now()
	for loop := 0; loop < 5; loop++ {
		d.AddExpense(Expense{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64(loop)})
		d.AddIncome(Income{Tm: now.Add(time.Duration(int64(time.Second) * int64(loop))), Name: "test", Value: float64((loop)) * 2})
	}

	for loop := 0; loop < 10; loop++ {
		fmt.Println(d.GetAtTime(now.Add(time.Duration(int64(time.Second) * int64(loop)))))
	}
}
