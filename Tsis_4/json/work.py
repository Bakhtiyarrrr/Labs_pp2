import json
from d import x
print("Interface Status")
print("="* 98)
print("Dn", " "* 55, "Discription", " "*10, "Speed", " "*5, "Mtu")
y = json.loads(x)
dn = []
speed = []
mtu = []
for a,b in y.items():
    if a == "imdata":
     for n in b:
        d = n["l1PhysIf"]["attributes"]
        for k,l in d.items():
           if k == "dn":
              dn.append(l)
           if k == "speed":
              speed.append(l)
           if k == "mtu":
              mtu.append(l)
for j in range(len(dn)):
   if len(dn[j]) == 41:
      dn[j] = dn[j] + " "

print()
print("-"*58, "-"*22, "-"*6, " "*4, "-"*4 )

for i in range(len(speed)):
   print(dn[i]," "*38, speed[i], " "*3, mtu[i])
              
