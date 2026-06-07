
def dob_extractor(file):
    with open(file) as f:
        dob_list=[]
        for line in f:
            info= line.split("\t")
            dob=info[1]
            print(dob)
            dob_list.append(dob)
    return dob_list[1:]

print(dob_extractor("customers.txt"))