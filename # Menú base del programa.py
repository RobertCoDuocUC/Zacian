
def datos_Francisco():
 print("Mi nombre es Francisco Salas y tengo 21 años.")

def datos_roberto():
    print("Mi nombre es Roberto Cornejo y tengo 20 años.")
    
# Menú base del programa
while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Función de integrante 1")
 print("2. Función de integrante 2")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
    input("Programa finalizado.")
    break
 elif op == "1":
    datos_roberto()
 elif op == "2":
    datos_Francisco() 
 else:
    print(" Opción inválida.")
