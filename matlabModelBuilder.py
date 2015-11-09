import snoPatternSplit,sys,re,random,negativeDataGen,trainHoldSplit,snoPatternSplit,subprocess,fastaU,os

hacaFastaHum = "seq/haca_human_snoRNA.fa"
cdFastaHum = "seq/cd_human_snoRNA.fa"
hacaFastaGB = "seq/unique_haca_genbank.fa"
cdFastaGB = "seq/unique_cd_genbank.fa"
ncRNAGB = "seq/unique_rand_ncRNA_50-200_genbank.fa"
allDNAGB = "seq/unique_rand_allDNA_50-200_genbank.fa"
	
	
"""
A function that writes the feature vectors as well as the type vectors to an m-file for matlab processing
featuresIn = the feature vectors to write to the file
headersIn = the headers associated with the sequences and features (not neccesarily used)
nameOut = the name for the file and the matlab function to load it
debug = boolean for printing debug data
"""	
def writeToMfile(featuresIn,typesIn,headersIn,nameOut,directory,debug):
	totalData = featuresIn
	mFileHeader = "function [X,t,header] = " + nameOut + "()\n"
	mFileEnd = "end"
	#generating strings for an m-file
	fOut = "\tX={\n"
	nRow = 0
	counter = 0;
	nItem = 0
	#features
	for item in featuresIn:
		counter += 1
		nItem += 1
		fOut += "\t\t"
		fOut += str(item)
		if nItem<len(featuresIn):
			fOut += ";\n"
		else:
			fOut += "\n\t};\n"
	nItem = 0
	tOut = "\tt={\n\t\t"
	counter = 0;
	#types
	if type(typesIn[0]) is list:
		for item in typesIn:
			counter += 1
			nItem += 1
			tOut += str(item)
			if nItem<len(typesIn):
				tOut += ";"
				if (counter%50)==0:
					tOut += "\n\t\t"
			else:
				tOut += "\n\t};"
	else:
		for item in typesIn:
			counter += 1
			nItem += 1
			tOut += " " + str(item) + " "
			if nItem<len(typesIn):
				tOut += ";"
			else:
				tOut += "\n\t};"
	#headers
	nItem = 0
	hOut = "\n\theader={\n\t\t"
	counter = 0;
	for item in headersIn:
		counter += 1
		nItem += 1
		hOut += "'" + item + "'"
		if nItem<len(headersIn):
			hOut += " ; "
		else:
			hOut += "\n\t};\n"
	if debug >=1:
		print tOut
		print fOut	
	mFile = open((directory+nameOut + ".m"), 'w')
	mFile.write(mFileHeader)
	mFile.write(fOut)
	mFile.write(tOut)
	mFile.write(hOut)
	mFile.write(mFileEnd)
	mFile.close()
	return
	

def randomizeSeqs(heads,seqs):
	seqOut = []
	headOut = []
	indices = range(len(heads))
	random.shuffle(indices)
	for n in indices:
		seqOut.append(seqs[n])
		headOut.append(heads[n])
	return [headOut,seqOut]	

def dataGen(percHold,allIn,ncIn,typeIn):
	#build datasets for the models
	#1. create postive and negative datasets
	pHead,pSeq = fastaU.read(typeIn,True,False)
	nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncIn,40,allIn,40,True,20,True,False)
	#randomize the data
	[pHead,pSeq] = randomizeSeqs(pHead,pSeq)
	[nHead,nSeq] = randomizeSeqs(nHead,nSeq)
	
	return pHead,pSeq,nHead,nSeq
	
def foldSplit(split,heads,seqs,types):
	lenSplit = len(heads)/split
	if lenSplit*split<len(heads):
		lenSplit += 1
	headOut = [0]*split
	seqOut = [0]*split
	typesOut = [0]*split
	i = 0
	#print "len(headOut) = " + str(len(headOut))
	for start in range(len(heads))[::lenSplit]:
		end = start + lenSplit
		#print "index is: " + str(i) + "\nstart is: " + str(start) + "\nend is: " + str(end)
		if end<len(heads):
			headOut[i] = heads[start:end]
			seqOut[i] = seqs[start:end]
			typesOut[i] = types[start:end]
		else:
			headOut[i] = heads[start:]
			seqOut[i] = seqs[start:]
			typesOut[i] = types[start:]
		i += 1
	return headOut,seqOut,typesOut
	
