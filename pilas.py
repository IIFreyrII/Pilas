class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía")

    def ver_cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("La pila está vacía")

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print(pila.ver_cima())  
print(pila.desapilar()) 
print(pila.esta_vacia()) 
