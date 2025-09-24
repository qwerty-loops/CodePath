def count_less_than(race_times, threshold):
       win = 0
       if len(race_times) ==0:
           return 0
       
       else:
            for i in race_times:
                if i < threshold:
                    win +=1
            return win


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))