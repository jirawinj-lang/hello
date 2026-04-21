has_good_credit = True
has_high_income = False

if has_good_credit and not has_high_income:
    print("Eligible for load")


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
