import random as rnd
fyld = ["pepproni","salat","tun","ost","skinke","tomat","mayo"]
def sandwich(fyld,amount):
    print("sandwichen indeholder")
    for i in range(0,amount ):
        print(rnd.choice(fyld))
    print()

sandwich(fyld,5)
sandwich(fyld,2)
sandwich(fyld,10)