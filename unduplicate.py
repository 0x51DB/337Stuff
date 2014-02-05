fr = open("scraped.lines", "r")
read_data = fr.read()
fr.close()
seen = set()
for line in read_data.splitlines() :
    if line not in seen :
        seen.add(line)
fw = open("scraped.lines", "w")
for line in seen :
    fw.write(line + "\n")
fw.close()
