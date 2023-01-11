#!/bin/python

#Zaimportowane moduly
try:
    from subprocess import call
    from Data_Creator_SSH_logging import SSH
    from Conections_by_HTTP import HTTP_DATA
    
except:
    print("Pojawil sie problem z zaimportowaniem potrzebnych modulow")

##################################

#Glowna klasa
class Presentation():

    # kostruktor tworzacy zmienne klasowe oraz wywolujacy komendy zmian uprawnien do skryptu bashowego i wywolucy go
    def __init__(self) -> None:
        self.SSH = SSH()
        self.HTTP = HTTP_DATA()
        self.service= []
        

        with open("./Service.txt","r") as file:
            self.service =file.readlines()
        
        
    def Change_actual_service(self,num=0):
        
        if num == "1":
            return self.service[0]
        else:
            return self.service[1]
       
    



Present=Presentation()

service ="1"
while True:

    inp = input(f"""Wybierz:\n
    1. Pokaz aktualne wyniki badania uslugi {Present.Change_actual_service(service)}\n
    2. Pobierz nowe wyniki\n
    3. Zmien usluge\n
    4. Zapisz wyniki do plikow .db \n""")
    

    if inp =="1" and service == "1":
        
        Present.SSH.Show_results()
        input()
        call("clear")

    elif inp == "1" and service == "2":
        Present.HTTP.Show_Result()
        input()
        call("clear")
    
    if inp=="2" and service == "1":
        Present.SSH.Get_new_data()
        call("clear")


    elif inp =="2" and service == "2":
        Present.HTTP.Get_new_data()
        call("clear")
        
    #3 Zrobic
    
    if inp == "3":
        call("clear")
        service = input('''Jaka usluge sprawdzic:\n
        1) SSHD\n
        2) HTTP\n''')
        call("clear")
    
    if inp == "4" and service=="1":
        try:
            Present.SSH.Write_into_database()
        except:
            print("Brakuje danych do zapisu")
    
    if inp =="4" and service == "2":
        try:
            Present.HTTP.Write_into_database()
        except:
            print("Brakuje danych do zapisu")
            exit()
    
    

    
    









