"""
snoPatternSplit
HBoxes:
	ANANNA - flanked by 2 large hairpin formations
C/D:
boxes C (RUGAUGA, R=purine) and D (CUGA)
"""
import sys
import re

"""
A function to write out a table of kmers as a key for frequencies of kmers
"""
def generateKmersRec(length,seq,listIn):
	nucList1 = ["A","U","G","C"]
	if length == 0:
		listIn.append(seq)
		return listIn
	for n1 in nucList1:
		generateKmersRec(length-1,(seq+n1),listIn)

nmerTotalList = []
print "starting kmerlist generation..."
for i in range(1,6):
	tempL = []
	generateKmersRec(i,"",tempL)
	nmerTotalList.append(tempL)
print "generation complete."
	
#feature nMer lists for motifs 
hboxFeatureList = ["AAAAAA","AAAAUA","AAAAGA","AAAACA","AAAUAA","AAAUUA","AAAUGA","AAAUCA","AAAGAA","AAAGUA","AAAGGA","AAAGCA","AAACAA","AAACUA","AAACGA","AAACCA","AUAAAA","AUAAUA","AUAAGA","AUAACA","AUAUAA","AUAUUA","AUAUGA","AUAUCA","AUAGAA","AUAGUA","AUAGGA","AUAGCA","AUACAA","AUACUA","AUACGA","AUACCA","AGAAAA","AGAAUA","AGAAGA","AGAACA","AGAUAA","AGAUUA","AGAUGA","AGAUCA","AGAGAA","AGAGUA","AGAGGA","AGAGCA","AGACAA","AGACUA","AGACGA","AGACCA","ACAAAA","ACAAUA","ACAAGA","ACAACA","ACAUAA","ACAUUA","ACAUGA","ACAUCA","ACAGAA","ACAGUA","ACAGGA","ACAGCA","ACACAA","ACACUA","ACACGA","ACACCA"]
cboxFeatureList = ["AUGAUGA","AUGAAGA","AGGAUGA","AGGAAGA","AUGAUGU","AUGAAGU","AGGAUGU","AGGAAGU","AUGAUGG","AUGAAGG","AGGAUGG","AGGAAGG","AUGAUGC","AUGAAGC","AGGAUGC","AGGAAGC","UUGAUGA","UUGAAGA","UGGAUGA","UGGAAGA","UUGAUGU","UUGAAGU","UGGAUGU","UGGAAGU","UUGAUGG","UUGAAGG","UGGAUGG","UGGAAGG","UUGAUGC","UUGAAGC","UGGAUGC","UGGAAGC","GUGAUGA","GUGAAGA","GGGAUGA","GGGAAGA","GUGAUGU","GUGAAGU","GGGAUGU","GGGAAGU","GUGAUGG","GUGAAGG","GGGAUGG","GGGAAGG","GUGAUGC","GUGAAGC","GGGAUGC","GGGAAGC","CUGAUGA","CUGAAGA","CGGAUGA","CGGAAGA","CUGAUGU","CUGAAGU","CGGAUGU","CGGAAGU","CUGAUGG","CUGAAGG","CGGAUGG","CGGAAGG","CUGAUGC","CUGAAGC","CGGAUGC","CGGAAGC"]


