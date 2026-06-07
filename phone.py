
def phone_extractor(file):
    with open(file) as f:
        phone_numbers = []  # To store all the phone numbers
        for line in f:
            info = line.split("\t")  # Data is delimited by "\t". So, we use that to separate fields
            phone = info[3]  # Extract the phone number
            phone_numbers.append(phone)  # Add the extracted phone number to the list
    return phone_numbers[1:]

# Testing the function
print(phone_extractor("customers.txt"))