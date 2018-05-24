#ifndef __GENE_ANNOTATION_H__
#define __GENE_ANNOTATION_H__

#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <map>

using namespace std;

typedef struct {
	string gene_id;
	string gene_name;
	string chr;
	uint32_t start;
	uint32_t end;
} ExonSeg;

typedef struct GTFRecord {
	string chr;
	string source;
	uint32_t start;
	uint32_t end;
	string gene_id;
	string trans_id;
	int exon_num;
	string gene_name;

	bool operator < (const GTFRecord& r) const {
		return (chr == r.chr) ? (start < r.start) : (chr < r.chr);
	}
} GTFRecord;


class GTFParser {
private:
	FILE* input;
	size_t file_size;

	char* line;
	int len;
	size_t max_line_size;

	GTFRecord* current_record;
	vector <GTFRecord> records;
	map <string, vector <ExonSeg> > wt_exons;

public:
	GTFParser (void);
	GTFParser (char* filename);
	~GTFParser (void);

	void init (char* filename);
	bool get_next (void);
	bool has_next (void);
	bool read_next (void);

	void tokenize(char* line, int len, const string& delim, vector<string>& gtf_fields);
	bool parse_gtf_rec (char* line, int len);
	bool load_gtf (void);
	void set_wild_type(void);

	int binary_search(const vector <ExonSeg>& seg, int beg, int end, bool on_start, uint32_t target);
	int search_loc(const string& chr, bool on_start, uint32_t target);

	void print_record(const GTFRecord& r);
	void print_records(void);
};

#endif	//__GENE_ANNOTATION_H__
