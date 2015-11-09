haca = '(((((((((.....((..(((((..((((......))))..)))))..))..))))))))).......(((.((((((.(..((((.((((((........)))))).))))...).)))))).)))......'
cd = '(((((....................((((.(.......).))))......(((((((......)))...))))(((((...(((((((.(((((...))))).))))))))))))(((((....)))))....(((.((((..((((((.......)))))))))).)))...)))))........'


def loopFeat(structIn,debug):
	loopLen = 0		#stores the length of the current loop
	loopLenL = []	#a list of loop lengths
	stemLen = 0		#stores the length of the current stem
	stemLenL = []	#a list of stem lengths
	saveS = []		#stores the current unmatched portion of the structure
	flatL = 0		#stores the length of the flat single strand part of the RNA
	debugS = ''
	for c in structIn:	
		if c == ')': #')' triggers a backtrack in the saved string to find corresponding '(' and get the loop length inbetween
			debugS += '\nchecking for stems and loops'			
			while True:
				debugS += "\n" + str(saveS)
				d = saveS.pop()
				if d == '.':
					loopLen += 1
					flatL -= 1
					if stemLen > 0:
						stemLenL.append(stemLen)
						stemLen = 0
						debugS += '\tend of a stem: ' + str(stemLen) + " "
					debugS += '\tloop size: ' + str(loopLen) + " "
					
				elif d == '(':
					stemLen += 1
					if loopLen > 0:
						loopLenL.append(loopLen)
						loopLen = 0
						debugS += '\tloop ends: ' + str(loopLen) + " "					
					debugS += '\tstem bond: ' + str(stemLen) + " "
					break

				elif d == ')':
					print 'WARNING: ")" FOUND, counts are comprimised check program'
					break
					
				else:
					print 'WARNING: nothing is happening in loop detection!'
					break

		elif c == '.':
			if stemLen > 0:
				stemLenL.append(stemLen)
				debugS += str(saveS) + '\nend of a stem: ' + str(stemLen)
				stemLen = 0
			flatL += 1
			saveS.append(c)
			
		elif c == '(':
			saveS.append(c)

		else:
			print 'WARNING: unexpected character, aborting'
			break

		if debug:
			print debugS
		debugS = ''
	
	#computing stats on the structure
	avgLoop = 0
	for n in loopLenL:
		avgLoop += n
	avgLoop = float(avgLoop)/len(loopLenL)
	
	avgStem = 0
	for n in stemLenL:
		avgStem += n
	avgStem = float(avgStem)/len(stemLenL)
	
	medianLoop = loopLenL[:]
	medianLoop.sort()
	medianLoop = medianLoop[len(medianLoop)/2]
	
	medianStem = stemLenL[:]
	medianStem.sort()
	medianStem = medianStem[len(medianStem)/2]
	
	maxLoop = max(loopLenL)
	maxStem = max(stemLenL)

	if debug:
		print 'loops: ' + str(loopLenL)\
		+'\navgloop: ' + str(avgLoop)\
		+'\nmedianloop: ' + str(medianLoop)\
		+'\nmaxloop: ' + str(maxLoop)\
		+ '\nstems: ' +  str(stemLenL)\
		+'\navgStem: ' + str(avgStem)\
		+'\nmedianStem: ' + str(medianStem)\
		+'\nmaxStem: ' + str(maxStem)\
		+ '\nflat: ' + str(flatL)
		
	return [maxLoop,medianLoop,avgLoop,maxStem,medianStem,avgStem,flat]
	
print 'cd'
loopFeat(cd,True)
#print '\nhaca'
#loopFeat(haca,True)
