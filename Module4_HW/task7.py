# 1
msg = 'Zahar Berkut'
# 2
print(msg)
# 3
msg += msg
msg *= 3
print(msg)
# 4
hello = 'Hello '
hello = hello + msg + ' '
print(hello)
# 5
msg = msg[0:6] + msg[0:5] + 'ovich ' + msg[6:12]
print(msg) 
# 6
s = 'colorless'
s = s[0:4] + 'u' + s[4:]
print(s)
# 7
a, b, c, d, e = 'dish-es', 'run-ning', 'nation-ality', 'un-do', 'pre-heat'
a = a[0:4] + a[5:]
b = b[0:3] + b[4:]
c = c[0:6] + c[7:]
d = d[0:2] + d[3:]
e = e[0:3] + e[4:]
print(a, b, c, d, e)
