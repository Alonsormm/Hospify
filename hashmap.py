

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
            listP[hash].append(p)
    def search(self,p):
        hash = self.hashing(p.nombre)
        
        if(self.listP[hash]==None):
            return None
        else:
            a = self.listP[hash].index(p)
            if(a == -1):
                return None
            else:
                return self.listP[hash][a]
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

