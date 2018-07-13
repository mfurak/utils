#!/usr/bin/env python3
import datetime

time_format = '%H:%M'

while(True):
    try:
        first_h = input("first hour: ")
        first_m = input("first minute: ")
        second_h = input("second hour: ")
        second_m = input("second minute: ")
        first_time = datetime.datetime.strptime("{}:{}".format(first_h, first_m), time_format)
        second_time = datetime.datetime.strptime("{}:{}".format(second_h, second_m), time_format)
        time_diff = second_time - first_time
        lunch_diff = time_diff - datetime.timedelta(minutes=30)
        print("First time: {} \t Second time: {} \t Diff: {:02d}:{:02d} \t No lunch diff: {:02d}:{:02d}".format(first_time.time().strftime(time_format), second_time.time().strftime(time_format),time_diff.seconds//3600,(time_diff.seconds%3600//60),lunch_diff.seconds//3600,(lunch_diff.seconds%3600//60)))
    except Exception as e:
        print(e)
        exit()
