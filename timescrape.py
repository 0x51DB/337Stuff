fr = open('goldenglobes.json','r')
fw = open('time.lines','w')
read_data = fr.read()
i = 0
while (i < len(read_data)) :
    testval = read_data.find("\"$date\" : ", i)
    if testval != -1 :
        i = testval + 10
        checkboundval = 1
        boundval = i
        while(checkboundval == 1) :
            boundval = read_data.find(" ", boundval + 1)
            if (read_data[boundval - 1] != '\\') :
                checkboundval = 0
        fw.write(read_data[i:boundval])
        fw.write("\n")
        i = boundval
    i = i + 1
fr.close()
fw.close()
