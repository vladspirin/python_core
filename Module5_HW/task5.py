sup_num_list = ['x\u00b9', 'x\u00b2', 'x\u00b3', 'x\u2074'] 
for x in sup_num_list:
    print("%10s" % x, end='')
print()
for i in range(1, 10):    
    for j in range(1, 5):
        print("%10d" % i ** j, end='')
    print()
