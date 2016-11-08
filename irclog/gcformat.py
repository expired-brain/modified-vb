notice = '''AUG_#01_MIX_GOOD_SMALL 75.41%
    AUG_#01_MIX_NO_REFUND 99% ---- Sniffed - NoRefund
    AUG_#01_US_MIX_GOOD 81.5%
    AUG_#01_WORLD_NO_INFO 75.56%
    AUG_#01_USA_MIX_NO_REF 99.49% ---- Sniffed - NoRefund
    AUG_#01_WORLD_NO_REF 97.76% ---- Sniffed - NoRefund
    AUG_#01_USA_MIX_GOOD 78.85%
    AUG_#01_US_GOOD_VALID 75.17%
    AUG_#01_US_MIX_NO_INFO 79.63%
    AUG_#01_SMALL_MIX_HIGH 67.54%
    AUG_#01_USA_NO_REF 99.03% ---- Sniffed - NoRefund
    AUG_#01_USA_GOOD_VALID 71.43%
    AUG_#31_USA_NO_REF 99.05% ---- Sniffed - NoRefund
    AUG_#10_TURKEY_GOOD_VALID 44.7%
    AUG_#13_USA_MIX_NO_CVV 76.57%'''

notice = notice.replace(" ", ":")
notice = notice.replace("_#", " ")
notice = notice.replace("_", " ")
notice = [s.strip().split(' ') for s in notice.splitlines()]

bal = []
for p in notice:
    pa = '''<td style="text-align:center"><span style="color:#FFD700"><strong>'''+ p[0] + '''</strong> <span style="color:#FFFFFF">(''' + p[1] + '''valid)</span></span></td>'''
    print pa

arr = []
for d in bal: print '<tr>'+ arr.append([d[0], d[1]]) +'<tr>'



##########################################################################

notice = str.replace(" ", ":")
notice = str.replace("_#", " ")
notice = str.replace("_", " ")
notice = [s.strip().split(': ') for s in notice.splitlines()]


for p in notice: print '''<td style="text-align:center"><span style="color:#FFD700"><strong>'''+ p[0] + '''</strong> <span style="color:#FFFFFF">(''' + p[1] + '''valid)</span></span></td>'''


value bosaia amake dibe... 
<tr> 



>>> [s.strip() for s in data_string.splitlines()]
['Name: John Smith', 'Home: Anytown USA', 'Phone: 555-555-555', 'Other Home: Somewhere Else', 'Notes: Other data', 'Name: Jane Smith', 'Misc: Data with spaces']


>>> [s.strip().split(': ') for s in data_string.splitlines()]
[['Name', 'John Smith'], ['Home', 'Anytown USA'], ['Phone', '555-555-555'], ['Other Home', 'Somewhere Else'], ['Notes', 'Other data'], ['Name', 'Jane Smith'], ['Misc', 'Data with spaces']]4



n = [s.strip().split(' ') for s in st.splitlines()]


>>> listobj = [('love', 'yes', 'no'), ('valentine', 'no', 'yes'), ('day', 'yes','yes')]
>>> var1, var2, var3 = listobj
>>> var1
('love', 'yes', 'no')
>>> var2
('valentine', 'no', 'yes')
>>> var3
('day', 'yes', 'yes')




>>> mylist = [[], ['shotgun', 'weapon'], ['pistol', 'weapon'], ['cheesecake', 'f
ood'], []]
>>> print mylist[2][1]
weapon
