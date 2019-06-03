class Node:
  def __init__(self,data,prio):
    self.data = data
    self.prio = prio
    self.sig = None
  def imprimirNodo(self):
    print(self.data)

class Cola:
  def __init__(self):
    self.head = None
    self.tam = 0
    
  def insert(self,data, prio):
    if self.head == None:
      self.head = Node(data,prio)
      self.tam+=1
      return
    temp = Node(data,prio)
    last = self.head
    if prio > self.head.prio:
      temp.sig = self.head
      self.head = temp
      self.tam+=1
      return
    while last.sig:
      if last.sig.prio < prio:
        break
      last = last.sig
    temp.sig = last.sig
    last.sig = temp
    self.tam+=1

  def pop(self):
    if self.tam == 1:
        temp = self.head.data
        self.head = None
        self.tam-=1
        return temp
    temp = self.head.data
    self.head = self.head.sig
    self.tam-=1
    return temp
  def isEmpty(self):
    if self.head ==None:
      return True
    return False