import re
import sys

fname = sys.argv[1]
lens = [0,
		0,	#chr 1
		81195210 + 78077248 + 59128983 + 3,
		81195210 + 78077248 + 59128983 + 243199373 + 63025520 + 48129895 + 51304566 + 7,
		81195210 + 78077248 + 59128983 + 243199373 + 63025520 + 48129895 + 51304566 + 198022430 + 8,
		0,
		180915260 + 1,
		180915260 + 171115067 + 2,
		180915260 + 171115067 + 159138663 + 3,
		180915260 + 171115067 + 159138663 + 146364022 + 4,
		249250621 + 1,
		249250621 + 135534747 + 2,
		249250621 + 135534747 + 135006516 + 3,
		249250621 + 135534747 + 135006516 + 133851895 + 4,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878 + 5,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878 + 107349540 + 6,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878 + 107349540 + 102531392 + 7,
		0,
		81195210 + 1,
		81195210 + 78077248 + 2,
		81195210 + 78077248 + 59128983 + 243199373 + 4,
		81195210 + 78077248 + 59128983 + 243199373 + 63025520 + 5,
		81195210 + 78077248 + 59128983 + 243199373 + 63025520 + 48129895 + 6,
		180915260 + 171115067 + 159138663 + 146364022 + 141213431 + 5,						#MT
		180915260 + 171115067 + 159138663 + 146364022 + 141213431 + 16569 + 6,				#X
		180915260 + 171115067 + 159138663 + 146364022 + 141213431 + 16569 + 155270560 + 7	#Y
		]

ch2int = { str(x): x for x in range(1, 23) }
ch2int["MT"] = 23
ch2int["X"] = 24
ch2int["Y"] = 25
#print ch2int

with open(fname, "r") as f:
	for l in f:
		l = l.strip();
		if l[0] == "#":
			print l
			continue

		ll = re.split("\t", l)

		if ll[0] not in ch2int.keys():
			print l
			continue
		ch = ch2int[ll[0]]
	
		st = int(ll[3])
		end = int(ll[4])
		new_contig = ""
		if ch in [1, 10, 11, 12, 13, 14, 15, 16]:
			new_contig = "1"
		elif ch in [2, 3, 4, 17, 18, 19, 20, 21, 22]:
			new_contig = "2"
		else:
			new_contig = "3"
				
		print "\t".join( [ new_contig, ll[1], ll[2], str(st + lens[ch]), str(end + lens[ch]) ] + ll[5:] )
