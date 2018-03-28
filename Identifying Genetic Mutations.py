# Open all the files and set them all to be read
aHemoFile = open("Hemoglobin_A.txt")
aHemo = aHemoFile.read()

bHemoFile = open("Hemoglobin_B.txt")
bHemo = bHemoFile.read()

aHexaFile = open("HEXA_A.txt")
aHexa = aHexaFile.read()

bHexaFile = open("HEXA_B.txt")
bHexa = bHexaFile.read()

aSOD1File = open("SOD1_A.txt")
aSOD1 = aSOD1File.read()

bSOD1File = open("SOD1_B.txt")
bSOD1 = bSOD1File.read()

#Transcribe and translate each codon
def transcribe(string):
    Rna=""
    for item in string:
        if item=="A":
            Rna+="U"
        elif item=="T":
            Rna+="A"
        elif item=="C":
            Rna+="G"
        elif item=="G":
            Rna+="C"
    return Rna


def translate(RNA):
    counter = 0
    variable = ''
    proteins  = ''
    for item in RNA:
        counter += 1
        if counter % 3 == 0:
            variable += item
            if variable == "UUU" or variable == "UUC":
                proteins  +="F"
            elif variable == "UUA" or variable == "UUG" or variable == "CUU" or variable == "CUC" or variable == "CUA" or variable == "CUG":
                proteins  +="L"
            elif variable == "AUU" or variable == "AUC" or variable == "AUA":
                proteins +="I"
            elif variable == "AUG":
                proteins +="M"
            elif variable == "GUU" or variable == "GUC" or variable == "GUA" or variable == "GUG":
                proteins +="V"
            elif variable == "UCU" or variable == "UCC" or variable == "UCA" or variable == "UCG":
                proteins +="S"
            elif variable == "CUU" or variable == "CCC" or variable == "CCA" or variable == "CCG":
                proteins +="P"
            elif variable == "ACU" or variable == "ACC" or variable == "ACA" or variable == "ACG":
                proteins +="T"
            elif variable == "GCU" or variable == "GCC" or variable == "GCA" or variable == "GCG":
                proteins +="A"
            elif variable == "UAU" or variable == "UAC":
                proteins +="Y"
            elif variable == "UAA" or variable == "UAG":
                proteins +="X"
            elif variable == "CAU" or variable == "CAC":
                proteins +="H"
            elif variable == "CAA" or variable == "CAG":
                proteins +="Q"
            elif variable == "AAU" or variable == "AAC":
                proteins +="N"
            elif variable == "AAA" or variable == "AAG":
                proteins +="K"
            elif variable == "GAU" or variable == "GAC":
                proteins +="D"
            elif variable == "GAA" or variable == "GAG":
                proteins +="E"
            elif variable == "UGU" or variable == "UGC":
                proteins +="C"
            elif variable == "UGA":
                proteins +="X"
            elif variable == "UGG":
                proteins +="W"
            elif variable == "CGU" or variable == "CGC" or variable == "CGA" or variable == "CGG":
                proteins +="R"
            elif variable == "AGU" or variable == "AGC":
                proteins +="S"
            elif variable == "AGA" or variable == "AGG":
                proteins +="R"
            elif variable == "GGU" or variable == "GGC" or variable == "GGA" or variable == "GGG":
                proteins +="G"     
            variable = ''      
        else:
            variable += item  
            
    return proteins  


# Identify mutations
def mutations(seq1, seq2):
    prot1 = (translate(transcribe(seq1)))
    prot2 = (translate(transcribe(seq2)))
    lenSeq1 = len(seq1)
    lenSeq2 = len(seq2)
    if lenSeq1 != lenSeq2:
        print("This is a frameshift mutation!")
    else:
        c = -1
        for char in prot1:
            c += 1
            if char == prot2[c]:
                continue
            else:
                if char == "X" or prot2[c] == "X":
                    print("This is a nonsense mutation!")
                else:
                    if char != "X" or prot2[c] != "X":
                        print("This is a missense mutation!")
mutations(aHemo, bHemo)
mutations(aHexa, bHexa)
mutations(aSOD1, bSOD1)            