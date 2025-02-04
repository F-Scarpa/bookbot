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
        letters_list = []

        for char in file:
            char = char.lower()
            if char not in counter_dict:
                counter_dict[char] = 1
            else:
                counter_dict[char] += 1
            
        #counter_dict = dict(list(sorted(counter_dict.items()))[32:])
        counter_dict = list(counter_dict.items())
        #print([list(counter_dict[0])])
        for i in range(len(counter_dict)):
            character = list(counter_dict[i])
            letters_list.append(character)
            letters_list.sort()
        
        
        #print(letters_list[32:])
        for data in letters_list[32:]:
            print(f"The '{data[0]}' character was found {data[1]} times")
    

        return "---End report---"
        
    
    print(char_count(file_contents))



main()