selectedFeatures1 = ['CUGUG', 'CAUUU', 'UUUUU', 'GGCUG', 'ACAUU', 'UGUGG', 'GCAGC', 'UGGCU', 'GCCUG', 'GUGGC', 'AAAAA', 'UUCCU', 'CUGCC', 'GCUGC', 'UGCCU', 'UGUUU', 'CAGUG', 'UGCAA', 'GCUGU', 'CACAG', 'UUGUU', 'UUGUG', 'UGUUG', 'UUAAA', 'GCUUG', 'UGUGC', 'GCCUC', 'AAAGC', 'UGUGU', 'UUUAU', 'UGGUU', 'UUGCU', 'GCCAG', 'GUGCU', 'CUGCA', 'UACAU', 'UUUCU', 'AAGCA', 'GGCCU', 'UCAUU', 'AGACA', 'UGGCC', 'CCUUU', 'CUGUU', 'CUUGU', 'UUUUC', 'CAAUU', 'UGCUU', 'AUGGG', 'CCUUG', 'ACAGU', 'UUUGG', 'AGCAA', 'GUGUG', 'CUGGC', 'UUGAA', 'CCUGU', 'ACAAU', 'UUUGA', 'UCCAU', 'CAUUG', 'CAAAC', 'UGCCC', 'CCAUU', 'UUUCA', 'UUUGC', 'GCACA', 'GUGUU', 'AGCUG', 'UUCCA', 'CAUGG', 'AAUGG', 'CUCUG', 'UCCUG', 'AACAU', 'CUGGG', 'AAUUG', 'AAAAG', 'UUGGA', 'UAAAU', 'CCUCA', 'GCAAA', 'CAAAG', 'UCUCU', 'AUUUG', 'UGGGU', 'GUGAA', 'UGUCU', 'UGAAG', 'CUGGU', 'GGCCC', 'UAAUU', 'UGUGA', 'GAGCA', 'GACAA', 'AAAAC', 'AGCCU', 'ACAGC', 'AGCAG', 'UUCUU', 'CAUUC', 'AUGCA', 'CUUGC', 'UUGCC', 'GAAAG', 'GCCUU', 'UGGUA', 'AAUUA', 'ACUGU', 'UGGGC', 'CAGUA', 'AGAAA', 'UUACA', 'UGCUG', 'CUUCC', 'CUUUG', 'UCUUU', 'CCAUG', 'CCACA', 'UGAUA', 'GCUAU', 'UAUCC', 'UGCUA', 'AUUAA', 'AUUAU', 'GCCCU', 'UUCUG', 'CUUUC', 'UAUAU', 'CUCUU', 'CUCAU', 'CCAGC', 'GCCCC', 'UGGUG', 'AUUGU', 'UGGGA', 'GACAU', 'AUUCA', 'CCCAU', 'ACAUG', 'AGCAC', 'GAAAU', 'CACAU', 'CCCAG', 'AUUGA', 'GACAG', 'CCAGA', 'CCUCU', 'GGAAA', 'AGGCU', 'CUACA', 'UUGAU', 'UACAA', 'CUGAU', 'AUGUG', 'GGAGA', 'CAUCU', 'GUUGC', 'GAAUG', 'UGGGG', 'UUAUA', 'AACCC', 'AGUCU', 'CACUC', 'AAAGU', 'CUGAC', 'AUUUA', 'GUCUG', 'AAUAA', 'CAGCG', 'GUGGU', 'AGUGU', 'ACACU', 'GCUCU', 'GGUCU', 'AGAGA', 'UCCCA', 'UCAAU', 'AAGUG', 'GAAAA', 'CAAAU', 'UUCAU', 'AACAA', 'UGGUC', 'CAGGC', 'CCUCC', 'AGUGG', 'AUGAG', 'GGGCC', 'CUCAG', 'AUGGC', 'GUUUC', 'UAACU', 'UCUUG', 'UGCAC', 'UUGGC', 'CAUGU', 'AUCUG', 'UCACA', 'AGUGA', 'AUGAA', 'GUCUC', 'UGUAU', 'GGAGG', 'CUAUA', 'CUAUG', 'AGAUG', 'CUCCA', 'CCCCG', 'CCGUG', 'AAGAA', 'GAUAU', 'GUUGU', 'ACUGC', 'CACAA', 'AAUGC', 'CACCU', 'UACUG', 'AUAUA', 'UUUAC', 'GUUGG', 'ACUUG', 'CUCCU', 'UUCCC', 'CAUGC', 'UUAUC', 'GCGGC', 'CUGUA', 'GACUG', 'CAUUA', 'GGCUA', 'AAGGG', 'AGUAA', 'AGAUU', 'AGAGG', 'GGCAC', 'UUGUC', 'UAUGU', 'UAUGG', 'CGCCU', 'CCAGG', 'AAAGA', 'UGGAC', 'GCAUG', 'CUGAG', 'CAACC', 'UAACA', 'CCAAG', 'GGUCA', 'UGAUU', 'UCCAA', 'ACAUA', 'CUAUU', 'AUCAA', 'CAAUA', 'GAGAU', 'UAUAG', 'UCUUA', 'CAGGG', 'CUAAA', 'UAUUA', 'UGAGA', 'UCCAG', 'UCUAU', 'AUGAU', 'CUAAU', 'GCGCU', 'AUACA', 'CGGCU', 'GUUUA', 'GGUAG', 'UAAAG', 'CUCUA', 'ACAGG', 'AUAGU', 'AUAUU', 'UUAAG', 'CCAAU', 'GCCGU', 'AGGAG', 'CAUAA', 'GUCAU', 'CAAGG', 'GUACA', 'AACUU', 'UGACU', 'GAGAG', 'CACCA', 'CGCUG', 'GUCAC', 'GCGUG', 'GCAAU', 'UCCCU', 'CAGAA', 'UGUUA', 'AUAGC', 'UUAAU', 'CUUCU', 'CUCUC', 'CAUAG', 'AUCCA', 'AUCCC', 'AAUUC', 'GUGAC', 'GGAUA', 'UGACC', 'AACCA', 'UGAUC', 'GACUU', 'AAGCU', 'UAUCA', 'UAGAG', 'GAUGC', 'CCUUC', 'UAGUC', 'UCAAG', 'UAACC', 'GGGGG', 'AUAAG', 'GUCUA', 'CAAGU', 'GACAC', 'GUAUA', 'UGAGG', 'CGUGU', 'CUUAA', 'UUCAC', 'AUGAC', 'GGGAA', 'GCAGA', 'CAAUC', 'UCAGC', 'UAAGA', 'UACAG', 'UAGAU', 'UUGCG', 'CGUGC', 'UAUGC', 'GUCAG', 'GACCU', 'UCAGG', 'AGUAU', 'AUGUA', 'AGGAA', 'AAUCC', 'ACUGG', 'CAGGA', 'UACCC', 'GUAGA', 'GUAGC', 'GUAAU', 'CCGCC', 'AGAAG', 'CGGCC', 'AGCCC', 'GCGCC', 'AUCUU', 'ACCAG', 'CUUAC', 'CUCCC', 'CUAAC', 'GGCCG', 'CGCUU', 'AUCAU', 'UGCGC', 'CCUAC', 'CGGGC', 'GAGAA', 'UUAAC', 'UACAC', 'AUGUC', 'GCCUA', 'AAUCA', 'CCAUC', 'CGUUU', 'ACUCU', 'ACUCC', 'UCACU', 'UCAUC', 'GCUAA', 'GGGAU', 'CAUCC', 'GAUCU', 'GGGUU', 'CAACU', 'GCAUC', 'UCAGA', 'UCAUA', 'UAGUG', 'GGGGA', 'GAAUU', 'AACUC', 'GUAUG', 'GGAAG', 'UGUAG', 'GGCGC', 'AAGGC', 'CCCCA', 'GCAGG', 'AUAGA', 'AGACU', 'AGAUC', 'UUCUA', 'UCUCC', 'GGUAU', 'ACUAA', 'UGUCC', 'AUGUU', 'CAUCA', 'CAUAU', 'GUUGA', 'CCUCG', 'GUGUA', 'GUAGU', 'GUUAC', 'GUUAA', 'UAUGA', 'AUUCU', 'CACCC', 'AGGCA', 'UGCGG', 'ACACC', 'CCUAU', 'ACUAU', 'UAAGC', 'AAUCG', 'GUGAG', 'GAGGU', 'ACCAA', 'GGCCA', 'CGACA', 'ACGCU', 'CCCGU', 'CCAAC', 'GGACC', 'GCUUA', 'UAAUA', 'UAUAC', 'GAGUA', 'AGGAU', 'CCGUU', 'GGAUU', 'GAUAC', 'GAGGA', 'UCGGU', 'ACCAC', 'CCCAC', 'GAUUC', 'GUCGC', 'AGAUA', 'ACCCG', 'GGAGU', 'GGAGC', 'AAGUU', 'CCAUA', 'GAUAG', 'GUACU', 'AGCGA', 'CGCUC', 'ACACG', 'CGCCG', 'ACGCA', 'AGGUG', 'GGUAC', 'CGGUC', 'CGCAC', 'GAAGG', 'CAGGU', 'AUCGU', 'CCACC', 'GGCGU', 'UACUU', 'AGGGU', 'AGGGG', 'UCCCC', 'GUGGA', 'UCCGC', 'CUUCG', 'GUCCU', 'UAAGU', 'CAUAC', 'AGAAC', 'GGAAC', 'CACGC', 'AGGCG', 'AGUUC', 'GGUUA', 'GGUGG', 'ACUAG', 'CUCGA', 'UAGGC', 'UCGCC', 'CGUUA', 'GUAUC', 'GCGCA', 'UGUCG', 'GCGUC', 'UACCU', 'GGAAU', 'AGUUA', 'AGGUU', 'UCGUU', 'AGGAC', 'GGGUC', 'UAGCC', 'CCGCA', 'GCCAU', 'UGCCG', 'UUCCG', 'GAAUC', 'GAAGC', 'GGAUG', 'CCACG', 'CGUUC', 'CUAUC', 'UCUAG', 'GCGGU', 'UACGA', 'UACGU', 'UUAGU', 'AAACG', 'CCUUA', 'CGCAU', 'GGGGU', 'CGAAG', 'CGCAA', 'GUAGG', 'AACCG', 'AGUCG', 'AGUCC', 'GGUCC', 'GAUCA', 'CUCGC', 'UAGGG', 'CGGCA', 'CGGGA', 'GACUC', 'ACGUA', 'CGUAG', 'ACGGC', 'CGGGG', 'AUACG', 'AUCAG', 'GUAAG', 'AGGUA', 'CGAUU', 'CCCGA', 'AGACC', 'GCGAU', 'GUACC', 'UCCCG', 'ACGAU', 'ACGAG', 'GGAUC', 'CGUUG', 'AUCGC', 'UUAGC', 'ACGGU', 'ACCGG', 'AUAGG', 'CCUAG', 'GUCGU', 'GCCCG', 'CUAGG', 'CGAUA', 'UCGGA', 'UAGGU', 'AACGU', 'CUCGU', 'UACCG', 'GAACG', 'CGCGC', 'CGUCG', 'CACCG', 'GCGCG', 'CGACU', 'GUCCC', 'CCGUC', 'ACCGA', 'CCGGU', 'CGCUA', 'CGUCU', 'CGAGG', 'UACUC', 'CUUAG', 'UCCGG', 'GGUAA', 'GUUCG', 'CAACG', 'AACGG', 'UGACG', 'ACUCG', 'CGCGG', 'GCGGA', 'UUCGA', 'CCGCU', 'CUACG', 'GACCC', 'CGGAC', 'CUAGC', 'CGUAC', 'CUACU', 'CGGAA', 'UAUCG', 'GAUCG', 'GUUAG', 'CCGAG', 'GUCGG', 'ACUAC', 'ACGAA', 'AACGA', 'ACGGG', 'UCGUC', 'UCGAC', 'AGACG', 'ACGAC', 'CCGGA', 'CGAUC', 'GAACC', 'UCGGG', 'CGGGU', 'CGGUA', 'UAACG', 'ACCGU', 'CGAGA', 'UCGCG', 'CGUCC', 'ACGUC', 'CGACG', 'GACGA', 'GACCG', 'GUCCG', 'UACGG', 'ACGCG', 'GACGU', 'CGACC']

