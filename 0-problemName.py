s = ""
s = s.replace(".", "").replace(" ", "_")

fp = open(s + '.py', 'x')
fp.close()
