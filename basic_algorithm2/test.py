class Queue(list):
    put=list.append
    def peek(self):
        return self(0)    
    def get(self):
        return self.pop(0)
q=Queue()
q.append(1)
print(q)