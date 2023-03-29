long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

lines = long_text.strip().split('\n')
dict_str = {}
dict_str ['name'] = lines[0]
dict_str ['lei'] = lines[1]

sub_funds = []
i = 2
while i < len(lines):
    sub_fund = {}
    sub_fund['title'] = lines[i][2:]
    sub_fund['isin'] = []
    i += 1
    while i < len(lines) and len(lines[i]) == 12:
        sub_fund['isin'].append(lines[i])
        i += 1
    sub_funds.append(sub_fund)
dict_str['sub_fund'] = sub_funds

print(dict_str)
