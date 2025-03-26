'''Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).'''

class Producto:
    
    def __init__(self,nombre, precio , cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def valor_total(self):
        total = self.precio * self.cantidad   
        print(f"TOTAL INVENTARIO: {total}€.")
                   
              
producto1 = Producto("laptop",665,5)#3325
producto1.valor_total()

producto2 = Producto("Monitor",100,10)
producto2.valor_total()

total = Producto
total.valor_total(producto1,producto2)   