selectedFeatures2 = ['CUGUG', 'CAUUU', 'UUUUU', 'ACAUU', 'UGUGG', 'GCCUG', 'GUGGC', 'UUCCU', 'UGCCU', 'UGUUU', 'UGCAA', 'GCUGU', 'CACAG', 'UUGUG', 'UGUUG', 'GCUUG', 'UGUGC', 'GCCUC', 'UGUGU', 'UUUAU', 'UUGCU', 'GCCAG', 'GUGCU', 'UACAU', 'AAGCA', 'GGCCU', 'UCAUU', 'AGACA', 'UGGCC', 'CUGUU', 'CUUGU', 'CAAUU', 'AUGGG', 'CCUUG', 'ACAGU', 'GUGUG', 'ACAAU', 'UCCAU', 'CAUUG', 'UGCCC', 'CCAUU', 'GCACA', 'GUGUU', 'AACAU', 'AAUUG', 'UUGGA', 'UGGGU', 'GUGAA', 'UGUCU', 'GGCCC', 'UAAUU', 'UGUGA', 'GACAA', 'ACAGC', 'UUCUU', 'CAUUC', 'AUGCA', 'CUUGC', 'UUGCC', 'GAAAG', 'UGGUA', 'AAUUA', 'ACUGU', 'CAGUA', 'UUACA', 'UGCUG', 'CUUUG', 'UCUUU', 'CCAUG', 'CCACA', 'UGAUA', 'GCUAU', 'UAUCC', 'UGCUA', 'AUUAA', 'AUUAU', 'GCCCU', 'CUUUC', 'UAUAU', 'CUCUU', 'CUCAU', 'GCCCC', 'AUUGU', 'CCCAU', 'ACAUG', 'CACAU', 'AUUGA', 'GACAG', 'CCAGA', 'AGGCU', 'CUACA', 'UACAA', 'AUGUG', 'GUUGC', 'UGGGG', 'AACCC', 'AGUCU', 'CACUC', 'AAAGU', 'GUCUG', 'AGUGU', 'ACACU', 'GGUCU', 'AGAGA', 'AAGUG', 'UUCAU', 'UGGUC', 'CAGGC', 'AGUGG', 'GUUUC', 'UAACU', 'CAUGU', 'UCACA', 'GUCUC', 'UGUAU', 'GGAGG', 'CUAUA', 'CUAUG', 'CCCCG', 'CCGUG', 'GUUGU', 'AAUGC', 'CACCU', 'UACUG', 'UUAUC', 'GCGGC', 'CUGUA', 'CAUUA', 'GGCUA', 'AGUAA', 'UUGUC', 'UAUGG', 'CGCCU', 'CCAGG', 'AAAGA', 'UGGAC', 'GCAUG', 'UAACA', 'GGUCA', 'CUAUU', 'GAGAU', 'UAUAG', 'UCUUA', 'UAUUA', 'CUAAU', 'GCGCU', 'AUACA', 'CGGCU', 'GUUUA', 'GGUAG', 'AUAGU', 'UUAAG', 'CCAAU', 'GCCGU', 'CAUAA', 'GUCAU', 'GUACA', 'UGACU', 'GUCAC', 'GCGUG', 'AUAGC', 'CAUAG', 'GUGAC', 'UGACC', 'GACUU', 'AAGCU', 'UAUCA', 'UAGAG', 'UAACC', 'GGGGG', 'AUAAG', 'GUCUA', 'GUAUA', 'CGUGU', 'UUCAC', 'GGGAA', 'CAAUC', 'UAAGA', 'UACAG', 'UUGCG', 'CGUGC', 'GACCU', 'AUGUA', 'AGGAA', 'CAGGA', 'UACCC', 'GUAGA', 'GUAGC', 'GUAAU', 'AGAAG', 'GCGCC', 'ACCAG', 'CUUAC', 'CUAAC', 'GGCCG', 'CCUAC', 'CGGGC', 'UUAAC', 'UACAC', 'GCCUA', 'CCAUC', 'UCACU', 'GGGAU', 'CAUCC', 'GAUCU', 'UCAGA', 'UCAUA', 'UAGUG', 'GGGGA', 'UGUAG', 'GGCGC', 'GCAGG', 'AGAUC', 'CAUCA', 'CCUCG', 'GUAGU', 'ACUAU', 'UAAGC', 'GUGAG', 'ACCAA', 'ACGCU', 'CCCGU', 'UAAUA', 'GAGUA', 'GAUAC', 'GAGGA', 'GUCGC', 'AGAUA', 'ACCCG', 'CCAUA', 'GAUAG', 'CGCUC', 'CGCCG', 'ACGCA', 'AGGUG', 'CAGGU', 'AUCGU', 'AGGGU', 'AGGGG', 'UCCCC', 'UCCGC', 'GUCCU', 'CAUAC', 'GGAAC', 'AGGCG', 'GGUGG', 'UAGGC', 'UCGCC', 'GUAUC', 'UACCU', 'GGAAU', 'UCGUU', 'AGGAC', 'GGGUC', 'CCGCA', 'GCCAU', 'UUCCG', 'GAAGC', 'GGAUG', 'UACGA', 'UACGU', 'CGCAU', 'GGGGU', 'GGUCC', 'CUCGC', 'UAGGG', 'CGGGA', 'CGGGG', 'AUACG', 'AUCAG', 'AGGUA', 'CGAUU', 'AGACC', 'GUACC', 'AUCGC', 'CCUAG', 'GUCGU', 'GCCCG', 'CUAGG', 'CGUCG', 'GUCCC', 'CCGUC', 'ACCGA', 'CGCUA', 'CGUCU', 'UACUC', 'GGUAA', 'CAACG', 'AACGG', 'CGCGG', 'UUCGA', 'CCGCU', 'GACCC', 'CGGAC', 'CUAGC', 'CUACU', 'CGGAA', 'UAUCG', 'GUUAG', 'CCGAG', 'GUCGG', 'ACUAC', 'ACGAA', 'AACGA', 'UCGUC', 'UCGAC', 'AGACG', 'ACGAC', 'GAACC', 'UCGGG', 'CGGGU', 'CGGUA', 'UAACG', 'ACCGU', 'CGAGA', 'UCGCG', 'CGUCC', 'ACGUC', 'CGACG', 'GACGA', 'GACCG', 'GUCCG', 'UACGG', 'ACGCG', 'GACGU', 'CGACC']


