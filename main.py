def letterPos(w, x):
    
    a = None
    
    for i in range(0, len(w)):
        if w[i] == x:
            a = i + 1
            break

    if a == None:
        return "No"
    else:
        return a
         
      

print(letterPos("hello", "l"))

