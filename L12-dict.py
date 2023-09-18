d = {
    'today':{'E95':20.4,'diesel':21.84,'E85':14.99},
    'yesterday':{'E95':20.4,'diesel':22,'E85':15},
    'two days ago':{'E95':20.2,'diesel':21.7,'E85':14.98}
    }


sum = {'E95':0,'diesel':0,'E85':0}
for price in d.values():
    sum['E95'] += price['E95']
    sum['diesel'] += price['diesel']
    sum['E85'] += price['E85']

for type, price in sum.items():
    print(f'Average price is of {type}: {sum[type]/len(d.values())}')