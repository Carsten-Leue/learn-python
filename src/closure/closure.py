def createClosure(name):
    print(f"Hello {name}")
    counter = 0
    def increment():
        nonlocal counter
        print(f"Hello {name}: {counter}")
        counter = counter+1;
    
    return increment;