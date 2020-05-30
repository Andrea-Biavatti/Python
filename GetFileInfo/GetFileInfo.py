import time
import os

print("Criado por Heitor Bisneto em 05/03/20.")
print("Copyright © 2020 Heitor. All rights reserved.")
print()
SoftwareName = "Get Info"
print("App Name: ", SoftwareName + " [Versão 1.0]")
print("")
Separator = ("=" * 20)
print(Separator + " " + SoftwareName + " " + Separator)
print()

MyDir = 'C:/'
with os.scandir(MyDir) as entries:
    for entry in entries:
        if entry.is_file():
            #Criado = os.stat(entry).st_ctime
            Criado = time.strftime('%d %m %Y', time.gmtime(os.stat(entry).st_ctime))
            Modificado = time.strftime('%d %m %Y', time.gmtime(os.path.getmtime(entry)))

            print("Nome do arquivo: ",entry.name)
            print("Criado em: ",Criado)
            print("Modificado em: ",Modificado)
            print()
