package database

import (
	"context"
	"database/sql"
	"log"

	_ "modernc.org/sqlite"
)

const (
	dbpath = ""
)

type db struct {
	db *sql.DB
}


func OpenDB () *db {
	d := db{}
	var err error
	d.db ,err = sql.Open("sqlite",dbpath)
	if err != nil {
		log.Println(err)
		return nil
	}

	_, err = d.db.ExecContext(context.Background(), `
		CREATE TABLE IF NOT EXISTS finance {
			date DATE NOT NULL,
			time TIME NOT NULL
			PRIMARY KEY (date,time)
		}
	
		CREATE TABLE IF NOT EXISTS income {
			date  DATE			NOT NULL,
			time  TIME 			NOT NULL,
			name  VARCHAR(100)	NOT NULL,
			value INT			NOT NULL
			PRIMARY KEY (date,time,name)
			FOREIGN KEY (date,time) REFERENCES fiance (date,time)
		} 
		
		CREATE TABLE IF NOT EXISTS expense {
			date  DATE			NOT NULL,
			time  TIME 			NOT NULL,
			name  VARCHAR(100)	NOT NULL,
			value INT			NOT NULL
			PRIMARY KEY (date,time,name)
			FOREIGN KEY (date,time) REFERENCES fiance (date,time)
		} 
	`)
	return &db{}
}
