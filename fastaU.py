import sys
import re

"""
A function to read in a fasta file and return a list of headers and seqs with corresponding indicies
fasta = file name to read in
isRNA = a boolean for converting reads to RNA if needed
debug = prints debug info after running
headerList = a list of headers from the fasta
seqList = a list of seqs from the fasta
"""
def read(fasta,isRNA,debug):
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
def write(header,seq,fileName):
	if len(header)==len(seq):
		file = open(fileName, 'w')
		for i in range(len(header)):
			file.write(header[i] + "\n" + seq[i] + "\n")
		file.close()
	else:
		print "Quitting: sequence number not equal to header number"