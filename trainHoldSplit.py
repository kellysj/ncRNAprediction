"""
A set of functions to split fastas into training and holdout sets
"""

import sys
import re
import random


"""
A function to read in a fasta file and return a list of headers and seqs with corresponding indicies
fasta = file name to read in
isRNA = a boolean for converting reads to RNA if needed
debug = prints debug info after running
headerList = a list of headers from the fasta
seqList = a list of seqs from the fasta
"""
def fastaRead(fasta,isRNA,debug):
	headerre = re.compile(r'>(.*)')
	seqre = re.compile(r'^[UNATGC]+')
	headerList = []
	seqList = []
	seq = ""
	for line in open(fasta):
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			headerList.append(headerMatch.group(0))
			if len(seq)>0:
				seqList.append(seq)
				seq = ""
		if seqMatch:
			seqToAdd = seqMatch.group()
			if isRNA:
				seqToAdd = seqToAdd.replace("T","U")
			seq += seqToAdd
	seqList.append(seq)#adding the last seq

	if debug:
		print "headerlist range is: " , len(headerList)
		print "seqList range is: " , len(seqList)
		for i in range(len(seqList)):			
			print fasta,":",i,":",len(headerList), ":header: ", headerList[i]
			print fasta,":",i,":",len(seqList), ":seq: " , seqList[i]
		print "Header Size:", len(headerList)
		print "Seq Size:", len(seqList)
	return headerList,seqList
"""
A function that writes a set of header and seq lists to a file
header = the header list to use
seq = the seq list to use
fileName = the name of the file to write to
"""
def fastaWrite(header,seq,fileName):
	if len(header)==len(seq):
		file = open(fileName, 'w')
		for i in range(len(header)):
			file.write(header[i] + "\n" + seq[i] + "\n")
		file.close()
	else:
		print "Quitting: sequence number not equal to header number"
"""
Splits a given dataset into a holdout and training set
headerTraining = training header list
seqTraining = training seq list
headerHoldout = hold out header list
seqHoldout = hold out seq list
"""
def randomSelect(percHoldOut,head,seq,isRNA,debug):
	headerTraining = []
	seqTraining = []
	numberOfSeqs = int((1-percHoldOut)*len(seq))
	print "train seq n for random select is:" + str(numberOfSeqs) + " training and " + str(len(seq)-numberOfSeqs) +  " out of a total of " + str(len(seq))
	for i in range(numberOfSeqs):
		headerTraining.append(head.pop(int(random.random()*len(head))))
		seqTraining.append(seq.pop(int(random.random()*len(seq))))
	headerHoldout = head
	seqHoldout = seq
	if debug:
		for i in range(len(headerTraining)):
			print "training:",headerTraining[i]
			print seqTraining[i]
		for i in range(len(headerHoldout)):
			print "holdout:",headerHoldout[i]
			print seqHoldout[i]
	return headerTraining,seqTraining,headerHoldout,seqHoldout
"""
writes the training and holdout lists to a file from a given fasta
percHoldOut = the percentage of seqs to hold for testing
fasta = the fasta to draw data from
prefixOut = the prefix for resulting split fastas
"""
def splitDataWrite(percHoldOut,fasta,prefixOut):
	holdNameOut = prefixOut + "_holdout.fa"
	trainNameOut = prefixOut + "_train.fa"
	head,seq = fastaRead(fasta)
	trainHead,trainSeq,holdHead,holdSeq = randomSelect(percHoldOut,fasta,True)
	fastaWrite(trainHead,trainSeq,trainNameOut)
	fastaWrite(holdHead,holdSeq,holdNameOut)