def encode(s):
  s1 = ""
  countl = 0
  qr_count = 0
  s  =  s + ";"
  for i in range(len(s)-1):
    countl += 1
    if s[i] != s[i+1]:
      qr_count = countl
      if qr_count == 1:
          s1 += s[i]
          countl = 0
      else:
          s1 += str(qr_count) + s[i]
          countl = 0
  return s1
  
def decode(st):
    news = ''
    n = ''
    for i in st:
        if i.isdigit():
            n += i
        else:
            if not n:
                news += i
            else:
                news += i * int(n)
                n = ''
    return news

s = input("Введите: ")
s_chp1 = encode(s)
print(s_chp1)
print(decode(s_chp1))

