S = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

n = 0


n += S.count('c=')
S = S.replace('c=',' ')

n += S.count('c-')
S = S.replace('c-',' ')

n += S.count('dz=')
S = S.replace('dz=',' ')

n += S.count('d-')
S = S.replace('d-',' ')

n += S.count('lj')
S = S.replace('lj',' ')

n += S.count('nj')
S = S.replace('nj',' ')

n += S.count('s=')
S = S.replace('s=',' ')

n += S.count('z=')
S = S.replace('z=',' ')

for i in range(26):
  n += S.count(alpha[i])


print(n)