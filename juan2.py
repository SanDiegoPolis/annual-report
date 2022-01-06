from count import count as count_data
import time

def offset_str(hour): # 传入str类型
    int_hour = (int(hour) - 6) % 24
    if int_hour < 10: return str(int_hour).zfill(2)
    else: return str(int_hour)

def deoffset_str(hour): # 传入str类型
    int_hour = (int(hour) + 7) % 24
    if int_hour < 10: return str(int_hour).zfill(2)
    else: return str(int_hour)

def offset(hour): # 传入float类型
    return (hour - 6) % 24

def deoffset(hour): # 传入float类型
    return (hour + 6) % 24

def juan():
    t0  = time.time()
    file_sender = './list/list_sender.txt'
    file_time = './list/list_time.txt'

    with open(file_sender, 'r', encoding='utf-8') as f:
        list_sender = [word.strip('\n') for word in f.readlines()]
    with open(file_time, 'r', encoding='utf-8') as f:
        list_time = [word.strip('\n') for word in f.readlines()]

    list_Y_M_D = []
    list_h_m_s = []
    for time1 in list_time:
        [Y_M_D, h_m_s] = time1.split('T')
        list_Y_M_D.append(Y_M_D)
        list_h_m_s.append(h_m_s)

    list_month = []
    list_date = []
    for Y_M_D in list_Y_M_D:
        [year, month, date] = Y_M_D.split('-')
        list_month.append(month)
        list_date.append(date)

    list_hour = []
    list_minute = []
    for h_m_s in list_h_m_s:
        [hour, minute, second] = h_m_s.split(':')
        list_hour.append(hour)
        list_minute.append(minute)

    sender, count = count_data() # 导入count.py

    month_latest = []
    date_latest = []
    hour_latest = []
    minute_latest = []
    hour_latest_morning = []
    minute_latest_morning = []
    month_earliest = []
    date_earliest = []
    hour_earliest = []
    minute_earliest = []

    latest_ave = []
    
    for j in range(len(sender)):
        sender_id = sender[j]

        month_latest_i = '-1'
        date_latest_i = '-1'
        hour_latest_i = '06'
        minute_latest_i = '00'
        hour_latest_morning_i = '-1'
        minute_latest_morning_i = '-1'
        month_earliest_i = '-1'
        date_earliest_i = '-1'
        hour_earliest_i = '05'
        minute_earliest_i = '59'

        hour_latest_ave_i = 0
        minute_latest_ave_i = 0
        latest_ave_n = 0
        
        for i in range(len(list_sender)):
            if (list_sender[i] == sender_id):
                if (offset_str(list_hour[i]) >= offset_str(hour_latest_i)):
                    hour_latest_i = list_hour[i] # 最晚发言小时
                if (offset_str(list_hour[i]) <= offset_str(hour_earliest_i)):
                    hour_earliest_i = list_hour[i] # 最早发言小时

                if (offset_str(list_hour[i]) >= offset_str('02')):
                #if 1:
                    latest_ave_n += 1
                    hour_latest_ave_i += int(offset_str(list_hour[i]))
                    minute_latest_ave_i += int(list_minute[i])
        hour_latest.append(hour_latest_i)
        hour_earliest.append(hour_earliest_i)

        latest_ave.append(-1 if latest_ave_n <= 10 else round(latest_ave_n / int(count[j]), 4)) # 卷王
    
    sorted_list = zip(sender, count, latest_ave)
    sorted_list = sorted(sorted_list, key = lambda x : x[2], reverse = True)
    for obj in sorted_list:
        print(obj)
    t1  = time.time()
    print(str(round(t1 - t0, 2)) + 's') # 测量运行时间

if __name__ == '__main__': 
    juan()