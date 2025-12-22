
arquivo = open("/Users/alemart/PythonProjects/Python_DIO/Arquivos/teste2.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")

arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

arquivo.close()
