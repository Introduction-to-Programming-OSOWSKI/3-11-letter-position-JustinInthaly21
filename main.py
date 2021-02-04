def letterPos(w, x):
    

    
    for i in range(0, len(w)):
        if w[i] == x:
            return i + 1
        else:
            return None
      

print(letterPos("hello", "h"))