def writeCrumInput(trainHead,trainFeat,trainType,holdHead,holdFeat,holdType,directory,functionName):
	
	trainName = "FEAT_" + functionName + "_train"
	holdName = "FEAT_" + functionName + "_hold"

	writeToMfile(trainFeat,trainType,trainHead,trainName,directory,False)
	writeToMfile(holdFeat,holdType,holdHead,holdName,directory,False)

	mTemplate = open("TEMPLATE_ncRNA_testing.m")
	mFile = open((directory + functionName + ".m"), 'w')
	for line in mTemplate:
		line = line.replace("%FUNCTONNAME%",functionName)
		line = line.replace("%TRAINING%",trainName)
		line = line.replace("%HOLDING%",holdName)
		mFile.write(line)
	mFile.close()
	mTemplate.close()
	
def makeDirectory(name):
	FNULL = open(os.devnull, 'w')
	directory = "./" + name + "/"
	if subprocess.call(["ls", directory],stdout=FNULL, stderr=subprocess.STDOUT) == 0:
		subprocess.call(["rm", "-r", directory])
		subprocess.call(["mkdir", directory])
		subprocess.call(["chmod", "+s",directory])
	else:
		subprocess.call(["mkdir", directory])
		subprocess.call(["chmod", "+s",directory])		
		
def writeToMasterMfile(functionNameL,batchName,directory,masterName):
	mTemplate = open("TEMPLATE_ncRNA_foldMaster.m")
	mFile = open(("./" + directory + "/" + masterName + ".m"), 'a')
	for line in mTemplate:
		lineOut = line.replace("%BATCHNAME%",  batchName)
		if lineOut.find("%FUNCTIONNAME%") > 0:
			lineTemp = lineOut
			lineOut = ""
			for functionName in functionNameL:
				lineOut += (lineTemp.replace("%FUNCTIONNAME%", functionName).replace(";",";\n"))
		mFile.write(lineOut)
	mFile.close()
	mTemplate.close()
		
		

maxWindow = 4
prefix = "haca-1"
foldN = 10
directory = prefix
makeDirectory(directory)
masterName = "run_" + prefix

print "reading in fastas..."
#read and generate
pHead,pSeq = fastaU.read(hacaFastaGB,True,False)
nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncRNAGB,40,allDNAGB,40,True,20,True,False)

print "randomizing data..."
#randomize the data
pHead,pSeq = randomizeSeqs(pHead,pSeq)
nHead,nSeq = randomizeSeqs(nHead,nSeq)

print "making type lists..."
#make type lists
pType = [1]*len(pHead)
nType = [0]*len(nHead)

#make holdouts
print "spliting for fold validation..."
pHeadL,pSeqL,pTypeL = foldSplit(foldN,pHead,pSeq,pType)
nHeadL,nSeqL,nTypeL = foldSplit(foldN,nHead,nSeq,nType)

print "writing splits to fastas..."
for i in range(len(pHeadL)):
	fastaU.write(pHeadL[i],pSeqL[i],("./" + directory + "/fold-" + str(i) + "_pos_" + prefix + ".fasta"))

for i in range(len(nHeadL)):
	fastaU.write(nHeadL[i],nSeqL[i],("./" + directory + "/fold-" + str(i) + "_neg_" + prefix + ".fasta"))

print "generating scripts per window width..."
for window in range(maxWindow):
	print "for window " + str(window) + "..."
	#gather features		
	pFeatL = []
	nFeatL = []
	print "getting features..."
	for seqL in pSeqL:
		pFeatT = []
		for seq in seqL:
			pFeatT.append(str(snoPatternSplit.makeFeatureVector(seq,window+1)))
		pFeatL.append(pFeatT)
		
	for seqL in nSeqL:
		nFeatT = []
		for seq in seqL:
			nFeatT.append(str(snoPatternSplit.makeFeatureVector(seq,window+1)))
		nFeatL.append(nFeatT)
		
	print "done."
	#set up a directory
	subPrefix = "window-" + str(window+1)
	subDirectory = directory + "/" + subPrefix
	makeDirectory(subDirectory)
	batchName = (subPrefix + "_" + prefix)
	functionBatchL = []
	for j in range(foldN):
		print "writing files for fold " + str(j) + "..."
		cpHeadL = pHeadL[:]
		cpTypeL = pTypeL[:]
		cpFeatL = pFeatL[:]
		cnHeadL = nHeadL[:]
		cnTypeL = nTypeL[:]
		cnFeatL = nFeatL[:]
		functionName = ("fold_" + str(j) + "_" + subPrefix + "_" + prefix).replace("-","_")
		functionBatchL.append(functionName)
		holdHead = cpHeadL.pop(j) + cnHeadL.pop(j)
		trainHeadL = cpHeadL + cnHeadL
		trainHead = []
		for tHead in trainHeadL:
			trainHead += tHead
			
		holdFeat = cpFeatL.pop(j) + cnFeatL.pop(j)
		trainFeat = []
		trainFeatL = cpFeatL + cnFeatL
		for tFeat in trainFeatL:
			trainFeat += tFeat
			
		holdType = cpTypeL.pop(j) + cnTypeL.pop(j)
		trainType = []
		trainTypeL = cpTypeL + cnTypeL
		for tType in trainTypeL:
			trainType += tType
		writeCrumInput(trainHead,trainFeat,trainType,holdHead,holdFeat,holdType,(subDirectory + "/"),functionName)
	writeToMasterMfile(functionBatchL,batchName.replace("-","_").replace("window_","w"),directory,masterName.replace("-","_"))
