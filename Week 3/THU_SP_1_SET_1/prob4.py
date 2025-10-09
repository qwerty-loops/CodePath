

def find_the_log_conc_val(logs):
    low,high=0,len(logs)-1
    s=0
  
    while low<=high:
        if low==high:
            s+=logs[low]
            low+=1
        elif len(str(logs[high]))==2:
            s+=logs[low]*100+logs[high]
            low+=1
            high-=1
        elif len(str(logs[high]))==1:
            s+=logs[low]*10+logs[high]
            low+=1
            high-=1
    return s

print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 