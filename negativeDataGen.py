import sys
import re
import random
"""
Functions for randomly generating data from 2 fastas and optionally adding random data. For use with the feature finding part of the project
"""
maxL = 160	#the max length of the random data
v = 80		#the variation of seqs less than the max length

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
	for line in open(fasta):
		headerMatch = re.search(headerre, str(line))
		seqMatch = re.search(seqre, str(line).upper())
		if headerMatch:
			headerList.append(headerMatch.group(0))
		if seqMatch:
			seq = seqMatch.group()
			if isRNA:
				seq = seq.replace("T","U")
			seqList.append(seq)

	if debug:
		for i in range(len(seqList)):
			print headerList[i]
			print seqList[i]
		print "Header Size:", len(headerList)
		print "Seq Size:", len(seqList)
	return headerList,seqList
	
"""
A function for generating synthetic data
maxLength = the max length for the random sequence
variation = the variation between sequences
isRNA = output is RNA instead of DNA
Seq = the string of random sequence from the given parameters
"""
def synthSeqGen(maxLength,variation,isRNA):
	nt = ""
	Seq = ""
	length = int(maxLength-(variation*random.random()))
	
	for n in range(length):
		i = 4*random.random()
		if 1>i>=0:
			nt = "A"
		if 2>i>=1:
			if isRNA:
				nt = "U"
			else:
				nt = "T"
		if 3>i>=2:
			nt = "G"
		if 4>i>=3:
			nt = "C"
		Seq += nt
	return Seq

"""
A function to randomly select sequences from input lists and/or generate random data
numberOfSeqs = number of sequences to output as a list
fasta1 = file name of the first fasta file
r1 = ratio of the first fasta sequences to add to the compilation
fasta2 = file name of the second fasta file
r2 = ratio of the second fasta sequences to add to the compilation
useSynth = to use or not use synthetic sequences
rS = the ratio of synthetic sequences
"""
def compileData(numberOfSeqs,fasta1,r1,fasta2,r2,useSynth,rS,isRNA,debug):
	header = []
	seq = []
	totalR = r1+r2
	if useSynth:
		totalR += rS
	nFasta1 = r1*(numberOfSeqs/totalR)
	nFasta2 = r2*(numberOfSeqs/totalR)
	nSynth = numberOfSeqs-nFasta1-nFasta2
	head1,seq1 = fastaRead(fasta1,isRNA,False)
	head2,seq2 = fastaRead(fasta2,isRNA,False)
	for i in range(nFasta1):
		header.append(head1.pop(int(random.random()*len(head1))))
		seq.append(seq1.pop(int(random.random()*len(seq1))))
	for i in range(nFasta2):
		header.append(head2.pop(int(random.random()*len(head2))))
		seq.append(seq2.pop(int(random.random()*len(seq2))))
	for i in range(nSynth):
		synHead = ">synth" + str(i)
		header.append(synHead)
		seq.append(synthSeqGen(maxL,v,True))
	if debug:
		for i in range(len(seq)):
			print header[i]
			print seq[i]
	return header,seq
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
	