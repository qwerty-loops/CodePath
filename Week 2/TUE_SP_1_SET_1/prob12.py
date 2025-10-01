def sort_performers(performer_names, performance_times):
    # sp={}
    # for i, j in zip(performer_names, performance_times):
    #     sp[i]=j
    # print(sp)
    # return sorted(sp.items(),key=lambda i : i[1],reverse=True)

    # Step 1: combine names with times
    combined = list(zip(performer_names, performance_times))
    print(combined)
    
    # Step 2: sort by time descending
    combined.sort(key=lambda x: x[1], reverse=True)
    
    # Step 3: take only the names
    # return [name for name, _ in combined]
    for i in combined:
        print (i)

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))