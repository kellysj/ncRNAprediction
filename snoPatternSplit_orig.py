"""
snoPatternSplit
HBoxes:
	ANANNA - flanked by 2 large hairpin formations
C/D:
boxes C (RUGAUGA, R=purine) and D (CUGA)
"""
import sys
import re
testHead = "U97"
testSeq = "UUGCCCGAUGAUUAUAAAAAGACGCGUUAUUAAGAGGACUUUAUGCUGGAGUUCUUGACGUUUUUCUCUCUUUUCUAUACUUCUUUUUCUUUCUUUGAAUGUCCAGCGUCCUGUGAGCGAAGAUUAUGAGAUAUGAGGGCAA"
hboxFeatureList = ["AAAAAA","AAAAUA","AAAAGA","AAAACA","AAAUAA","AAAUUA","AAAUGA","AAAUCA","AAAGAA","AAAGUA","AAAGGA","AAAGCA","AAACAA","AAACUA","AAACGA","AAACCA","AUAAAA","AUAAUA","AUAAGA","AUAACA","AUAUAA","AUAUUA","AUAUGA","AUAUCA","AUAGAA","AUAGUA","AUAGGA","AUAGCA","AUACAA","AUACUA","AUACGA","AUACCA","AGAAAA","AGAAUA","AGAAGA","AGAACA","AGAUAA","AGAUUA","AGAUGA","AGAUCA","AGAGAA","AGAGUA","AGAGGA","AGAGCA","AGACAA","AGACUA","AGACGA","AGACCA","ACAAAA","ACAAUA","ACAAGA","ACAACA","ACAUAA","ACAUUA","ACAUGA","ACAUCA","ACAGAA","ACAGUA","ACAGGA","ACAGCA","ACACAA","ACACUA","ACACGA","ACACCA"]
cboxFeatureList = ["AUGAUGA","AUGAAGA","AGGAUGA","AGGAAGA","AUGAUGU","AUGAAGU","AGGAUGU","AGGAAGU","AUGAUGG","AUGAAGG","AGGAUGG","AGGAAGG","AUGAUGC","AUGAAGC","AGGAUGC","AGGAAGC","UUGAUGA","UUGAAGA","UGGAUGA","UGGAAGA","UUGAUGU","UUGAAGU","UGGAUGU","UGGAAGU","UUGAUGG","UUGAAGG","UGGAUGG","UGGAAGG","UUGAUGC","UUGAAGC","UGGAUGC","UGGAAGC","GUGAUGA","GUGAAGA","GGGAUGA","GGGAAGA","GUGAUGU","GUGAAGU","GGGAUGU","GGGAAGU","GUGAUGG","GUGAAGG","GGGAUGG","GGGAAGG","GUGAUGC","GUGAAGC","GGGAUGC","GGGAAGC","CUGAUGA","CUGAAGA","CGGAUGA","CGGAAGA","CUGAUGU","CUGAAGU","CGGAUGU","CGGAAGU","CUGAUGG","CUGAAGG","CGGAUGG","CGGAAGG","CUGAUGC","CUGAAGC","CGGAUGC","CGGAAGC"]
def pnDictCompare(posDict,negDict):
	out = ""
	sortedList = sorted(posDict, key=posDict.get)
	for k in sortedList[::-1]:
		out += k + "\t" + str(posDict[k]) + "\t"
		if k in negDict:
			out += str(negDict[k])
			del negDict[k]
		else:
			out += "0"
		out += "\n"
	for k in negDict:
		out += k + "\t0\t" + str(negDict[k]) + "\n"
	return out
	
	
def freqTableToString(freqTin,flatten):
	out = ""
	dictFreq = {}
	for row in freqTin:
		freqAdd = ""
		for num in row:
			if flatten and num > 1:
				freqAdd += "1"
			else:
				freqAdd += str(num)
		if freqAdd in dictFreq:
			dictFreq[freqAdd] += 1
		else:
			dictFreq[freqAdd] = 1
	sortedList = sorted(dictFreq,key=dictFreq.get)
	for k in sortedList[::-1]:
		out += k + ":" + str(dictFreq[k]) + "\n"
	return out
def tMake(typeIn,dim):
	if dim == 1:
		return typeIn
	else:
		tList = [0,0,0]
		if typeIn - 4 >= 0:
			tList[2] = 1
			typeIn = typeIn-4
		else:
			tList[2] = -1
		if typeIn - 2 >= 0:
			tList[1] = 1
			typeIn = typeIn-2
		else:
			tList[1] = -1
		if typeIn - 1 >= 0:
			tList[0] = 1
			typeIn = typeIn-1
		else:
			tList[0] = -1
		return tList
