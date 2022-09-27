a="a";b="b";c="c";d="d";e="e";f="f";g="g";h="h";i="i"

#p1's turn 
print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
while True:
    #P1's TURN----------------------
    t_1=input("\nP1's turn -  ")
    if t_1=="a":
        a="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="b":
        b="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="c":
        c="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="d":
        d="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="e":
        e="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="f":
        f="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="g":
        g="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="h":
        h="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_1=="i":
        i="X"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    
#P1 Winning condition

    if a=="X" and b=="X" and c=="X":
        print("P1 won!")
        break
    if a=="X" and e=="X" and i=="X":
        print("P1 won!")
        break
    if a=="X" and d=="X" and g=="X":
        print("P1 won!")
        break
    if c=="X" and f=="X" and i=="X":
        print("P1 won!")
        break
    if g=="X" and h=="X" and i=="X":
        print("P1 won!")
        break
    if d=="X" and e=="X" and f=="X":
        print("P1 won!")
        break
    if c=="X" and e=="X" and g=="X":
        print("P1 won!")
        break
    if b=="X" and e=="X" and h=="X":
        print("P1 won!")
        break

#P2's turn-----------------------

    t_2=input("\nP2's turn - ")
    if t_2=="a":
        a="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="b":
        b="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="c":
        c="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="d":
        d="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="e":
        e="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="f":
        f="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="g":
        g="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="h":
        h="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    if t_2=="i":
        i="O"
        print("\n",a, b, c,"\n",d, e, f,"\n",g, h, i)
    
#P2's WINNING TERMS------------------------    

    if a=="O" and b=="O" and c=="O":
        print("P2 won!")
        break
    if a=="O" and e=="O" and i=="O":
        print("P2 won!")
        break
    if a=="O" and d=="O" and g=="O":
        print("P2 won!")
        break
    if c=="O" and f=="O" and i=="O":
        print("P2 won!")
        break
    if g=="O" and h=="O" and i=="O":
        print("P2 won!")
        break
        break
    if d=="O" and e=="O" and f=="O":
        print("P2 won!")
        break
    if c=="O" and e=="O" and g=="O":
        print("P2 won!")
        break
    if b=="O" and e=="O" and h=="O":
        print("P2 won!")
        break