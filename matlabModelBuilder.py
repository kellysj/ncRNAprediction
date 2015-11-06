import snoPatternSplit,sys,re,random,negativeDataGen,trainHoldSplit,snoPatternSplit,subprocess

hacaFastaHum = "seq/haca_human_snoRNA.fa"
cdFastaHum = "seq/cd_human_snoRNA.fa"
hacaFastaGB = "seq/unique_haca_genbank.fa"
cdFastaGB = "seq/unique_cd_genbank.fa"
ncRNAGB = "seq/unique_rand_ncRNA_50-200_genbank.fa"
allDNAGB = "seq/unique_rand_allDNA_50-200_genbank.fa"

#this is just a default function, needs to be rewritten for a 10fold validation
#compiles positive data, generates and compiles negative data
#creates holdout set and training set
def crumDataGen(percHold,allIn,ncIn,typeIn,filePrefix,directory):
	#build datasets for the models
	#1. create postive and negative datasets
	pHead,pSeq = trainHoldSplit.fastaRead(typeIn,True,True)
	nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncIn,40,allIn,40,True,20,True,False)
	#holdout splits
	pHeadTrain,pSeqTrain,pHeadHold,pSeqHold = trainHoldSplit.randomSelect(percHold,pHead,pSeq,True,True)
	nHeadTrain,nSeqTrain,nHeadHold,nSeqHold = trainHoldSplit.randomSelect(percHold,nHead,nSeq,True,False)

	#writing Fastas
	trainHoldSplit.fastaWrite(pHeadTrain,pSeqTrain, directory + "DATA_"+  filePrefix + "_pos_train.fa")
	trainHoldSplit.fastaWrite(pHeadHold,pSeqHold, directory +"DATA_"+  filePrefix + "_pos_hold.fa")
	trainHoldSplit.fastaWrite(nHeadTrain,nSeqTrain, directory +"DATA_"+  filePrefix +"_neg_train.fa")
	trainHoldSplit.fastaWrite(nHeadHold,nSeqHold, directory +"DATA_"+  filePrefix + "_neg_hold.fa")


#creates an input for crum by splitting up data AND processing features
def crumInputGen(kmerSize,directory,filePrefix,nHoldIn,pHoldIn,nTrainIn,pTrainIn):

	pHeadTrain,pSeqTrain =  pTrainIn
	pHeadHold,pSeqHold =  pHoldIn
	nHeadTrain,nSeqTrain =  nTrainIn
	nHeadHold,nSeqHold =  nHoldIn

	posT = 1
	negT = 0
	#2. run feature selection
	pFt,pTt = snoPatternSplit.featureFinder(pSeqTrain,posT,kmerSize,True,False)
	nFt,nTt = snoPatternSplit.featureFinder(nSeqTrain,negT,kmerSize,True,False)
	pFh,pTh = snoPatternSplit.featureFinder(pSeqHold,posT,kmerSize,True,False)
	nFh,nTh = snoPatternSplit.featureFinder(nSeqHold,negT,kmerSize,True,False)

	trainName = "FEAT" +  "_" + filePrefix+ "_" +  str(kmerSize).replace("-","n") + "_" + "all_train"
	holdName = "FEAT" +  "_" + filePrefix+ "_" +  str(kmerSize).replace("-","n") + "_" + "all_hold"

	snoPatternSplit.writeToMfile(pFt+nFt,pTt+nTt,pHeadTrain+nHeadTrain,trainName,directory,False)
	snoPatternSplit.writeToMfile(pFh+nFh,pTh+nTh,pHeadHold+nHeadHold,holdName,directory,False)



	nameOut = filePrefix

	mTemplate = open("TEMPLATE_ncRNA_testing.m")
	mFile = open((directory + nameOut + ".m"), 'w')
	for line in mTemplate:
		line = line.replace("%FUNCTONNAME%",nameOut)
		line = line.replace("%TRAINING%",trainName)
		line = line.replace("%HOLDING%",holdName)
		mFile.write(line)
	mFile.close()
	mTemplate.close()

def SplitFasta(nSplit,FastaIn):
	Head,Seq = trainHoldSplit.fastaRead(typeIn,True,True)
	n = len(pSeq)
		

#final function, runs everything
def runCrumInputGen(filePrefix,typeFastaIn,kmerLen):
	directory = "./" + filePrefix + "/"
	if subprocess.call(["mkdir", directory]) == 0:
		subprocess.call(["rm", "-r " + directory])
		subprocess.call(["mkdir", directory])
	crumDataGen(allDNAGB,ncRNAGB,typeFastaIn,filePrefix,directory)
	nHold = directory+"DATA_"+filePrefix+"_neg_hold.fa"
	pHold = directory+"DATA_"+filePrefix+"_pos_hold.fa"
	nTrain = directory+"DATA_"+filePrefix+"_neg_train.fa"
	pTrain = directory+"DATA_"+filePrefix+"_pos_train.fa"
	for i in range(2,kmerLen+1):
		crumInputGen(i,directory,filePrefix,nHold,pHold,nTrain,pTrain)

