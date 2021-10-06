import re
# input file
f = open("mailaddress.txt", "rt")
# output file
fw = open("name.txt", "w")
toFindAddr = "hotmail.com"
cnt = 0
for mailAddr in f:
    st = mailAddr.casefold().split("@")
    if st[1].find(toFindAddr) < 0:
        continue
    removedSt = ''.join([i for i in st[0] if not i.isdigit()])
    splitList = re.split('_|\.', removedSt)
    if len(splitList) > 1:
        fw.write('First name = ' + splitList[0] + ', Last name = ' + splitList[1] + '\n')
        #print('First name = ' + splitList[0] + ', Last name = ' + splitList[1] + '\n')
    else:
        fw.write('First name = ' + splitList[0] + '\n')
        #print('First name = ' + splitList[0] + '\n')
    cnt = cnt + 1
# print count of names
fw.write('Count : ' + str(cnt))
f.close()
fw.close()
