def name_ext(file):
    with open(file) as f:
        Customer_name = []
        for line in f:        
            info = line.split("\t")
            name = info[0]
            Customer_name.append(name)
        return Customer_name[1:]
print(name_ext("customers.txt"))
        
        