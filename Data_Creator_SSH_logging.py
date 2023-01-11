from subprocess import call
from pandas import DataFrame as dt
import os
import sqlite3

class InvalidReadService(Exception):
    pass

class SSH():
    def __init__(self) -> None:
        
        call(f"chmod +x ./script.sh",shell=True)
        call("./script.sh",shell=True)

        self.Accepted_ipies=[]
        self.Data_Accepted_ipies=[]
        self.Rejected_ipies=[]
        self.Data_Rejected_ipies=[]
        self.iterator = 1
        
        self.conn = sqlite3.connect('Database.db')

        self.conn.execute('CREATE TABLE IF NOT EXISTS ACCEPTED_IPIES (IP text, CUANTITY text);')
        self.conn.execute('CREATE TABLE IF NOT EXISTS REJECTED_IPIES (IP text, CUANTITY text);')
        self.conn.commit()

        self.Reading_accepted_ipies()
        self.Reading_rejected_ipies()
        self.Creating_tables()
        
        


    # Metoda czytajaca z pliku numery ip, ktory udalo sie przprowadzic poprawny proces logowania
    def Reading_accepted_ipies(self):
        try:
            with open("./Accepted_ipies.txt","r") as file:
                cont= file.readlines()
                if len(cont) == 0:
                    raise InvalidReadService
                
                for i in cont:
            
            
                    data= i.strip()
                    data=i.split()
                    self.Accepted_ipies.append(data[1])
                    self.Data_Accepted_ipies.append(data[0])
        except InvalidReadService:
            print("Usluga nie wlaczona, albo brakuje danych do odczytu - ssh")
            exit()

    # Metoda czytajaca z pliku numery ip, ktorym nie udalo sie przprowadzic poprawny proces logowania
    def Reading_rejected_ipies(self):


        with open("./Rejected_ipies.txt","r") as file:
    
            cont = file.readlines()
            for i in cont:
                data= i.strip()
                data=i.split()
                self.Rejected_ipies.append(data[1])
                self.Data_Rejected_ipies.append(data[0])


    def Clear_all_variables(self):
        self.Accepted_ipies=[]
        self.Data_Accepted_ipies=[]
        self.Rejected_ipies=[]
        self.Data_Rejected_ipies=[]
    
    def Creating_tables(self):

        self.Correct_entries_ip= dt(index=self.Accepted_ipies,data=self.Data_Accepted_ipies,columns=["Udane logowania z poszczególnych numerów ip",])
        self.Reject_entries_ip= dt(index=self.Rejected_ipies,data=self.Data_Rejected_ipies,columns=["Nieudane logowania z poszczególnych numerów ip",])


    def Get_new_data(self):
        self.Clear_all_variables()
        call("./script.sh",shell=True)
        self.Reading_accepted_ipies()
        self.Reading_rejected_ipies()
        self.Creating_tables()
    
    def Show_results(self):
        print(self.Correct_entries_ip)
        print()
        print(self.Reject_entries_ip)
    
    def Write_into_database(self):

       

        
        
        

        self.Correct_entries_ip.to_sql('ACCEPTED_IPIES',self.conn,if_exists='replace',index=False)
        self.Reject_entries_ip.to_sql('REJECTED_IPIES',self.conn,if_exists='replace',index=False)

        self.conn.commit()
        
    
