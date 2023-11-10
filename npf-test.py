import numpy_financial as npf

rate = .05/12  # monthly
nper = 10*12   # months
pmt = 100
pv = 100

fv = npf.fv(rate, nper, -pmt, -pv)

print("Task:")
print("What is the future value after 10 years of saving $100 now, with an additional monthly savings of $100. Assume the interest rate is 5% (annually) compounded monthly?")
print("Solution:")
print(f"future value = {fv:.2f}")
