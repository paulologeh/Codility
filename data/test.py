import numpy as np
import pandas as pd
import csv


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    result = []
    for file in files:
        # print(file)
        rows = []
        # read in rows
        with open(file, 'r') as csvfile:
            data = csv.reader(csvfile, skipinitialspace=True)
            for row in data:
                rows.append(row)

        highestVolume = {}
        highestClose = {}
        for i in range(1, len(rows)):
            key = rows[i][0]
            year = key[:4]
            new = True
            for keys in highestVolume:
                if year in keys:
                    new = False
                    if highestVolume[keys] < int(rows[i][5]):
                        del highestVolume[keys]
                        highestVolume[rows[i][0]] = int(rows[i][5])
                    break
            if new:
                highestVolume[rows[i][0]] = int(rows[i][5])
            new = True
            for keys in highestClose:
                if year in keys:
                    new = False
                    if highestClose[keys] < rows[i][4]:
                        del highestClose[keys]
                        highestClose[rows[i][0]] = rows[i][4]
                        break
            if new:
                highestClose[rows[i][0]] = rows[i][4]

        data1 = {'date': [], 'vol': []}
        for key in highestVolume:
            data1['date'].append(key)
            data1['vol'].append(highestVolume[key])

        data2 = {'date': [], 'close': []}
        for key in highestClose:
            data2['date'].append(key)
            data2['close'].append(highestClose[key])

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        result.append([df1, df2])
    print(result)
    return result


solution(['./data/throwsh.csv', './data/framp.csv'])
