def count_occurences(file_name:str, word:str) -> int:
    counter = 0
    try:
        word = word.lower()
        stream = open(file_name)
        lines = stream.readlines(3)
        while len(lines) != 0 :
            for line in lines:
                line = line.lower().replace(',', '').replace('.', '').replace('\n', '')
                for file_word in line.split():
                    if file_word == word:
                        counter+=1
            lines = stream.readlines(3)
        stream.close()
    except Exception as e:
        print(f'An error occurred: {e}')
    return counter

print(count_occurences('sample_text.txt', 'the'))


# Solution by PCAP
def count_occurences(file_name, word):
    count = 0
    try:
        stream = open(file_name, 'r')
        for line in stream:
            words = line.replace('.', ' ').replace(',', ' ').split()
            for i in words:
                if(i.lower() == word.lower()):
                    count = count + 1
    except Exception:
        print('something went wrong')
    finally:
        stream.close()
    return count