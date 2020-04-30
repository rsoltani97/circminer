import sys
import re
#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#import numpy as np

def parse_cigar(cigar):
	mysum = 0
	ind = 0
	lens = re.split("M|D|N|=|X|I|S|H|P", cigar)
	if lens[-1] == '':
		del lens[-1]

	types = [ c for c in cigar if not c.isdigit() ]

	#print cigar
	#print types
	#print lens

	count = { }
	for t in "MDN=XISHP":
		count[t] = 0
	for i in range(len(types)):
		count[types[i]] += int(lens[i])

	#print count
	return count['S'], count['I'] + count['D'], count['N']

#def plot(dist):
#	fig = plt.figure()
#	ax = fig.add_subplot(111, projection='3d')
#	xs = range(76)
#	for d in dist:
#		ax.bar(xs, d)
#	
#	ax.set_xlabel('CS')
#	ax.set_ylabel('ERR')
#	ax.set_zlabel('CNT')
#
#	plt.show()

sam_fname = sys.argv[1]

dist = [[[ 0 for x in range(2*76) ] for y in range(2*76) ] for z in range(2*76) ]

line = 0
mate_sc = 0
mate_err = 0
mate_mm = 0
mate_indel = 0
mate_intron = 0
mate_sam = ""
mate_md = ""

with open(sam_fname, 'r') as sf:
	for l in sf:
		if l[0] == '@':
			continue

		ll = l.strip().split()
		
		flag = int(ll[1])
		if flag > 255:
			continue

		line += 1
		
		cigar = ll[5]
		if cigar == "*":
			print "bad cigar!!!"
			continue

		nm = [x for x in ll[11:] if x.startswith('NM')]
		md = [x for x in ll[11:] if x.startswith('MD')]

		if nm == [] or md == []:
			print '{} Missing NM/MD!!! Assuming no error...'.format(ll[0])
			nm = 'NM:i:0'
			md = 'MD:i:76'
		else:
			nm = nm[0]
			md = md[0]

		#if len(ll) > 16:
		#	nm = ll[15]
		#	md = ll[16]
		#else:
		#	nm = ll[11]
		#	md = ll[12]

		#print cigar, nm
		sc, indel, intron = parse_cigar(cigar)
		mm = int(nm.split(':')[2])
		#print sc, indel, mm
		err = mm + indel

		tlen = abs(int(ll[8])) - mate_intron - intron
		#if (line % 2 == 0) and tlen > 500:
		#	print>> sys.stderr, mate_sam
		#	print>> sys.stderr, l.strip()
		#	continue
		
		if line % 2 == 1:
			mate_sam = l.strip()
			mate_err = err
			mate_sc = sc
			mate_mm = mm
			mate_indel = indel
			mate_intron = intron
			mate_md = md
		
		else:
			dist[indel+mate_indel][mm+mate_mm][sc+mate_sc] += 1
			#if (indel + mate_indel == 0) and (mm + mate_mm > 0) and (sc + mate_sc > 0) and ((md[0] == '1' and not md[1].isdigit()) or (md[-1] == '1' and not md[-2].isdigit()) or (mate_md[0] == '1' and not mate_md[1].isdigit()) or (mate_md[-1] == '1' and not mate_md[-2].isdigit())):
			if indel + mate_indel == 0 and  mm + mate_mm == 0 and sc + mate_sc == 0:
				print>> sys.stderr, mate_sam
				print>> sys.stderr, l.strip()

sums = [ ]
for i in range(76):
	sums.append(sum(sum(dist[i], [])))
print "indel > 0: {}".format( sum(sums[1:]) )

for i in range(10):
	print "indel = {}: {}".format( i, sums[i] )

for d in dist[0][:21]:
	for e in d[:21]:
		print e,
	print

print sum(sum(dist[0],[]))
