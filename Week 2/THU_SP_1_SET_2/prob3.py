def navigate_research_station(station_layout, observations):

    d={}
    for i,ch in enumerate(station_layout):
        d[ch]=i
    # print(d)
    # print(d['a'].key())

    tt,curr=0,0    
    
    for ch in observations:
        ni=d[ch]
        tt+=abs(curr-ni)
        curr=ni
    return tt

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))