import snoPatternSplit,sys,re,random,negativeDataGen,trainHoldSplit,snoPatternSplit,subprocess

hacaFastaHum = "seq/haca_human_snoRNA.fa"
cdFastaHum = "seq/cd_human_snoRNA.fa"
hacaFastaGB = "seq/unique_haca_genbank.fa"
cdFastaGB = "seq/unique_cd_genbank.fa"
ncRNAGB = "seq/unique_rand_ncRNA_50-200_genbank.fa"
allDNAGB = "seq/unique_rand_allDNA_50-200_genbank.fa"
filePrefix = "TEST"
foldN = 10;
#data in
print "reading files and generating neg seqs\n"
#pHead,pSeq = trainHoldSplit.fastaRead(typeFastaIn,True,False)
#nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncRNAGB,40,ncIn,40,True,20,True,False)
#randomizing for splits
print "randomizing for splits\n"
pHead = ["pHead1","pHead2","pHead3","pHead4","pHead5","pHead6","pHead7","pHead8","pHead9","pHead10","pHead11","pHead12","pHead13","pHead14","pHead15","pHead16","pHead17","pHead18","pHead19","pHead20","pHextra1"]
pSeq = ["pSeq1","pSeq2","pSeq3","pSeq4","pSeq5","pSeq6","pSeq7","pSeq8","pSeq9","pSeq10","pSeq11","pSeq12","pSeq13","pSeq14","pSeq15","pSeq16","pSeq17","pSeq18","pSeq19","pSeq20","pSextra1"]
nHead = ["nHead1","nHead2","nHead3","nHead4","nHead5","nHead6","nHead7","nHead8","nHead9","nHead10","nHead11","nHead12","nHead13","nHead14","nHead15","nHead16","nHead17","nHead18","nHead19","nHead20","nHextra1"]
nSeq = ["nSeq1","nSeq2","nSeq3","nSeq4","nSeq5","nSeq6","nSeq7","nSeq8","nSeq9","nSeq10","nSeq11","nSeq12","nSeq13","nSeq14","nSeq15","nSeq16","nSeq17","nSeq18","nSeq19","nSeq20","nSextra1"]
print "length n head:", len(nHead),"\nphead:",len(pHead),"\nnSeq",len(nSeq),"\npSeq",len(pSeq),"\n"


#creating a cross fold set
pVerList = []
nVerList = []
divCount = (len(pSeq)-len(pSeq)%foldN)/foldN
print "popping for the crossfold stuff\ndivcount is:",divCount,"\n"
while(len(pVerList)<foldN):
	tempNHead = []
	tempPHead = []
	tempNSeq = []
	tempPSeq = []
	for i in range(0,divCount):
		tempNHead.append(nHead.pop())
		tempPHead.append(pHead.pop())
		tempNSeq.append(nSeq.pop())
		tempPSeq.append(pSeq.pop())
		print i
	print tempPSeq
	print tempNSeq
	pVerList.append([tempPHead,tempPSeq])
	nVerList.append([tempNHead,tempNSeq])
	#print "sublist:", len(pVerList[len(pVerList)-1][0]),"\ntemp seq L", len(tempPSeq)
functionList = []
#creates files for crossfold cases
print "creating files for each crossfold case\n"
for i in range(0,len(pVerList)):
	#print "\npverlist: ",len(pVerList), ":",str(i)
	nHold = nVerList.pop(i)
	print "nHold Head:", nHold[0],"\nnHold Seq:",nHold[1]
	pHold = pVerList.pop(i)
	print "pHold Head:", pHold[0],"\npHold Seq:",pHold[1]
	#print "phold",len(pHold), "\n"
	nTrainHead	= []
	nTrainSeq = []
	pTrainHead = []
	pTrainSeq = []
	print "makeTrain: ",len(pVerList), ":",str(i)
	for j in range(0,len(pVerList)):
		#print "makeTrain: ",len(pVerList), ":",str(i), ":", str(j)
		for k in range(0,len(nVerList[j][0])):
			nTrainHead.append(nVerList[j][0][k])
			print "neg Head:",nVerList[j][0][k]
			nTrainSeq.append(nVerList[j][1][k])
			print "neg Seq:",nVerList[j][1][k]
			pTrainHead.append(pVerList[j][0][k])
			print "pos Head:",pVerList[j][0][k]
			pTrainSeq.append(pVerList[j][1][k])
			print "pos Seq:",pVerList[j][1][k]
	print nTrainHead
	print nTrainSeq
	print pTrainHead
	print pTrainSeq
	print "length p train: ",len(pTrainSeq),"\nlength phold: ",len(pHold[0]),"\ntotal:", str(len(pTrainSeq)+len(pHold[0]))
	functionName = filePrefix + "_10fh" + str(i)
	#crumInputGen(kmerSize,directory,functionName,nHold,pHold,[nTrainHead,nTrainSeq],[pTrainHead,pTrainSeq])
	print functionName
	functionList.append(functionName)
	#print "before reinsert:", len(pVerList)
	pVerList.insert(i,pHold)
	nVerList.insert(i,nHold)  
	#print "after reinsert:", len(pVerList)
# masterName = filePrefix + "_10foldMaster_k" + str(kmerSize)
# print(len(pSeq))
# mTemplate = open("TEMPLATE_ncRNA_foldMaster.m")
# mFile = open((directory + masterName + ".m"), 'w')
# matlabBatch = ""
# errorName = "totalErr_" + filePrefix;
# for name in functionList:
	# matlabBatch += "[errTest_" + name + ",errTrain_" + name +  "] = " + name + "();\n" + errorName + "= [" + errorName+ ";[errTest_" + name + ",errTrain_" + name +  "]];\n"
# for line in mTemplate:
	# line = line.replace("%ERRNAME%",  errorName)
	# line = line.replace("%FUNCTIONBATCH%",matlabBatch)
	# mFile.write(line)
# mFile.close()
# mTemplate.close()