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
        self.variant = pd.Series(['A', 'T', 'C', 'G', 'a', 't', 'c', 'g'])
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
        variant = pd.Series(['A', 'T', 'C', 'G', 'a', 't', 'c', 'g'])
        for row in range(len(self.df.index)) :
            print(row)
            # Initialize values
            size = self.df.iloc[row, 3]
            read = self.df.iloc[row, 4]
            quality = self.df.iloc[row, 5]
            countVar = pd.Series(0, index = variant)
            countRef = 0
            needNA = True
            # read one character a time
            for index in range(size):
                # get quality value
                valQuality = quality[index]
                # get read character
                valRead = read[index]
                # if the read quality is greater than 30
                if getQInt(valQuality) > 30:
                    # and the read is a reference
                    if isRef(valRead):
                        countRef += 1
                    # and the read is a variant
                    elif isVar(valRead):
                        countVar[valRead] += 1
            # check if any variant occurs more than 3 times
            for var in variant:
                if countVar[var] >= 3:
                    self.out = self.out.append(pd.DataFrame({
                        "Chromosome Name" : [self.df.iloc[row, 0]],
                        "Position" : [int(self.df.iloc[row, 1])],
                        "Reference" : [self.df.iloc[row, 2]],
                        "WinterDawn Base" : [var],
                        "Frequency" : [(countVar[var])/(sum(countVar) + countRef)]}))
                    needNA = False
            # if no SNP found in the position
            if needNA:
                self.out = self.out.append(pd.DataFrame({
                    "Chromosome Name" : [self.df.iloc[row, 0]],
                    "Position" : [int(self.df.iloc[row, 1])],
                    "Reference" : [self.df.iloc[row, 2]],
                    "WinterDawn Base" : ['NA'],
                    "Frequency" : [0]}))

    def outFile(self, name):
        print(f"Generating result table to {name} ...")
        self.out.to_csv(name, "\t", index=False,
            header=True,
            columns=["Chromosome Name", "Position", "Reference", "WinterDawn Base", "Frequency"])

    def outPlot(self, name):
        print(f"Generating plot to {name} ...")
        plt.figure(figsize=(10,6), dpi=300)
        plt.xlabel('Position')
        plt.ylabel('SNP Frequencies')
        plt.title('SNP Call of Winter Dawn')
        plt.xticks(np.arange(1, 60881, 1000), np.arange(1, 60881 , 1000), fontsize = 6, rotation = 45)
        plt.plot(self.out['Position'], self.out['Frequency'], '-o')
        plt.savefig(name)

def isRef(char):
    return True if pd.Series(char).str.contains("[.,]")[0] else False

def isVar(char):
    return True if pd.Series(char).str.contains("[atcgATCG]")[0] else False

def getQInt(char):
    quality = ord(char) - 33
    return quality

main(sys.argv)
