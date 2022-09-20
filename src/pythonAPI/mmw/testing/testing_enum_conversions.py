from enum import Enum


class typ(Enum):
    none    = 0
    I16     = 1

print(typ.none, (typ.none.name), type(typ.none.name))

#Conversion backward:
string = "none"
print(typ.__members__, typ[string])

