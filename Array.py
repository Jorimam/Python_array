
class Array:
    def __init__(self, index = 0):
        self.array_length = 0
        self.item = []
         
#Append method

    def append(self, item):
        self.item[self.array_length] = item
        self.array_length += 1
        
        print([self.item[i] for i in range(self.array_length)])
        
#Insert method
     
    def insert(self, position, item_to_insert):
        self.item_to_insert = item_to_insert
        self.position = position

        self.item[self.position] = self.item_to_insert
        
#Pop method

    def pop(self, item_to_pop = None):
       self.item_to_pop = item_to_pop
       if item_to_pop is None:
           
            
           for i in self.item:
               pass
            
           del self.item[i]
           self.array_length -= 1
           print([self.item[i] for i in range(self.array_length)])
        

       elif self.item_to_pop > self.array_length:
           print("Wrong Indexing")
       else:
           self.item_to_pop = item_to_pop 
           del self.item[item_to_pop]

#Remove method
        
    def remove(self, item_to_remove):
        self.item_to_remove = item_to_remove
        if item_to_remove in self.item:
            del item_to_remove

            print([self.item[i] for i in range(self.array_length)])
            
          
    







