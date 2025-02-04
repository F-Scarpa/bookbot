def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)


    def word_count(file):
        count_words = file.strip()
        count_words = file.split()
        return len(count_words)
    
    #print(word_count(file_contents))

    def char_count(file):
        
        counter_dict = {}
        for char in file:
            char = char.lower()
            if char not in counter_dict:
                counter_dict[char] = 1
            else:
                counter_dict[char] += 1
               
        return counter_dict
    
    print(char_count(file_contents))



main()
