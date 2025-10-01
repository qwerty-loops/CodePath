def max_audience_performances(audiences):
    max_aud = max(audiences)
    c=0
    for i in audiences:
        if i==max_aud:
            c+=1
    return max_aud*c

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))