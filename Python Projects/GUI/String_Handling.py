#String Handling
a = "hi"
for i in a:
    print(i)
def has_no_e(word):
    word = str(word)
    for i in word:
        if i == "e":
            return False
    return True
        
        
def avoids(word, forbidden):
    word = str(word)
        
        
    for i in word:
        if i in forbidden:
            return False
    return True

def uses_only(word,letters):
    
    z = 0
   
    for i in letters:
        if i in word:
            z = z + 1
    if len(letters) == len(word) and z== len(word)  :
        return True
    else:
        return False

def uses_all(word,letters):
 
    z = 0
    
    for i in letters:
        if i in word:
            z = z + 1
    if len(letters) >= len(word) and z >= len(word)  :
        return True
    else:
        return False
def has_no_e_mod(word):
    z = 0
    word = str(word)
    u = 0
    o = []
    a = word.split()
    print(a)
    for i in a:
        u = 0
        for q in i:
                    
            if has_no_e(q) == False:
                pass
                u = u + 1
        if u == 0:
            o.append(i)
            z = z + 1
    print(" percentage is ", (int(z)/int(len(a))) * 100)
    return o
def avoids_mod(word, forbidden):
    word = str(word)
    a = word.split() 
    o = []
    print(a)    
    for i in a:
        u = 0
        for q in i:
            if avoids(q,forbidden)==False:
                u = u + 1
                
        if u == 0:
            o.append(i)
    return o
def has_no_e_percent(word):
    z = 0
    word = str(word)
    u = 0
    o = []
    a = word.split()
    print(a)
    for i in a:
        u = 0
        for q in i:
                    
            if has_no_e(q) == False:
                pass
                u = u + 1
        if u == 0:
            o.append(i)
            z = z + 1
    a = (int(z)/int(len(a))) * 100
    return a

            
            

    
    
    
    
    
    
    

    
           

    
