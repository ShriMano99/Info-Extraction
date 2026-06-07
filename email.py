def email_extractor(file):
    with open(file) as f:
        emails = []
        for line in f:
            info = line.split("\t")
            email = info[5]
            emails.append(email)
    return emails[1:] 

print(email_extractor("customers.txt"))
