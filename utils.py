import json
import pandas as pd

def calculate_json_length(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Assuming the JSON is a list of strings, calculate its length
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        # For dictionaries, you might want to count keys or items
        # Here we count the number of keys
        return len(data.keys())
    else:
        print("Unsupported data type. Expected a list or dictionary.")
        return None
    
def sort_csv_by_length(file_path):
    df = pd.read_csv(file_path)
    # Sort the DataFrame by the length column in ascending order
    df.sort_values(by=['Length'], ascending=True, inplace=True)
    # Write the sorted DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

def shuffle_and_reduce_csv(file_path, n, N):   # n is the words length and N is the amount of words with length n that we want to keep
    # Step 1: Read the CSV file
    df = pd.read_csv(file_path)
    
    # Step 2: Filter rows based on length
    filtered_df = df[df['length'] == n]
    
    # Step 3: Shuffle the DataFrame
    shuffled_df = filtered_df.sample(frac=1).reset_index(drop=True)
    
    # Step 4: Reduce the DataFrame to keep only the first 4000 rows
    reduced_df = shuffled_df.head(N)
    
    # Step 5: Save the resulting DataFrame to a new CSV file
    output_file_path = "shuffled_reduced_" + file_path.split("/")[-1]
    reduced_df.to_csv(output_file_path, index=False)
    
    print(f"Shuffled and reduced data saved to {output_file_path}")

def number_of_words_length_n(file_path, n):   # n is the length of words that we want to know their amount
    # Step 1: Read the CSV file
    df = pd.read_csv(file_path)
    
    # Step 2: Filter rows based on length
    filtered_df = df[df['Length'] == n]
    
    # Step 3: Count the number of rows
    row_count = len(filtered_df)
    
    # Step 4: Return the count
    return row_count



print(number_of_words_length_n('dataset.csv', 5))
