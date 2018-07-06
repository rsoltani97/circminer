import re
import sys

fname = sys.argv[1]

lens = [0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		249250621,
		249250621 + 135534747,
		249250621 + 135534747 + 135006516,
		249250621 + 135534747 + 135006516 + 133851895,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878 + 107349540,
		249250621 + 135534747 + 135006516 + 133851895 + 115169878 + 107349540 + 102531392,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0]

with open(fname, "r") as f:
	for l in f:
		l = l.strip();
		if l[0] == "#":
			print l
			continue

		ll = re.split("\t", l)

		ch = ll[0]
		st = int(ll[3])
		end = int(ll[4])
		if ch not in ["10", "11", "12", "13", "14", "15", "16"]:
			print l
		else:
			ch = int(ch)
			if ch >= 10 and ch <=16:
				print "\t".join( [ "1", ll[1], ll[2], str(st + lens[ch]), str(end + lens[ch]) ]
									+ ll[5:] )
			else:
				print l

