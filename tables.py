import tkinter as tk
from tkinter import ttk


SMALL_FONT = ('Verdana', 8)

class SimpleTable(ttk.Frame):
    def __init__(self, parent, today):

        ttk.Frame.__init__(self, parent)
        self.topLabs = []
        global today1
        today1 = today
        columns = 20
        
        for column in range(columns):
            label = ttk.Label(self, text=str(int((today%365)%30)+1)+'/'+str(int((today%365)/30)+1)+'/'+str(int(today/365)-2000),
                              font=SMALL_FONT)
            today = today + 365.0/2
            label.grid(row=0, column=column+1)
            self.topLabs.append(label)

        self.leftLab1 = ttk.Label(self,text='P [kg/ha]')
        self.leftLab2 = ttk.Label(self,text='K [kg/ha]')
        self.leftLab3 = ttk.Label(self,text='S [kg/ha]')
        self.leftLab1.grid(row=1, column=0)
        self.leftLab2.grid(row=2, column=0)
        self.leftLab3.grid(row=3, column=0)
        
            
        self.var = {}
        for row in range(3):
            if row == 0:
                for column in range(columns):
                    self.var[column] = tk.StringVar()
                    ent = ttk.Entry(self, width=4, textvariable=self.var[column])
                    ent.grid(row=row+1, column=column+1, padx=1, pady=1, sticky='nsew')
                    if column%2 != 0:
                        self.var[column].set(24)
                    else:
                        self.var[column].set(0)
            elif row == 1:
                for column in range(columns):
                    self.var[columns+column] = tk.StringVar()
                    ent = ttk.Entry(self, width=4, textvariable=self.var[columns+column])
                    ent.grid(row=row+1, column=column+1, sticky="nsew", padx=1, pady=1)
                    if (columns+column)%2 != 0:
                        self.var[columns+column].set(30)
                    else:
                        self.var[columns+column].set(0)
            elif row == 2:
                for column in range(columns):
                    self.var[2*columns+column] = tk.StringVar()
                    ent = ttk.Entry(self, width=4, textvariable=self.var[2 * columns+column])
                    ent.grid(row=row+1, column=column+1, sticky="nsew", padx=1, pady=1)
                    if (2*columns+column)%2 != 0:
                        self.var[2*columns+column].set(20)
                    else:
                        self.var[2*columns+column].set(0)

    def getVal(self):
        TFert = []
        massP = []
        massK = []
        massS = []
        for col in range(20):
            TFert.append(today1+col*365.0/2)
            massP.append(float(self.var[col].get()))
            massK.append(float(self.var[20+col].get()))
            massS.append(float(self.var[20*2+col].get()))
            
        return TFert, massP, massK, massS

