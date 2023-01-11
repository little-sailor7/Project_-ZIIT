from subprocess import call
from pandas import DataFrame as dt
import sqlite3

class InvalidReadService(Exception):
    pass

class HTTP_DATA():
    def __init__(self) -> None:

        

        call(f"chmod +x ./HTTP.sh",shell=True)
        call("./HTTP.sh",shell=True)

        self.connected_ipies=[]
        self.appearence = []

        self.conn = sqlite3.connect('Database.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS HTTP_TABLE (IP text, CUANTITY text);')
        
        self.Read_Data()

        self.Create_table()

    def Read_Data(self):
        
        try:
            with open("./HTTP_IPIES.txt","r") as file:
                cont = file.readlines()
                if len(cont) == 0:
                    raise InvalidReadService
                else:
                    for i in cont:
                
                
                        data= i.strip()
                        data=i.split()

                        self.connected_ipies.append(data[1])
                        self.appearence.append(data[0])
        except InvalidReadService:
            print("Usluga niewlaczona, albo brak danych do odczytu - http")
            exit()
        

    def Create_table(self):
        self.http_table_ipies = dt(index=self.connected_ipies,data=self.appearence,columns=["Ilosc polaczen z poszczegolnych numerow IP"])
    
    def Clear_all_var(self):
        self.connected_ipies=[]
        self.appearence = []
    
    def Get_new_data(self):

        self.Clear_all_var()

        call("./HTTP.sh",shell=True)

        self.Read_Data()
        
        self.Create_table()


    def Show_Result(self):
        print(self.http_table_ipies)
    
    def Write_into_database(self):

       

        
        
        

        self.http_table_ipies.to_sql('HTTP_TABLE',self.conn,if_exists='replace',index=False)
        

        self.conn.commit()
        