#print("stats module loaded")

def word_count(file_contents):
    num_words = len(file_contents.split()) 
    return num_words 

def char_count(file_contents):
    char_counts = {}
    for char in file_contents.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(char_dict):
    return char_dict["num"]

def format_report(char_counts):
    sorted_list = []
    
    for char, count in char_counts.items():#char is the key, count is the value
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)    
    return sorted_list



    