hboxre = re.compile(r'([A].{1}[A].{2}[A])')
acare = re.compile(r'(ACA)')
dboxre = re.compile(r'(CUGA)')
cboxre = re.compile(r'([AUGC]UGAUG[AUGC])')
headerre = re.compile(r'>(.*)')
seqre = re.compile(r'^[UNATGC]+')
failre = re.compile(r'JOLLY')

def generateKmersRec(len):
	nucList1 = ["A","U","G","C"]
	if len==0:
		return ","
	for n1 in nucList1:
		return n1 + generateKmersRec(len-1)

def MotifMatch(reIn, seqIn, percLT, percGT, headerIn, flipped, debug):
	"""
	reIn = compiled regex to search with
	seqIn = the RNA or DNA to search
	Note:
	matchIndex/length(seqIn) = iRatio 
	percGT = iRatio that valid matches are greater than
	percLT = iRatio that valid matches are less than
	headerIn = a string for the header of the sequence 
	debug = will print debug info for the method to the command line
	matchList = a list of valid match objects from the 
	"""
	matchList = []
	badMatch = 0
	debugString = ""
	if debug:
		debugString = headerIn
	seq = seqIn.replace("T","U")
	boxMatch = re.finditer(reIn, seq)	
	nSearchMatch = 0
	for match in boxMatch:
		nSearchMatch += 1
		h_index = match.start()
		total_length = len(seq)
		index_ratio = h_index/float(total_length)
		matchString = "+"
		if (index_ratio>percGT) and (index_ratio<percLT):
			matchList.append(match)
		else:
			badMatch += 1
			matchString = "-"
		if debug:
			debugString += "\n"
			debugString +=  str(nSearchMatch)
			debugString += " : "
			debugString += str(("%.2f" % index_ratio))
			debugString += str(match.span())
			debugString += "\t"
			debugString += match.group()
			debugString += "("
			debugString += matchString
			debugString += ")"
	if len(matchList)==0 and flipped == False:
		flipped = True
		[matchList,badMatch,flipped,debugString] = MotifMatch(reIn, seqIn[::-1], percLT, percGT, headerIn,flipped, debug)	
	if debug:
		print debugString
	return matchList,badMatch,flipped,debugString

	
def motifStats(reIn,percLT, percGT,fasta, debug):
	motifList = {}
	nseq = 0
	nheader = 0
	nlines = 0
	totallength = 0
	header = ""
	nMatch = 0
	nUnMatched = 0
	nBadMatch = 0
	nUnFlipped = 0
	nFlipped = 0
	totalMultiMatches = 0
	nmultimotif = 0
	for line in open(fasta):
		nlines += 1
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			nheader += 1
			header = headerMatch.group(0)
		if seqMatch:
			nseq += 1
			seq = seqMatch.group()
			seq = seq.replace("T","U")
			totallength += len(seq)
			[validMotifs,badMotifs,isFlipped,outString] = MotifMatch(reIn,seq,percLT,percGT,header,False,debug)
			
			if len(validMotifs) > 0:
				#print header
				if len(validMotifs) > 1:
					nmultimotif += 1
					totalMultiMatches += len(validMotifs)
				nMatch += 1
				if isFlipped:
					nFlipped +=1
				else:
					nUnFlipped +=1				
				for match in validMotifs:
					motif = match.group()
					if motif in motifList:
						motifList[motif] += 1
					else:
						motifList[motif] = 1
					#print "%.2f" % (match.start()/float(len(seq))) , ":" , match.group()
			else:
				if badMotifs > 0:
					nBadMatch += 1
				else:
					nUnMatched += 1
					#print header
					#print seq
	sortedList = sorted(motifList, key=motifList.get)
	
	percmatchL = "%.1f" % (100.0*(float(nMatch)/float(totallength)))
	permatchS = "%.1f" % (100*(float(nMatch)/float(nseq)))
	if nmultimotif>0:
		motifperseq = "%.2f" % (float(totalMultiMatches)/float(nmultimotif))
	else:
		motifperseq = 0
	print "seq Count: ", nseq
	print "avg Length: ", "%.1f" % (float(totallength)/float(nseq))
	print "total matches: ", nMatch
	print "% matching sequences: ", permatchS
	print "avg motif count per seq: ", motifperseq
	print "multi motif seqs: ", nmultimotif
	#for motif in sortedList:
	#	print motif, ":", motifList[motif]
	return motifList,nseq,totallength,nMatch,nUnMatched,nBadMatch,nUnFlipped,nFlipped,totalMultiMatches,nmultimotif

	
