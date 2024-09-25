lines =open("./out", 'r').readlines()
data = ''
for i, line in enumerate(lines):
    if (i % 2) == 0:
        data += line[10:].strip()

data_bytes = bytes.fromhex(data)

with open('test.pdf', 'wb') as out_file:
    out_file.write(data_bytes)

