def sum_honey(hunny_jars):
    total_honey=0
    if len(hunny_jars) == 0:
        return 0
    else :
        for honey in hunny_jars:
            total_honey += honey
        return total_honey

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
