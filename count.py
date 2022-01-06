def count():
    file = './list/list_sender.txt'

    with open(file, 'r', encoding='utf-8') as f:
        list_sender = [word.strip('\n') for word in f.readlines()]

    msg_count = {}
    for msg in list_sender:
        if msg in msg_count.keys():
            msg_count[msg] = msg_count[msg] + 1
        else:
            msg_count[msg] = 1
        
    for k, v in msg_count.items():
        msg_count[k] = str(v)

    sorted_msg_count_list = sorted(msg_count.items(), key = lambda x : int(x[1]), reverse = True)

    with open('./msg_count.txt', 'w', encoding='utf-8') as f:
        for obj in sorted_msg_count_list:
            f.write(obj[0] + ':' + str(obj[1]) + '\n')

    #print('Count complete!')

    return zip(*sorted_msg_count_list)

if __name__ == '__main__': 
    count()