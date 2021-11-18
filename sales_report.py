"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # Creates an empty array for salespeople
melons_sold = [] # Creates an empty array for melons sold

f = open('sales-report.txt') # Opens our sales report file
for line in f: # Iterates through each line in the file
    line = line.rstrip() # Strips the white text from the end of the line
    entries = line.split('|') # Splits each line on the | character

    salesperson = entries[0] # Selects the name of the salesperson and saves as a variable
    melons = int(entries[2]) # Selects the number of melons sold and converts it to an integer

    if salesperson in salespeople: # Check if the salesperson is already in the salespeople array
        position = salespeople.index(salesperson) # If they are in the salesperson array, identify and save the position

        melons_sold[position] += melons # Add the melons from the line to the equivalent position in the melons_sold array
    else:
        salespeople.append(salesperson) # If they are not in the salesperson array, it will append it to the array
        melons_sold.append(melons)  # We will also append the number of melons sold to the melons_sold array


for i in range(len(salespeople)): # Iterate through the length of the salesperson array
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # Print the results for each matching pair in the two arrays


"Improvements"
# We should rename variables to improve readability
# We should utilize functions to improve efficiency
# Instead of having two unrelated arrays, we should use a dict so we can store the information as much more useful key value pairs