import urllib2
import re
import xml.etree.ElementTree as ET
import random
import sys
# Download protein FASTA records linked to abstracts published 
# in 2009 that are indexed in MeSH for both asthma and 
# leukotrienes.
giQueryTest = r"29565438,29565441,29565450"

db1 = 'pubmed'
db2 = 'nuccore'
linkname = 'pubmed_gene'
testquery = 'snoRNA'
testGI = "21614549"
cdSearch = r'(C/D[All+Fields]+AND+snoRNA[All+Fields])+AND+(50:200[SLEN])'
hacaSearch = r'(ACA[All+Fields]+AND+snoRNA[All+Fields])+AND+(50:200[SLEN])'
randomSearch = r'((50:200[SLEN])+NOT+snoRNA[All+Fields]+NOT+ncRNA[All+Fields])'
ncRandSearch = r'(ncRNA[All+Fields]+AND+(50:200[SLEN])+NOT+snoRNA[All+Fields])'
batchSize = 250
def queryDBbykeyword(query):
	#assemble the esearch URL
	base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
	esearchurl = base + "esearch.fcgi?db=" + db2 + "&term=" + query + "&usehistory=y"
	#post the esearch URL
	#print "eSearch URL: " + esearchurl
	html = urllib2.urlopen(esearchurl).read()
	web1 = re.search(r'<WebEnv>(\S+)<\/WebEnv>',html).group(1)
	key1 = re.search(r'<QueryKey>(\d+)<\/QueryKey>',html).group(1)
	count = int(re.search(r'<Count>(\d+)<\/Count>',html).group(1))
	#efetching:
	#fastaList = []
	start = 0
	while (start < count):
		cond = (start > count)
		efetchurl = base + "efetch.fcgi?db=" + db2 + "&query_key=" + key1 + "&WebEnv=" + web1 + "&retstart=" + str(start) + "&retmax=" + str(batchSize) +"&rettype=fasta&retmode=xml"
		data = urllib2.urlopen(efetchurl).read()
		batchRoot = ET.fromstring(data)
		#print data
		for record in batchRoot.iter('TSeq'):
			
			gi = record.find('TSeq_gi').text
			seq = record.find('TSeq_sequence').text
			fasta = ">" + gi + "\n" + seq
			#fastaList.append(fasta)
			print fasta
		start += batchSize
	#print len(fastaList)
	#return fastaList
def queryRandomDownload(query,size,fileName):
	size = int(size)
	#assemble the esearch URL
	base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
	esearchurl = base + "esearch.fcgi?db=" + db2 + "&term=" + query + "&usehistory=y"
	#post the esearch URL
	print "eSearch URL: " + esearchurl
	html = urllib2.urlopen(esearchurl).read()
	web1 = re.search(r'<WebEnv>(\S+)<\/WebEnv>',html).group(1)
	key1 = re.search(r'<QueryKey>(\d+)<\/QueryKey>',html).group(1)
	count = int(re.search(r'<Count>(\d+)<\/Count>',html).group(1))
	#efetching:
	fastaList = []
	loadedIndexL = {}
	start = 0
	loadedIndexL[0] = None
	while (len(fastaList) <= size):		
		while start in loadedIndexL:
			start = int(float(count)*(random.random()))
		loadedIndexL[start] = None
		#print "start i is:", start ,"\ncount is:", count
		efetchurl = base + "efetch.fcgi?db=" + db2 + "&query_key=" + key1 + "&WebEnv=" + web1 + "&retstart=" + str(start) + "&retmax=" + "1" +"&rettype=fasta&retmode=xml"
		data = urllib2.urlopen(efetchurl).read()
		batchRoot = ET.fromstring(data)
		#print data
		for record in batchRoot.iter('TSeq'):			
			gi = record.find('TSeq_gi').text
			seq = record.find('TSeq_sequence').text
			fasta = ">" + gi + "\n" + seq
			if (re.search(r'^[N]+[N]$', seq))==None and (len(fastaList) <= size):
				fastaList.append(fasta)
				print fasta , "\nList Size" , len(fastaList), ":", size , ":" , len(fastaList) <= size 
			#else:
			#	print "piece of crap seq"
			#	print "List Size" , len(fastaList)
	print "all done"
	outFile = file(fileName, 'w')
	n = 0
	for fasta in fastaList:
		outFile.write(fasta)
		if fastaList.index(fasta) < len(fastaList):
			outFile.write("\n")
	outFile.close()
	
	#print len(fastaList)
	#return fastaList
	
def queryDBbyGI(id):
	base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
	efetchurl = base + "efetch.fcgi?db=" + db2 + "&id=" + id + "&rettype=fasta&retmode=xml"
	print "efetchurl: " + efetchurl
	output = urllib2.urlopen(efetchurl)
	data = output.read()
	seq = re.search(r'<TSeq_sequence>(\S+)<\/TSeq_sequence>',data).group(1)
	gi = re.search(r'<TSeq_gi>(\d+)<\/TSeq_gi>',data).group(1)
	fasta = ">" + gi + "\n" + seq + "\n"
	return fasta
	

queryRandomDownload(randomSearch,sys.argv[1],sys.argv[2])
#queryDB(testquery)
#print(queryDBbyGI(testGI))
#queryDBbykeyword(hacaSearch)
