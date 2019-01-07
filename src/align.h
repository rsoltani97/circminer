#ifndef __ALIGN_H__
#define __ALIGN_H__

#define MAXSTRSIZE 100

#include "common.h"

typedef struct {
	int q_matched;
	int r_matched;
	int score;
	int ed_dist;
} LocAlign;

struct AlignCandid{
	int ed;
	int sclen;
	int indel;

	AlignCandid (int e, int s, int i) : ed(e), sclen(s), indel(i) {}

	bool operator < (const AlignCandid& r) const {
		if (ed != r.ed)
			return ed < r.ed;
		if (sclen != r.sclen)
			return sclen < r.sclen;
		return indel < r.indel;
	}
};

class Alignment {
public:
	Alignment(void);
	~Alignment(void);
	void init(void);

	bool hamming_match_right(char* s, int n, char* t, int m);
	bool hamming_match_left (char* s, int n, char* t, int m);

	int  hamming_distance_right(char* s, int n, char* t, int m, int& sc_len);
	int  hamming_distance_left (char* s, int n, char* t, int m, int& sc_len);
	
	int global_alignment(char* s, int n, char* t, int m, int gap_pen, int mm_pen);
	int global_alignment(char* s, int n, char* t, int m);
	int global_alignment_reverse(char* s, int n, char* t, int m);

	void global_banded_alignment(char* s, int n, char* t, int m);
	void global_banded_alignment_reverse(char* s, int n, char* t, int m);
	
	void hamming_distance(char* s, int n, char* t, int m);
	void hamming_distance_bottom(char* s, int n, char* t, int m, int max_sclen);
	void hamming_distance_top(char* s, int n, char* t, int m, int max_sclen);
	
	// in the following are prefix to global alignmen 
	// prefix on s
	// global on t
	int local_alignment_right_sc(char* s, int n, char* t, int m, int& sc_len, int& indel);
	int local_alignment_left_sc (char* s, int n, char* t, int m, int& sc_len, int& indel);

	int local_alignment_right(char* s, int n, char* t, int m, int& indel);
	int local_alignment_left (char* s, int n, char* t, int m, int& indel);

	int local_alignment_left2(char* s, int n, char* t, int m, int& sc_len, int& indel);

private:
	int dp[MAXSTRSIZE][MAXSTRSIZE];
	int hamm[MAXSTRSIZE][MAXSTRSIZE];
	int diff_ch[ASCISIZE][ASCISIZE];
};

extern Alignment alignment;

#endif	//__ALIGN_H__
