import json
import os
import time



class Fornax:

    def df():

        projectname = input("Proszę podać nazwę projektu: ")
        pywersja = input("Podaj wersję Python'a: ")
        plik = input("Proszę podać nazwę pliku w którym znajduje się projekt: ")

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

        zawartosc = {
            "name": f"{projectname}",
            "version": f"{pywersja}",
            "filename": f"{plik}",
            "time": f"{time_string}"
        }
        
        json_object = json.dumps(zawartosc, indent=4)

        filename = 'fxpackage.json'
        with open(filename, 'w') as f:
            f.write(json_object)

class FornaxDataCheckingSystem(Exception):

    def fosc():
        
        filesize = os.path.getsize("fxpackage.json")
        if filesize == 0:

            raise FornaxDataCheckingSystem("Pusty plik fxpackage.json")

        else:
            pass
            #print("Fdscs pomyślny")
        