import asyncio
import time
from adap import STFF_Adapter

def query1():   
    """The right call of function with all needed data""" 
    func = STFF_Adapter()
    result = asyncio.run(func.update_Renew_Reservation(['A1_A3', 3, False]))
    print(result)

def query2():
    """The right call of function with all needed data"""
    func = STFF_Adapter()
    result = func.select_DefineSTFFCell(['21f9f975-6838-11ea-8fdb-001d6001edc0'])
    print(result)

def query3():
    """The wrong call of function with an error in the data list (the lack or excess of parameters)"""
    func = STFF_Adapter()
    result = asyncio.run(func.update_Renew_Reservation(['A1_A3', 3]))
    print(result)

def query4():
    """The wrong call of function with an error in data list (the lack or excess of parameters)"""
    func = STFF_Adapter()
    result = func.select_DefineSTFFCell(['21f9f975-6838-11ea-8fdb-001d6001edc0', 'extra parameter'])
    print(result)    


query1()
query2()
query3()
query4()


