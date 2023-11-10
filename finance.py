def fv(pv, r, n, m=1, type='compound'):

    if type=='compound':
        fv = round(pv*(1 + r/m)**(m*n), 2)
        return fv
    elif type=='simple':
        fv = round(pv*(1+r*n), 2)
        return fv

def compound_interest(principal, rate, periods, years):
    amount = round(principal*(1 + rate/periods)**(periods*years), 2)
    return amount

print(compound_interest(12000, 0.05, 1, 3))

