import os

path = './hwp_data/koreatest1'
exefile = 'hwp5txt'

res = []
for root, dirs, files in os.walk(path):
    rootpath = os.path.join(os.path.abspath(path), root)
    for file in files:
        filepath = os.path.join(rootpath, file)
        res.append(filepath)

    for result in res:
        filename = result[:-4] + ".txt"
        output = '--output ' + '"' + filename + '"'
        result = '"' + result + '"'
        print(exefile + " " + output + " " + result)
        os.system(exefile + " " + output + " " + result)