selectedFeatures3 = ['CUGUG', 'CAUUU', 'ACAUU', 'UGUGG', 'GCCUG', 'GUGGC', 'UUGUG', 'UGUUG', 'UGUGC', 'UUGCU', 'GUGCU', 'UACAU', 'GGCCU', 'UCAUU', 'AGACA', 'UGGCC', 'CUGUU', 'CUUGU', 'CAAUU', 'AUGGG', 'CCUUG', 'ACAGU', 'GUGUG', 'ACAAU', 'UCCAU', 'CAUUG', 'CCAUU', 'GUGUU', 'AAUUG', 'UUGGA', 'UGGGU', 'GUGAA', 'UGUCU', 'GGCCC', 'UGUGA', 'CAUUC', 'AUGCA', 'CUUGC', 'UUGCC', 'UGGUA', 'AAUUA', 'ACUGU', 'CAGUA', 'UUACA', 'UGAUA', 'GCUAU', 'UAUCC', 'UGCUA', 'AUUAA', 'AUUAU', 'CUUUC', 'GCCCC', 'CACAU', 'CUACA', 'UACAA', 'AUGUG', 'AGUCU', 'AGUGU', 'AAGUG', 'UUCAU', 'GUUUC', 'UAACU', 'CAUGU', 'GUCUC', 'CUAUA', 'CUAUG', 'CCGUG', 'CACCU', 'UUAUC', 'CAUUA', 'GGCUA', 'AGUAA', 'UAUGG', 'CGCCU', 'UGGAC', 'GCAUG', 'UAACA', 'GGUCA', 'CUAUU', 'UAUAG', 'UCUUA', 'CUAAU', 'GUUUA', 'GGUAG', 'AUAGU', 'UUAAG', 'GCCGU', 'CAUAA', 'GUCAU', 'GUCAC', 'GCGUG', 'AUAGC', 'CAUAG', 'UGACC', 'UAGAG', 'UAACC', 'GGGGG', 'GUCUA', 'GUAUA', 'UUCAC', 'UUGCG', 'CGUGC', 'GACCU', 'CAGGA', 'UACCC', 'GUAGA', 'GUAGC', 'GCGCC', 'CUUAC', 'CUAAC', 'CCUAC', 'UUAAC', 'GCCUA', 'UAGUG', 'UGUAG', 'GUAGU', 'GUCGC', 'CGCCG', 'AGGCG', 'UAGGC', 'UCGCC', 'GUAUC', 'UACGA', 'UACGU', 'GGGGU', 'GGUCC', 'UAGGG', 'AUACG', 'CGAUU', 'GUCCC', 'GAACC', 'UCGGG', 'CGGGU', 'CGGUA', 'ACCGU', 'CGAGA', 'CGUCC', 'ACGUC', 'CGACG', 'GACGA', 'GACCG', 'GUCCG', 'UACGG', 'ACGCG', 'GACGU', 'CGACC']



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
reIn = compiled regex to search with
seqIn = the RNA or DNA to search
Note:
matchIndex/length(seqIn) = iRatio 
percGT = iRatio that valid matches are greater than
percLT = iRatio that valid matches are less than
headerIn = a string for the header of the sequence
flipped = if the sequnce has already been flipped for recursive call in the motif; False to flip, True to not flip
debug = will print debug info for the method to the command line
matchList = a list of valid match objects from the 
"""
def MotifMatch(reIn, seqIn, percLT, percGT, headerIn, flipped, debug):
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
"""
Finds the motif in a sequence and returns a feature vector
seq = the sequence to analyze
isRNA = boolean for converting to RNA
featuresOut = the features found in the sequnce in a vector/list
"""	
def snoMotifFind(seq,nMerSplit,isRNA):
	header = "no header"
	matchDebug = False
	hboxre = re.compile(r'([A].{1}[A].{2}[A])')
	acare = re.compile(r'(ACA)')
	dboxre = re.compile(r'(CUGA)')
	cboxre = re.compile(r'([AUGC][UG]GA[UA]G[AUGC])')
	if isRNA:
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
			if motif in hboxFeatureList:
				hacaFeatures[hboxFeatureList.index(motif)] = 1 #THE FEATURE MATRIX IS BUILT HERE!!!
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
			if motif in cboxFeatureList:
				cdFeatures[cboxFeatureList.index(motif)] = 1 #THE FEATURE MATRIX IS BUILT HERE!!!
	#D box IS HERE
	[dMotifs,dbMotifs,dIsFlipped,dOutString] = MotifMatch(dboxre,seq,1,0,header,True,matchDebug)
	freqOfFeatures[3] = len(dMotifs)
	#sliding window HERE
	if nMerSplit>0:
		slideFeat = slideBreak3(seq,nMerSplit,False)
	if nMerSplit<0:
		nMerSplit = -nMerSplit
		selectList = []
		if nMerSplit == 1:
			selectList = selectedFeatures1
		if nMerSplit == 2:
			selectList = selectedFeatures2
		if nMerSplit == 3:
			selectList = selectedFeatures3
		
		slideFeat = slideBreak2(seq,selectList,False)
	#Adding all feature vectors to their respective lists
	featuresOut = freqOfFeatures+hacaFeatures+cdFeatures+slideFeat
	return featuresOut
"""
Compiles a list of all feature vectors
fastaIn = fasta to load
tList = a list of the class type of the sequences being processed
isRNA = boolean for RNA or not
fOut = feature vector list compiled
tOut = type list compiled

