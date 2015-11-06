import snoPatternSplit,sys,re

hacaFastaHum = "seq/haca_human_snoRNA.fa"
cdFastaHum = "seq/cd_human_snoRNA.fa"
hacaFastaGB = "seq/unique_haca_genbank.fa"
cdFastaGB = "seq/unique_cd_genbank.fa"
ncRNAGB = "seq/unique_rand_ncRNA_50-200_genbank.fa"
allDNAGB = "seq/unique_rand_allDNA_50-200_genbank.fa"


def getMaxLen(fastaIn):
	headerL = []
	seqL = []
	[headerL,seqL] = snoPatternSplit.fastaRead(fastaIn,True,False)	
	maxL = 0
	i = 0
	for seq in seqL:
		i += 1
		if len(seq)>maxL:
			maxL = len(seq)
			print i, ":",maxL, ":",seq
	return maxL
	
def getMinLen(fastaIn):
	headerL = []
	seqL = []
	[headerL,seqL] = snoPatternSplit.fastaRead(fastaIn,True,False)	
	minL = 99999999
	i = 0
	for seq in seqL:
		i += 1
		if len(seq)<minL:
			minL = len(seq)	
			print i, ':',minL, ':',seq
	return minL

print("hacaFastaGB")
print("max")
print(getMaxLen(hacaFastaGB))
print("min")
print(getMinLen(hacaFastaGB))

print("cdFastaGB")
print("max")
print(getMaxLen(cdFastaGB))
print("min")
print(getMinLen(cdFastaGB))

# print("ncRNAGB")
# print("max")
# print(getMaxLen(ncRNAGB))
# print("min")
# print(getMinLen(ncRNAGB))

# print("allGBDNA")
# print("max")
# print(getMaxLen(allDNAGB))
# print("min")
# print(getMinLen(allDNAGB))