subprocess.call(["chmod", "775","-R", ("./" + directory + "/")])


#################################################################################################################################


maxWindow = 4
prefix = "cd-1"
foldN = 10
directory = prefix
makeDirectory(directory)
masterName = "run_" + prefix

print "reading in fastas..."
#read and generate
pHead,pSeq = fastaU.read(cdFastaGB,True,False)
nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncRNAGB,40,allDNAGB,40,True,20,True,False)

print "randomizing data..."
#randomize the data
pHead,pSeq = randomizeSeqs(pHead,pSeq)
nHead,nSeq = randomizeSeqs(nHead,nSeq)

print "making type lists..."
#make type lists
pType = [1]*len(pHead)
nType = [0]*len(nHead)

#make holdouts
print "spliting for fold validation..."
pHeadL,pSeqL,pTypeL = foldSplit(foldN,pHead,pSeq,pType)
nHeadL,nSeqL,nTypeL = foldSplit(foldN,nHead,nSeq,nType)

print "writing splits to fastas..."
for i in range(len(pHeadL)):
	fastaU.write(pHeadL[i],pSeqL[i],("./" + directory + "/fold-" + str(i) + "_pos_" + prefix + ".fasta"))

for i in range(len(nHeadL)):
	fastaU.write(nHeadL[i],nSeqL[i],("./" + directory + "/fold-" + str(i) + "_neg_" + prefix + ".fasta"))

print "generating scripts per window width..."
for window in range(maxWindow):
	print "for window " + str(window) + "..."
	#gather features		
	pFeatL = []
	nFeatL = []
	print "getting features..."
	for seqL in pSeqL:
		pFeatT = []
		for seq in seqL:
			pFeatT.append(str(snoPatternSplit.makeFeatureVector(seq,window+1)))
		pFeatL.append(pFeatT)
		
	for seqL in nSeqL:
		nFeatT = []
		for seq in seqL:
			nFeatT.append(str(snoPatternSplit.makeFeatureVector(seq,window+1)))
		nFeatL.append(nFeatT)
		
	print "done."
	#set up a directory
	subPrefix = "window-" + str(window+1)
	subDirectory = directory + "/" + subPrefix
	makeDirectory(subDirectory)
	batchName = (subPrefix + "_" + prefix)
	functionBatchL = []
	for j in range(foldN):
		print "writing files for fold " + str(j) + "..."
		cpHeadL = pHeadL[:]
		cpTypeL = pTypeL[:]
		cpFeatL = pFeatL[:]
		cnHeadL = nHeadL[:]
		cnTypeL = nTypeL[:]
		cnFeatL = nFeatL[:]
		functionName = ("fold_" + str(j) + "_" + subPrefix + "_" + prefix).replace("-","_")
		functionBatchL.append(functionName)
		holdHead = cpHeadL.pop(j) + cnHeadL.pop(j)
		trainHeadL = cpHeadL + cnHeadL
		trainHead = []
		for tHead in trainHeadL:
			trainHead += tHead
			
		holdFeat = cpFeatL.pop(j) + cnFeatL.pop(j)
		trainFeat = []
		trainFeatL = cpFeatL + cnFeatL
		for tFeat in trainFeatL:
			trainFeat += tFeat
			
		holdType = cpTypeL.pop(j) + cnTypeL.pop(j)
		trainType = []
		trainTypeL = cpTypeL + cnTypeL
		for tType in trainTypeL:
			trainType += tType
		writeCrumInput(trainHead,trainFeat,trainType,holdHead,holdFeat,holdType,(subDirectory + "/"),functionName)
	writeToMasterMfile(functionBatchL,batchName.replace("-","_").replace("window_","w"),directory,masterName.replace("-","_"))
subprocess.call(["chmod", "775","-R", ("./" + directory + "/")])






















































