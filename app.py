from words import words_list
import csv 
import pandas as pd

# Prepare the data
data = [(len(word), word) for word in words_list]

# Define the CSV file name
file_name = 'dataset.csv'

# Write to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Length', 'Word', 'Pattern', 'Syllable_count'])
    # Write the data
    for row in data:
        writer.writerow(row)

df = pd.read_csv('dataset.csv')

# Sort the DataFrame by the length column in ascending order
df.sort_values(by=['Length', 'Word'], ascending=[True, True], inplace=True)

# Write the sorted DataFrame back to the CSV file
df.to_csv('dataset.csv', index=False)