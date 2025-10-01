def max_audience_performances(audiences):
    dict_audiences = {}
    for i,v in enumerate(audiences):
        if v not in dict_audiences:
            dict_audiences[v]=1
        else:
            dict_audiences[v]+=1
    max_aud = max(dict_audiences.keys())
    return max_aud * dict_audiences[max_aud]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))