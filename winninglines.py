fr = open("scraped.lines", "r")
read_data = fr.read()
fr.close()
data_array = read_data.splitlines()
fw = open("win.lines", "w")
for line in data_array :
    if line.find("win") != -1 or line.find("won") != -1 or line.find("best") != -1 :
        fw.write(line + "\n")
fw.close()
