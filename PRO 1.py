my_list=['zoro','luffy','goku','eren','hinata','gojo']
search_word="eren"
replace_word="levi"
for i in range (len(my_list)):
    if my_list[i] ==search_word:
        my_list[i]= replace_word
        print(my_list)
