s = 'hi All My Name Is Venkat Kiran I Am Stydeing In Amrita Collage'
sr = s.lower()
p = {}
se = set(sr)
li = list(se)
for i in li:
    p[i] = sr.count(i)
x = sorted(p.items(), key=lambda i: i[1], reverse=True)
print(x)
