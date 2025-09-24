def total_sales(ticket_sales):
    s=0
    for i in ticket_sales.values():
        s+=i
    return s

    # s=0
    # for i,v in enumerate(ticket_sales):
    #     print(i,v)
    #     s+=v
    # return s

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))