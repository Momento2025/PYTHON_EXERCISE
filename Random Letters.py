import random
def RL(Ft,St):
    return Ft,St
Ft = chr(random.randint(ord('a'),ord('z')))
St = chr(random.randint(ord('a'),ord('z')))

while Ft == St:
    St = chr(random.randint(ord('a'),ord('z')))

print(RL(Ft,St))
