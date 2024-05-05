from utils import number_of_words_length_n

file_path = 'dataset.csv'
c_sum = 0
max_len = 10
for length in range(max_len + 1):
    count = number_of_words_length_n(file_path, length)
    print(f"Number of rows with length {length}: {count}")
    c_sum = c_sum + count
print(f"Number of rows with length smaller or equal to {max_len}: {c_sum}")