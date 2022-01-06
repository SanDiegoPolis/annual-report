with open('temp1.txt', 'r', encoding='utf-8') as f:
    list_sender = [word.strip('\n') for word in f.readlines()]
    print(list_sender)