# convert when possible a number from any base into base 10

x = raw_input()
for i in range(2, 17):
  try: print "{}{}".format(i, int(x, i))
  except:pass