"""
def featureFinder(seqL,tList,nMerSplit,isRNA,debug):
	fOut = []
	tOut = []
	for seq in seqL:
		fOut.append(str(snoMotifFind(seq,nMerSplit,isRNA)))
		tOut.append(tList)
	if debug:
		for i in range(len(fOut)):
			print fOut[i]
			print tOut[i]
	return fOut,tOut

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

"""
A function to break a seq down into a freqency of sliding n-mers
"""
def slideBreak(seq,window,debug):
	freqL = []
	nmerL = nmerTotalList[window-1]
	for i in range(len(nmerL)):
		freqL.append(0)
	for i in range(len(seq)-(window-1)):
		subSeq = seq[i:i+window]
		
		if subSeq in nmerL:
			freqL[nmerL.index(subSeq)] += 1
		if debug:
			print str(i) + ":" + str(featIndex) + ":" + subSeq
	return freqL
	
"""
A function to break a seq down into a freqency of sliding n-mers
"""
def slideBreak3(seq,window,debug):
	freqL = []
	totalL = []
	curWindow = 1
	while curWindow <= window:
		totalL += slideBreak(seq,curWindow,False)
		#print totalL
		curWindow += 1
	return totalL

	
"""
A function to break a seq down into a freqency of sliding n-mers
"""
def slideBreak2(seq,listIn,debug):
	freqL = []
	nmerL = listIn
	window = len(listIn[0])
	for i in range(len(nmerL)):
		freqL.append(0)
	for i in range(len(seq)-(window-1)):
		subSeq = seq[i:i+window]
		
		if subSeq in nmerL:
			freqL[nmerL.index(subSeq)] += 1
		if debug:
			print str(i) + ":" + str(featIndex) + ":" + subSeq
	return freqL

"""
function that returns a dict of nMers and frequencies
"""
def featListSort(featIn,keyL):
	freqD = {}
	for item in keyL:
		freqD[item] = 0
	for featureL in featIn:
		for i in range(len(featureL)):
			key = keyL[i]
			freqD[key] += featureL[i]
	return freqD

"""
size = 5
posheadL,posseqL = fastaRead(sys.argv[1],True,False)
pfeatL = []
for seq in posseqL:
	pfeatL.append(slideBreak(seq,size,False))
negheadL,negseqL = fastaRead(sys.argv[2],True,False)
nfeatL = []
for seq in negseqL:
	nfeatL.append(slideBreak(seq,size,False))
pFD = featListSort(pfeatL,nmerTotalList[size-1])
nFD = featListSort(nfeatL,nmerTotalList[size-1])

ratioD = {}
newSelectedFeatures = []
for m in sorted(pFD, key=pFD.get,reverse=True):
	posFratio = float(pFD[m])/len(posheadL)
	negFratio = float(nFD[m])/len(negheadL)
	tFratio = posFratio/negFratio
	if tFratio<.6 or tFratio>1.4:
		newSelectedFeatures.append(m)
	#print m,":", "{0:.2f}".format(posFratio),":", "{0:.2f}".format(negFratio)
	ratioD[m] = tFratio

#for m in sorted(ratioD, key=ratioD.get,reverse=True):
#	print m , ":", "{0:.2f}".format(ratioD[m])

print newSelectedFeatures
"""
