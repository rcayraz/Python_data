   
def Hola(nombre):
        try:
            return ({"Saludo":"Hola Como estas","Nombre":nombre})   
        
        except Exception as e: 
            print("Error: {0}".format(e))
            
            
print(Hola("roberto")    )        