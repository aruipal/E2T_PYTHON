'''Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).'''

class Producto:
    
    inventario = {}
    precio_total = []
    
    def __init__(self,nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def meter_productos(self):
        self.inventario[self.nombre] = {"precio":self.precio, "cantidad":self.cantidad}
        #print(self.inventario)
        
    def valor_total(self):
        for i in self.inventario.values():
            total = self.precio * self.cantidad
            self.precio_total.append(total)  
        print(f"TOTAL INVENTARIO: {sum(self.precio_total)}€.")
                   
              
producto1 = Producto("laptop",665,5)
producto1.meter_productos()

producto2 = Producto("tablet",339,10)
producto2.meter_productos()

producto3 = Producto("PC",859,8)
producto3.meter_productos()

producto2.valor_total()