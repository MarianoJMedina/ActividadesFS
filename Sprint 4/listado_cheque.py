import sys
import os
import pathlib
import csv
import datetime

if __name__ == "__main__":
    if len(sys.argv) <= 4:
        print("Por favor, ingresa los argumentos correctos")
    else:
        nombre_archivo = sys.argv[1]
        dni = sys.argv[2]
        salida = sys.argv[3]
        tipo = sys.argv[4]
        estado = sys.argv[5]

        if salida == "PANTALLA":
            with open(nombre_archivo, 'r', newline='') as archivo_csv:
                reader = csv.reader(archivo_csv)
                for linea in reader:
                    if dni == linea[8] and tipo == linea[9] and estado == linea[10]:
                        os.system('cls')
                        print(f'Nro Cheque: {linea[0]}')
                        print(f'Codigo Banco: {linea[1]}')
                        print(f'Codigo Sucursal: {linea[2]}')
                        print(f'Nro Cuenta Origen: {linea[3]}')
                        print(f'Nro Cuenta Destino: {linea[4]}')
                        print(f'Valor: {linea[5]}')
                        print(f'Fecha Origen: {linea[6]}')
                        print(f'Fecha Pago: {linea[7]}')
                        print(f'DNI: {linea[8]}')
                        print(f'Tipo: {linea[9]}')
                        print(f'Estado: {linea[10]}')
                        print('-'*50)
                        break
                    else:
                        print("Cheque no encontrado")

        if salida == "CSV":
            with open(nombre_archivo, 'r', newline='') as archivo_csv1:
                reader = csv.reader(archivo_csv1)
                for linea in reader:
                    if dni == linea[8] and tipo == linea[9] and estado == linea[10]:
                        
                        campos = ['Fecha Origen', 'Fecha Pago', 'Valor', 'Nro Cuenta Origen']

                        tday = datetime.date.today()
                        archivo_nuevo = dni+"_"+str(tday)+".csv"

                        if not pathlib.Path(archivo_nuevo).exists():
                            with open(archivo_nuevo, "w", newline='') as archivo_csv2:
                                writer = csv.DictWriter(archivo_csv2, fieldnames=campos)
                                writer.writeheader()
                        
                        with open(archivo_nuevo, "a", newline='') as archivo_csv2:
                            writer = csv.DictWriter(archivo_csv2, fieldnames=campos)
                            writer.writerow({'Fecha Origen': linea[6], 'Fecha Pago': linea[7], 'Valor': linea[5], 'Nro Cuenta Origen': linea[3]})
                            

                       







            
                




