s = "вопрос"
ss = "бМХЛЮМХЭ"
sss = "оХРЮМХЕ"
print(s.encode("CP1251").decode("KOI8-R"))
print(ss.encode("KOI8-R").decode("CP1251"))
print(sss.encode("KOI8-R").decode("CP1251"))
