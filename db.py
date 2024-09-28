#file -- db.py

# to call a go function , the following call is sent :
# 'functionname'('arguments')
# the response is in the form of a csv

#import time as tm
import json

class db :
    def __init__ (self,outfile,infile) :
        #self.outfileName = outfilename
        #self.outfile = open(self.outfileName)
        #self.infileName = infilename
        #self.infile = open(self.infileName)

        self.outfile = outfile
        self.infile = infile
    
    def createIncome (self,name:str,value:int,time:float) :
        jsoncmd = json.dumps({"cmd":"CreateIncome", "name":name, "value":value,"time":time})
        print(jsoncmd,file=self.outfile)
        #print("CreateIncome(",time,',',name,',',value,')',sep='',file=self.file)
     
    def createExpense (self,name:str,value:int,time:float) :
        jsoncmd = json.dumps({"cmd":"CreateExpense", "name":name, "value":value,"time":time})
        print(jsoncmd,file=self.outfile)
        #print("CreateExpense(",time,',',name,',',value,')',sep='',file=self.file)
    
    def getIncomeAtTime (self,time: float) :
        jsoncmd = json.dumps({"cmd":"GetIncomeAtTime","time" :time})
        print(jsoncmd,file=self.outfile)

        #print("GetIncomeAtTime(",time,")")
        #tmarr, name, value = [], [], []
        
        # jsonStr = ""
        # while True :
        #     instr = input()
        #     jsonStr += instr
        #     if instr == '}' :
        #         break
        
        return json.load(self.infile)

        # instr = input()
        # while True :
        #     instr = self.file.readline()
        #     if not instr :
        #         break
            
        #     split = instr.split(',')
        #     tmarr.append(float(split[0]))
        #     name.append(split[1])
        #     value.append(int(split[2]))
    
    def getExpenseAtTime (self,time: float) :
        jsoncmd = json.dumps({"cmd":"GetExpenseAtTime","time" :time})
        print(jsoncmd,file=self.outfile)

        #print("GetIncomeAtTime(",time,")")
        #tmarr, name, value = [], [], []
        
        # jsonStr = ""
        # while True :
        #     instr = input()
        #     jsonStr += instr
        #     if instr == '}' :
        #         break
        
        return json.load(self.infile)
