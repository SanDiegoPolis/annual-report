# 目前只统计文字，不统计图片和其他特殊消息
import os

def extract_log(log_file):
    GROUP_ID = '88888888'
    YEAR_BEGIN = '2021-01-01'
    YEAR_END = '2022-01-01'

    with open(log_file, 'r', encoding='utf-8') as f:
        msg_list = [msg.strip('\n') for msg in f.readlines()]

    list_time = []
    list_sender = []
    list_msg = []
    list_log = []
    last_msg = ''

    for msg in msg_list:

        if (msg.startswith('[') == False): # 换行情况
            msg = last_msg + '\n' +  msg
            if bool(list_time): list_time.pop()
            if bool(list_sender): list_sender.pop()
            if bool(list_msg): list_msg.pop()

        last_msg = msg
        short_msg = msg
        left_pos = msg.find('[')
        right_pos = msg.find(']')
        index = 0

        if (msg.find('] - recv from: [') == -1 or msg.find(')]') == -1): # 筛掉send to等非消息消息格式
            continue
        while (left_pos != -1 and right_pos != -1):
            sliced_msg = short_msg[left_pos + 1 : right_pos]

            if (index == 0):
                if (sliced_msg < YEAR_BEGIN or sliced_msg > YEAR_END): # 划定时间范围，2022-01-01会小于所有2022-01-01以后的消息
                    break
                list_time.append(sliced_msg)
            if (index == 1): 
                if sliced_msg != 'INFO': # 筛掉ERROR等
                    list_time.pop()
                    break 
            if (index == 3): # 筛掉非大群消息
                if sliced_msg.find('(' + GROUP_ID + '),') == -1:
                    list_time.pop()
                    break
                
                qid = sliced_msg[sliced_msg.rfind('(') + 1 : sliced_msg.rfind(')')]
                list_sender.append(qid)

                right_pos = short_msg.find(')]')
                short_msg = short_msg[right_pos + 2 :]
            else:
                short_msg = short_msg[0 : left_pos] + short_msg[right_pos + 1 :] # 迭代主语句

            if (index == 2):
                left_pos = short_msg.find('[')
                right_pos = short_msg.find(')]') + 1
            else:
                left_pos = short_msg.find('[')
                right_pos = short_msg.find(']')
            index += 1
        else:
            list_msg.append(short_msg[left_pos + 1 :])
            if len(list_time) != len(list_sender) or len(list_time) != len(list_msg):
                print('time:' + str(len(list_time)) + '|sender:' + str(len(list_sender)) + '|msg:' + str(len(list_msg)) + 
                      '|time:' + list_time[-1] + '|sender:' + list_sender[-1] + '|msg:' + list_msg[-1])
                input()


    if len(list_time) == len(list_sender) and len(list_time) == len(list_msg):
        for i in range(len(list_msg)):
            list_log.append([list_time[i], list_sender[i], list_msg[i]])
    else:
        print('Warning！列表长度不等！' + 'time:' + str(len(list_time)) + '|sender:' + str(len(list_sender)) + '|msg:' + str(len(list_msg)))

    # for obj in list_time:
    #     print(obj)
    # for obj in list_sender:
    #     print(obj)
    # for obj in list_msg:
    #     print(obj)
    # for obj in list_log:
    #     print(obj)

    with open('./list/list_time.txt', 'a', encoding='utf-8') as f:
        for obj in list_time:
            f.write(str(obj) + '\n')
    with open('./list/list_sender.txt', 'a', encoding='utf-8') as f:
        for obj in list_sender:
            f.write(str(obj) + '\n')
    with open('./list/list_msg.txt', 'a', encoding='utf-8') as f:
        for obj in list_msg:
            f.write(str(obj) + '\n')
    with open('./list/list_log.txt', 'a', encoding='utf-8') as f:
        for obj in list_log:
            f.write(str(obj) + '\n')

    #print('time:' + str(len(list_time)) + '|sender:' + str(len(list_sender)) + '|msg:' + str(len(list_msg)))

if __name__ == '__main__':  
    files_list = os.listdir('./list/')
    for file in files_list:
        print('deleting ' + file)
        os.remove('./list/' + file)

    files_log = os.listdir('./logs/')
    for file in files_log:
        print('extracting ' + file)
        extract_log('./logs/' + file)