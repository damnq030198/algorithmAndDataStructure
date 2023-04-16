# Fast python code that first calls pow()  
# then applies % operator 
a = 2
b = 100
p = (int)(1e9+7) 
  
# Using direct fast method to compute  
# (a ^ b) % p. 
d = pow(a, b, p) 
print(d)

#Recursive
def mod_exp2(base, exp, mod):
    if exp == 0: 
        return 1
    if exp and 1 == 0:
        r = mod_exp2(base, exp / 2, mod)
        return (r * r) % mod
    else: 
        return (base % mod * mod_exp2(base, exp - 1, mod)) % mod


x = mod_exp2(a, b, p)
print(x)