def hacaFind(fasta,type, debug):
	tOut = tMake(type,1)
	hboxre = re.compile(r'([A].{1}[A].{2}[A])')
	acare = re.compile(r'(ACA)')
	hmotifList = {}
	header = ""
	nTotal = 0
	nHbox = 0
	nAca = 0
	nBoth = 0
	nNone = 0
	fList = []
	for line in open(fasta):
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			header = headerMatch.group(0)
		if seqMatch:
			nTotal += 1
			seq = seqMatch.group()
			seq = seq.replace("T","U")
			#H BOX STUFF IS HERE
			hacaFeatureList = []
			for i in range(len(hboxFeatureList)+1):
				hacaFeatureList.append(0)	
			[hMotifs,hbMotifs,hisFlipped,houtString] = MotifMatch(hboxre,seq,.7,.3,header,False,False)
			if len(hMotifs) > 0:		
				seq = hMotifs[0].string
				for match in hMotifs:
					motif = match.group()
					hacaFeatureList[hboxFeatureList.index(motif)+1] = 1 #THE FEATURE MATRIX IS BUILT HERE!!!
					if motif in hmotifList:
						hmotifList[motif] += 1
					else:
						hmotifList[motif] = 1				
			#ACA TAIL IS HERE
			[acaMotifs,acabMotifs,acaisFlipped,acaoutString] = MotifMatch(acare,seq,1,.9,header,True,False)
			hacaFeatureList[0] = len(acaMotifs)
			if len(acaMotifs) > 0 and len(hMotifs) > 0:
				nBoth += 1
			else:
				if len(acaMotifs) > 0:
					nAca += 1
				if len(hMotifs) > 0:
					nHbox += 1
				else:
					nNone += 1
			#print hacaFeatureList
			fList.append(hacaFeatureList)
	hsortedList = sorted(hmotifList, key=hmotifList.get)
	
	for motif in hsortedList[::-1]:
		print motif, ":", hmotifList[motif]
	if debug:
		print "total: ", nTotal, "\nhbox: ",("%.2f" % (100*float(nHbox)/nTotal)), "\naca: ",("%.2f" % (100*float(nAca)/nTotal)), "\nBoth: ",("%.2f" % (100*float(nBoth)/nTotal)), "\nNone: ",("%.2f" % (float(100*nNone)/nTotal))
	return fList

	
def cdFind(fasta,type, debug):
	tOut = tMake(type,1)
	dboxre = re.compile(r'(CUGA)')
	cboxre = re.compile(r'([AUGC][UG]GA[UA]G[AUGC])')
	cMotifList = {}
	header = ""
	nTotal = 0
	nCbox = 0
	nDbox = 0
	nBoth = 0
	nNone = 0
	for line in open(fasta):
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			header = headerMatch.group(0)
		if seqMatch:
			nTotal += 1
			seq = seqMatch.group()
			seq = seq.replace("T","U")
			#C box IS HERE
			[cMotifs,hbMotifs,hisFlipped,coutString] = MotifMatch(cboxre,seq,1,0,header,False,debug)
			if len(cMotifs) > 0:
				seq = cMotifs[0].string
				for match in cMotifs:
					motif = match.group()
					if motif in cMotifList:
						cMotifList[motif] += 1
					else:
						cMotifList[motif] = 1
			#D box IS HERE
			[dMotifs,dbMotifs,dIsFlipped,dOutString] = MotifMatch(dboxre,seq,1,0,header,True,debug)
			if len(dMotifs) > 0 and len(cMotifs) > 0:
				nBoth += 1
			else:
				if len(dMotifs) > 0:
					nDbox += 1
				if len(cMotifs) > 0:
					nCbox += 1
				else:
					nNone += 1
	csortedList = sorted(cMotifList, key=cMotifList.get)
	
	for motif in csortedList[::-1]:
		print motif, ":", cMotifList[motif]
	print "total: ", nTotal, "\ncbox: ",("%.2f" % (100*float(nCbox)/nTotal)), "\nDbox: ",("%.2f" % (100*float(nDbox)/nTotal)), "\nBoth: ",("%.2f" % (100*float(nBoth)/nTotal)), "\nNone: ",("%.2f" % (100*float(nNone)/nTotal))
	return

	
