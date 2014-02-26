fr = open('nominees.lines')
nominee_data  = fr.read()
fr.close()

nominee_blocks = nominee_data.split('\n\n')
for block in nominee_blocks :
    nominee_lines = block.splitlines()
    fr = open('./categories/' + nominee_lines[0])
    category_data = fr.read()
    fr.close()
    category_lines = category_data.splitlines()
    count = [0, 0]
    for i in range(2, len(nominee_lines)) :
        count.append(0)
        for category_line in category_lines :
            if nominee_lines[i].lower() in category_line :
                count[i] = count[i] + 1
    ret_line = nominee_lines[count.index(max(count))]
    ret_line = ret_line + ' has won an award for ' + nominee_lines[1] + '!'
    print count
    print ret_line
