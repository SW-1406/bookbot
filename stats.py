def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    count = {}
    for character in text.lower():
        if character in count.keys():
            count[character] += 1
        else:
            count[character] = 1
    return count

def get_sorted_character_list(count):
    count_list = []
    for key,value in count.items():
        count_list.append({"char":key,"num":value})
    count_list.sort(reverse=True,key=sort_by_num)
    return count_list

def sort_by_num(dict):
    return dict["num"]