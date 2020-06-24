#ifndef __INTERVAL_TREE_H__
#define __INTERVAL_TREE_H__

#include <cinttypes>
#include <string>
#include <vector>
#include <map>

#include "interval_info.h"
#include "common.h"

using namespace std;

template<class T>
class FlatIntervalTree {
private:
    vector <IntervalInfo<T>> disjoint_intervals;

    void shift_right(int ind);

    bool handle_overlap(int &cur_ind, const T &fresh);

    int search(uint32_t target);

public:
    FlatIntervalTree(void);
    ~FlatIntervalTree(void);

    bool add_dummy_interval(const IntervalInfo<T> &temp);
    void build(map <T, string> &sorted_list);

    IntervalInfo<T> *find(uint32_t pos);
    IntervalInfo<T> *find_ind(uint32_t pos, int &ind);

    IntervalInfo<T> *get_node(int ind);

    void build_trans2seg_table(int trans_cnt, vector <vector<uint8_t>> &trans2seg, vector<int> &starts);

    void print();
};

#include "interval_tree_impl.h"

#endif //__INTERVAL_TREE_H__
