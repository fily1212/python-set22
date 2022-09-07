a = {}
b = {'Filippo' : '3481234567',
        'Chiara': '0111234567',
        'qualcosa': [1,2,3]}
print(b)
print(b['Filippo'])
print(b)
if 'Edoardo' not in b.keys():
    b['Edoardo'] = '3456778997'