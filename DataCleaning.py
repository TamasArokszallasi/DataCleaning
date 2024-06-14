import csv

# Read the text from a TXT file
with open('Test.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# Initialize the lists to store the extracted data
types = []
countries = []
names = []
emails = []
xidss = []

# Define the keywords to search for
keywords = ["TYPE", "Country:", "NAME:", "E-MAIL:", "XiD:"]

# Initialize the start index
start = 0

# Loop over the data to extract the required information
while start != -1:
    for i in range(len(keywords)-1):
        start = data.find(keywords[i], start)
        if start == -1:
            break
        end = data.find(keywords[i+1], start)
        value = data[start+len(keywords[i]):end].strip()
        
        if keywords[i] == "TYPE":
            types.append(value)
        elif keywords[i] == "Country:":
            countries.append(value)
        elif keywords[i] == "NAME:":
            names.append(value)
        elif keywords[i] == "E-MAIL:":
            emails.append(value)
        elif keywords[i] == "XiD:":
            xids.append(value)
        
        start = end

# Write the extracted data into a CSV file
with open('Test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Type', 'Country', 'Name', 'Email', 'XiD'])
    writer.writerows(zip(types, countries, names, emails, xids))