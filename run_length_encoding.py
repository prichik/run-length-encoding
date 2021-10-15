s = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
def encode(s):
  s1 = ""
  countl = 0
  qr_count = 0
  s  =  s + ";"
  for i in range(len(s)-1):
    countl += 1
    if s[i] != s[i+1]:
      qr_count = countl

      s1 += str(qr_count) + s[i]

      countl = 0
  return s1

s_chp1 = encode(s)
print(s_chp1)

def decode(s_chp):
  s2 = ""
  mn = []
  m = []
  mb = []
  n = 0
  sm = ""
  for i in range(len(s_chp)):
    if ord("A") <= ord(s_chp[i]) <= ord("Z"):
      mb.append(s_chp[i])
  for i in range(len(s_chp)):
    if s_chp[i] in "1234567890":
      s2 += s_chp[i]
    else:
      n = int(s2)
      mn.append(n)
      s2 = ""
  for i in range(len(mn)):
    m.append(mn[i])
    m.append(mb[i])
  for i in range(len(m)-1):
    if i % 2 == 0:
      sm += m[i] * m[i+1]
  return sm

print(decode(s_chp1))
