import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# input = "/Users/jameschen/Dropbox/GradSchool/*Spring_18/hort503/Project/Project2/input.txt"
# output = "/Users/jameschen/Dropbox/GradSchool/*Spring_18/hort503/Project/Project2/output.txt"
# outplot = "/Users/jameschen/Dropbox/GradSchool/*Spring_18/hort503/Project/Project2/plot.png"
def main(argv):
    script, input, output, outplot = argv

    snp = SNPCall(input)
    snp.filterInDel()
    snp.filterSkip()
    snp.filterShortRead()
    snp.doCall()
    snp.outFile(output)
    snp.outPlot(outplot)
    print("Done")

class SNPCall(object):

    def __init__(self, input):
        self.df = pd.read_table(input, header = None)
        self.out = pd.DataFrame({
            "Chromosome Name" : [],
            "Position" : [],
            "Reference" : [],
            "WinterDawn Base" : [],
            "Frequency" : []})

    def filterInDel(self):
        print(f"Filtering reads contain insertion and deletion ...")
        isIndel = ~(self.df.iloc[:, 4].str.contains("[*+-]"))
        self.df = self.df[isIndel]

    def filterSkip(self):
        print(f"Filtering reads contain skip ...")
        isSkip = ~(self.df.iloc[:, 4].str.contains("[><]"))
        self.df = self.df[isSkip]

    def filterShortRead(self):
        print(f"Filtering reads with short depth ...")
        isShort = ~(self.df.iloc[:, 3] < 10)
        self.df = self.df[isShort]

    def printData(self):
        return self.df

    def doCall(self):
        print(f"Calling snp ...")
        variant = pd.Series(['A', 'T', 'C', 'G'])
        for row in range(len(self.df.index)):
            # Initialize values
            size = self.df.iloc[row, 3]
            read = self.df.iloc[row, 4]
            quality = self.df.iloc[row, 5]
            countVar = pd.Series(0, index = variant)
            countRef = 0
            indexQ = 0
            indexR = 0
            # read one character a time
            while indexQ != size:
                # get quality value
                valQuality = quality[indexQ]
                # get read character
                valRead = read[indexR]
                if valRead in "$":
                    indexR += 1
                    valRead = read[indexR]
                # if the read quality is greater than or equal 30
                if getQInt(valQuality) >= 30:
                    # and the read is a reference
                    if isRef(valRead):
                        countRef += 1
                    # and the read is a variant
                    if isVar(valRead):
                        countVar[valRead.upper()] += 1
                indexQ += 1
                indexR += 1
            # check if any variant occurs more than 3 times
            for var in variant:
                if countVar[var] >= 3:
                    self.out = self.out.append(pd.DataFrame({
                            "Chromosome Name": [self.df.iloc[row, 0]],
                            "Position": [self.df.iloc[row, 1].astype(int)],
                            "Reference": [self.df.iloc[row, 2]],
                            "WinterDawn Base": [var],
                            "Frequency": [countVar[var]/size]
                        })
                    )
            # if no SNP found in the position
            # if needNA:
            #     self.out = self.out.append(pd.DataFrame({
            #         "Chromosome Name" : [self.df.iloc[row, 0]],
            #         "Position" : [int(self.df.iloc[row, 1])],
            #         "Reference" : [self.df.iloc[row, 2]],
            #         "WinterDawn Base" : ['NA'],
            #         "Frequency" : [0]}))

    def outFile(self, name):
        print(f"Generating result table to {name} ...")
        self.out['Position'] = self.out['Position'].astype(int)
        self.out.to_csv(name, "\t", index=False,
            header=False,
            columns=["Chromosome Name", "Position", "Reference", "WinterDawn Base", "Frequency"])

    def outPlot(self, name):
        print(f"Generating plot to {name} ...")
        plt.figure(figsize=(15, 5), dpi=300)
        plt.xlabel('Position')
        plt.ylabel('SNP Frequencies')
        plt.title('SNP Call of Winter Dawn')
        # create plot
        width = 30
        alpha = .4
        indexA = self.out['WinterDawn Base'].str.contains("[A]")
        indexT = self.out['WinterDawn Base'].str.contains("[T]")
        indexC = self.out['WinterDawn Base'].str.contains("[C]")
        indexG = self.out['WinterDawn Base'].str.contains("[G]")
        plt.bar(self.out['Position'][indexA], self.out['Frequency'][indexA],
                width=width, alpha=alpha, color='b', label='SNP:A', snap=False)
        plt.bar(self.out['Position'][indexT], self.out['Frequency'][indexT],
                width=width, alpha=alpha, color='g', label='SNP:T', snap=False)
        plt.bar(self.out['Position'][indexC], self.out['Frequency'][indexC],
                width=width, alpha=alpha, color='k', label='SNP:C', snap=False)
        plt.bar(self.out['Position'][indexG], self.out['Frequency'][indexG],
                width=width, alpha=alpha, color='r', label='SNP:G', snap=False)
        plt.legend()
        plt.tight_layout()
        plt.savefig(name)
        # plt.show()

def isRef(char):
    return True if pd.Series(char).str.contains("[.,]")[0] else False

def isVar(char):
    return True if pd.Series(char).str.contains("[atcgATCG]")[0] else False

def getQInt(char):
    quality = ord(char) - 33
    return quality

main(sys.argv)
