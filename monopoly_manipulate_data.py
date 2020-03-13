def read_data():
    file = open('data.txt','r')
    raw = file.readlines()
    file.close()
    for a in range(len(raw)):
        raw[a] = raw[a].strip().split(';')
    return raw

def get_percentages(raw):
    new = []
    total = 0
    for a in range(len(raw)):
        total += int(raw[a][1])
    for b in range(len(raw)):
        new.append([str(raw[b][0]),((int(raw[b][1])/total)*100)])
    return new

def order(new,raw):
    newer = new
    newer.sort(key=lambda newer:newer[1])
    print(newer)
    rawer = raw
    for a in range(len(rawer)):
        rawer[a][1] = int(rawer[a][1])
    rawer.sort(key=lambda rawer:rawer[1])
    print(rawer)

def write_percentages(new):
    file = open('percentages.txt','w+')
    for c in range(len(new)):
        file.write(str(new[c][0]) + ';' + str(new[c][1]) + '\n')
    file.close()


raw = read_data()
new = get_percentages(raw)
write_percentages(new)
order(new,raw)
