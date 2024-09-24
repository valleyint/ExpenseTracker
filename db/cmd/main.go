package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os/exec"
	"time"

	"db/database"
)

const (
	pythonVersion = "python3.12"
	fileCommand   = "../../testDbConnector.py"
)

func main() {
	c, err := newController()
	if err != nil {
		panic(err)
	}

	ch := make(chan bool, 1)
	go c.runCommand(ch)

	decoder := json.NewDecoder(*c.stdout)
	for {
		var req request
		err := decoder.Decode(&req)
		if err != nil {
			log.Println(err)
		}
		c.handleRequest(req)
		select {
		case msg := <-ch:
			if msg {
				return
			}
		default:
			continue
		}
	}
}

type controller struct {
	stdout *io.ReadCloser
	stdin  *io.WriteCloser
	db     *database.Db
	cm     *exec.Cmd
}

type request struct {
	Cmd   string
	Time  int64 `json:"string"`
	Name  string
	Value int
}

func newController() (*controller, error) {
	c := controller{}
	var err error

	c.db, err = database.CreateFianances()
	if err != nil {
		panic(err)
	}

	c.cm = exec.Command(pythonVersion, fileCommand)

	stdin, err := c.cm.StdinPipe()
	if err != nil {
		return nil, err
	}
	c.stdin = &stdin

	stdout, err := c.cm.StdoutPipe()
	if err != nil {
		return nil, err
	}
	c.stdout = &stdout

	return &c, nil
}

func (c *controller) runCommand(ch chan bool) {
	err := c.cm.Start()
	if err != nil {
		panic(err)
	}

	err = c.cm.Wait()
	if err != nil {
		panic(err)
	}
	ch <- true
}

func (c *controller) handleRequest(req request) {
	// var req request
	// err := json.Unmarshal([]byte(reqStr), req)
	// if err != nil {
	// 	log.Println(err)
	// }
	fmt.Println(req)

	switch req.Cmd {
	case "CreateIncome":
		//time,name,value
		dbvals := database.Income{Tm: time.Unix(req.Time, 0), Name: req.Name, Value: float64(req.Value)}
		c.db.AddIncome(dbvals)

	case "CreateExpense":
		dbvals := database.Expense{Tm: time.Unix(req.Time, 0), Name: req.Name, Value: float64(req.Value)}
		c.db.AddExpense(dbvals)

	case "GetIncome":
		incomes := c.db.GetIncomeAtTime(time.Unix(req.Time, 0))
		resJson, err := json.Marshal(incomes)
		if err != nil {
			log.Println(err)
		}
		io.WriteString(*c.stdin, string(resJson))
	case "GetExpense":
		expenses := c.db.GetIncomeAtTime(time.Unix(req.Time, 0))
		expJson, err := json.Marshal(expenses)
		if err != nil {
			log.Println(err)
		}
		io.WriteString(*c.stdin, string(expJson))
	}
}
