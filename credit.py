def credit_card_extractor(file):
    with open(file) as f:
        credit_card = [] # To store all the credit card information
        for line in f:
            info = line.split("\t") # Data is separated by tabs(\t), so split the line into a list
            credit = info[11] # Extract the credit card information from the line
            if credit == "N/A":
                continue # If the credit card information is not available, skip to the next line
            credit_card.append(credit) # Add the credit card information to the list
    return credit_card[1:] # Return the list of credit card information

# Testing the function
print(credit_card_extractor("customers.txt"))