

class Persona(object):
    def __init__(self, nombre, edad, altura,peso,tipoS,alergias,sintomas):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.tipoS = tipoS
        self.alergias = alergias
        self.sintomas = sintomas

class Hash(object):
    def __init__(self):
        self.listP = [None]*100000
    def insert(self,p):
        hash = self.hashing(p.nombre)
        if(self.listP[hash]==None):
            self.listP[hash] = [p]
        else:
            self.listP[hash].append(p)
    def search(self,nombre):
        hash = self.hashing(nombre)
        
        if(self.listP[hash]==None):
            return None
        else:
            for i in self.listP[hash]:
                if i.nombre == nombre:
                    return i
            return None
    def delete(self,p):
        hash = self.hashing(p.nombre)
        if(self.listP[hash]==None):
            return False
        else:
            a = self.listP[hash].index(p)
            if(a == -1):
                return False
            else:
                self.listP[hash].pop(a)
                return True
    def hashing(self,str):
        hash = 5381
        for i in range(len(str)):
            c = ord(str[i])
            hash = hash*33+c
        return hash%100000

