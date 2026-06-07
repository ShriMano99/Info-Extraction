def account_extractor(file):
    with open("customers.txt") as f:
        account_numbers = []  # To store all the phone numbers
        for line in f:
            info = line.split("\t") # data is delimited by "\t"
            account = info[12] # Extract the account number
            account_numbers . append(account)
    return account_numbers[1:]

  # Testing the function
print(account_extractor("customers.txt"))