# Objective:
# Build a threaded program that counts the number of words in multiple large text files concurrently.
# Details:
# - You are given a list of file paths (say 5–10 large .txt files).
# - Write a function count_words(file_path) that opens a file, reads its contents, and returns the word count.
# - Use threading to launch one thread per file so that multiple files are processed at the same time.
# - Collect the results in a shared dictionary like:
# {
#     "file1.txt": 12345,
#     "file2.txt": 6789,
#     ...
# }
# -
# - Use a threading.Lock to ensure safe updates to the shared dictionary.
# - Print the total word count across all files at the end
 


import threading, time

def count_words(file_path, delay):
    print('Starting for: ', file_path)
    time.sleep(delay)
    c = 0
    with open(file_path, 'r') as f:
        for i in f:
            for j in i:
                c += 1
        print(f'Total words in {file_path}: {c}')

    print('Ended for:', file_path)
    

file1_path = 'file1.txt'
file2_path = 'file2.txt'
delay = 3

t1 = threading.Thread(target = count_words, args = (file1_path, delay))
t2 = threading.Thread(target = count_words, args = (file2_path, delay))

t1.start(); t2.start()
t1.join(); t2.join()

print('Both counting done')