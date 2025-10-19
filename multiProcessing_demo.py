import multiprocessing, time

def count_words(file_path, delay):
    print('Starting for: ', file_path)
    # time.sleep(delay)
    c = 0
    with open(file_path, 'r') as f:
        for i in f:
            for j in i:
                c += 1
        print(f'Total words in {file_path}: {c}')

    print('Ended for:', file_path)
    
if __name__ == "__main__":
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    delay = 3

    t1 = multiprocessing.Process(target = count_words, args = (file1_path, delay))
    t2 = multiprocessing.Process(target = count_words, args = (file2_path, delay))

    t1.start(); t2.start()
    t1.join(); t2.join()

    print('Both counting done')