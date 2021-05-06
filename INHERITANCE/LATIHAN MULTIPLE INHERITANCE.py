#latihan multiple inheritance
class base1(object):
    def __init__(self):
        self.str1 = "geek1"
        print("base1")
  
class base2(object):
    def __init__(self):
        self.str2 = "geek2"        
        print("base2")
  
class derived(base1, base2):
    def __init__(self):
          
        # Calling constructors of base1
        # and base2 classes
        base1.__init__(self)
        base2.__init__(self)
        print("derived")
          
    def printStrs(self):
        print(self.str1, self.str2)
         
ob = derived()
ob.printStrs()