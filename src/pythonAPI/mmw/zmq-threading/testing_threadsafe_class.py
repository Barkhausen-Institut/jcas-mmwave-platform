

class instr(object):
    myhost = ""
    mydict = {"host":""}
    def __init__(self,host):
        self.myhost = host
        self.mydict["host"] = host


    def get_myhost(self):
        return self.myhost, self.mydict["host"]

objA = instr("a")

print(objA.get_myhost())

objB = instr("b")

print(objA.get_myhost())
print(objB.get_myhost())