def snoMotifFind(fasta,type, debug):
	matchDebug = False
	if debug >= 3:
		matchDebug = True
	tOut = tMake(type,1)
	hboxre = re.compile(r'([A].{1}[A].{2}[A])')
	acare = re.compile(r'(ACA)')
	dboxre = re.compile(r'(CUGA)')
	cboxre = re.compile(r'([AUGC][UG]GA[UA]G[AUGC])')
	hMotifDict = {}
	cMotifDict = {}
	header = ""
	fList = []
	freqOfFeaturesList = []
	for line in open(fasta):
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			header = headerMatch.group(0)
		if seqMatch:
			seq = seqMatch.group()
			seq = seq.replace("T","U")
		#Creating empty feature vectors
			hacaFeatures = []
			for i in range(len(hboxFeatureList)):
				hacaFeatures.append(0)
			cdFeatures = []
			for i in range(len(cboxFeatureList)):
				cdFeatures.append(0)
			freqOfFeatures = []
			for i in range(4):
				freqOfFeatures.append(0)
		#H BOX IS HERE
			[hMotifs,hbMotifs,hisFlipped,houtString] = MotifMatch(hboxre,seq,.7,.3,header,False,matchDebug)
			freqOfFeatures[0] = len(hMotifs)
			if len(hMotifs) > 0:
				seq = hMotifs[0].string
				for match in hMotifs:
					motif = match.group()
					hacaFeatures[hboxFeatureList.index(motif)] = 1 #THE FEATURE MATRIX IS BUILT HERE!!!
					if motif in hMotifDict:
						hMotifDict[motif] += 1
					else:
						hMotifDict[motif] = 1
		#ACA TAIL IS HERE
			[acaMotifs,acabMotifs,acaisFlipped,acaoutString] = MotifMatch(acare,seq,1,.9,header,True,matchDebug)
			freqOfFeatures[1] = len(acaMotifs)
		#C box IS HERE
			[cMotifs,hbMotifs,hisFlipped,coutString] = MotifMatch(cboxre,seq,1,0,header,False,matchDebug)
			freqOfFeatures[2] = len(cMotifs)
			if len(cMotifs) > 0:
				seq = cMotifs[0].string
				for match in cMotifs:
					motif = match.group()
					cdFeatures[cboxFeatureList.index(motif)] = 1 #THE FEATURE MATRIX IS BUILT HERE!!!
					if motif in cMotifDict:
						cMotifDict[motif] += 1
					else:
						cMotifDict[motif] = 1
		#D box IS HERE
			[dMotifs,dbMotifs,dIsFlipped,dOutString] = MotifMatch(dboxre,seq,1,0,header,True,matchDebug)
			freqOfFeatures[3] = len(dMotifs)
		#Adding all feature vectors to their respective lists
			fList.append(freqOfFeatures+hacaFeatures+cdFeatures)
			freqOfFeaturesList.append(freqOfFeatures)
	if debug >=2:
		csortedList = sorted(cMotifDict, key=cMotifDict.get)	
		print "cbox motif list:"
		for motif in csortedList[::-1]:
			print motif, ":", cMotifDict[motif]
		hsortedList = sorted(hMotifDict, key=hMotifDict.get)
		print "hbox motif list:"
		for motif in hsortedList[::-1]:
			print motif, ":", hMotifDict[motif]
	if debug >= 1:
		print "nothing to say!"
	return fList,freqOfFeaturesList,hMotifDict,cMotifDict
	
	
def featureSelection(fastaPos,fastaNeg,nameOut,debug):
	posData,posFreq,posHMD,negCMD = snoMotifFind(fastaPos,1,0)
	negData,negFreq,negHMD,posCMD = snoMotifFind(fastaNeg,1,0)
	totalData = posData+negData
	if debug >= 2:
		print "pos set:\n", freqTableToString(posFreq,True)
		print "neg set:\n", freqTableToString(negFreq,True)
		print "key:\n1000 = hbox\n0100 = aca tail\n0010 = cbox\n0001 = dbox"
		print "HACA motifs:\n" , pnDictCompare(posHMD,negHMD)
		print "CD motifs:\n" , pnDictCompare(posCMD,negCMD)
		print ("%.2f" % (float(100*nNone)/len(fList)))
	t = []
	for i in range(len(posData)):
		t.append(1)
	for i in range(len(negData)):
		t.append(0)
	#generating strings for an m-file
	fOut = "\tX=[\n"
	nRow = 0
	for row in totalData:
		nItem = 0
		nRow+=1
		fOut += "\t\t"
		for item in row:
			fOut += str(item)
			nItem += 1
			if nItem<len(row):
				fOut += ","
			else:
				if nRow<len(totalData):
					fOut+= ";\n"
				else:
					fOut+= "\n\t]"
	nItem = 0
	tOut = "\tt=[\n\t\t"
	counter = 0;
	for item in t:
		counter += 1
		nItem += 1
		tOut += str(item)
		if nItem<len(t):
			tOut += ";"
			if (counter%50)==0:
				tOut += "\n\t\t"
		else:
			tOut += "\n\t]"
	if debug >=1:
		print tOut
		print fOut
	mFileHeader = "function X,t = builtFeature()\n"
	mFileEnd = "end"
	mFile = open(nameOut, 'w')
	mFile.write(mFileHeader)
	mFile.write(fOut)
	mFile.write(tOut)
	mFile.write(mFileEnd)
	mFile.close()
	return totalData,t
featureSelection(sys.argv[1],sys.argv[2],'temp',1)