#runCrumInputGen("cd_uni_1",cdFastaGB,5)
#runCrumInputGen("haca_uni_1",hacaFastaGB,5)
def nFoldCrumInputGen(nFolds,allIn,ncIn,typeFastaIn,filePrefix,kmerSize):
	directory = "./" + filePrefix + "/"
	if subprocess.call(["mkdir", directory]) != 0:
		print directory + " exists... clean up" 
		subprocess.call(["rm", "-r ", directory])
		subprocess.call(["mkdir", directory])
	foldN = nFolds;
	#data in
	print "reading files and generating neg seqs\n"
	pHead,pSeq = trainHoldSplit.fastaRead(typeFastaIn,True,False)
	nHead,nSeq = negativeDataGen.compileData(len(pSeq),ncRNAGB,40,ncIn,40,True,20,True,False)
	#randomizing for splits
	print "randomizing for splits\n"
	pHead,pSeq,no1,no2 = trainHoldSplit.randomSelect(0.0,pHead,pSeq,True,False)
	nHead,nSeq,no1,no2 = trainHoldSplit.randomSelect(0.0,nHead,nSeq,True,False)
	#print nHead
	#print pHead
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
			#print i
		#print tempPSeq
		#print tempNSeq
		pVerList.append([tempPHead,tempPSeq])
		nVerList.append([tempNHead,tempNSeq])
		#print "sublist:", len(pVerList[len(pVerList)-1][0]),"\ntemp seq L", len(tempPSeq)
	functionList = []
	#creates files for crossfold cases
	print "creating files for each crossfold case\n"
	for i in range(0,len(pVerList)):
		#print "\npverlist: ",len(pVerList), ":",str(i)
		nHold = nVerList.pop(i)
		#print "nHold Head:", nHold[0],"\nnHold Seq:",nHold[1]
		pHold = pVerList.pop(i)
		#print "pHold Head:", pHold[0],"\npHold Seq:",pHold[1]
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
				#print "neg Head:",nVerList[j][0][k]
				nTrainSeq.append(nVerList[j][1][k])
				#print "neg Seq:",nVerList[j][1][k]
				pTrainHead.append(pVerList[j][0][k])
				#print "pos Head:",pVerList[j][0][k]
				pTrainSeq.append(pVerList[j][1][k])
				#print "pos Seq:",pVerList[j][1][k]
		#print nTrainHead
		#print nTrainSeq
		#print pTrainHead
		#print pTrainSeq
		print "length p train: ",len(pTrainSeq),"\nlength phold: ",len(pHold[0]),"\ntotal:", str(len(pTrainSeq)+len(pHold[0]))
		functionName = filePrefix + "_10fh" + str(i)
		crumInputGen(kmerSize,directory,functionName,nHold,pHold,[nTrainHead,nTrainSeq],[pTrainHead,pTrainSeq])
		print functionName
		functionList.append(functionName)
		#print "before reinsert:", len(pVerList)
		pVerList.insert(i,pHold)
		nVerList.insert(i,nHold)  
		#print "after reinsert:", len(pVerList)
	masterName = filePrefix + "_10foldMaster"
	print(len(pSeq))
	mTemplate = open("TEMPLATE_ncRNA_foldMaster.m")
	mFile = open((directory + masterName + ".m"), 'w')
	matlabBatch = ""
	errorName = "totalErr_" + filePrefix;
	for name in functionList:
		matlabBatch += "[errTest_" + name + ",errTrain_" + name +  "] = " + name + "();\n" + errorName + "= [" + errorName+ ";[errTest_" + name + ",errTrain_" + name +  "]];\n"
	for line in mTemplate:
		line = line.replace("%ERRNAME%",  errorName)
		line = line.replace("%FUNCTIONBATCH%",matlabBatch)
		mFile.write(line)
	mFile.close()
	mTemplate.close()
	
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,hacaFastaGB,"haca_1_k2_10f",2)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,hacaFastaGB,"haca_1_k3_10f",3)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,hacaFastaGB,"haca_1_k4_10f",4)
nFoldCrumInputGen(10,allDNAGB,ncRNAGB,hacaFastaGB,"haca_1_k5_10f",5)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,hacaFastaGB,"haca_1_k6_10f",6)

#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,cdFastaGB,"cd_1_k2_10f",2)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,cdFastaGB,"cd_1_k3_10f",3)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,cdFastaGB,"cd_1_k4_10f",4)
nFoldCrumInputGen(10,allDNAGB,ncRNAGB,cdFastaGB,"cd_1_k5_10f",5)
#nFoldCrumInputGen(10,allDNAGB,ncRNAGB,cdFastaGB,"cd_1_k6_10f",6)

#subprocess.call(["usearch8.0.1623_i86linux32", "-derep_fulllength", testName, "-strand", "both", "-fastaout" , "unique_" + testName])
























































