t = 1#int(raw_input())

def get_next_occupied_wc_c(wcs, wc_i, direction):
    searching = True
    while searching:
        if wcs[wc_i] == False:
            return wc_i
        else:
            wc_i += direction

def get_closest_empty_wc(empty_wcs):
    max_min_ls_rs = 0
    max_min_ls_rs_list = []
    for wc_i, ls_rs in empty_wcs.iteritems():
        ls, rs = ls_rs
        min_ls_rs = min(ls, rs)
        if min_ls_rs > max_min_ls_rs:
            max_min_ls_rs = min_ls_rs
            max_min_ls_rs_list = [wc_i]
        elif min_ls_rs == max_min_ls_rs:
            max_min_ls_rs_list.append(wc_i)
    if len(max_min_ls_rs_list) == 1:
        return max_min_ls_rs_list[0]
    max_max_ls_rs = 0
    max_max_ls_rs_list = []
    for wc_i, rs_rs in [(wc_index, empty_wcs[wc_index]) for wc_index in max_min_ls_rs_list]:
        ls, rs = ls_rs
        max_ls_rs = max(ls, rs)
        if max_ls_rs > max_max_ls_rs:
            max_max_ls_rs = max_ls_rs
            max_max_ls_rs_list = [wc_i]
        elif max_ls_rs == max_max_ls_rs:
            max_max_ls_rs_list.append(wc_i)
    # if len(max_max_ls_rs_list) == 1:
    return max_max_ls_rs_list[0]



for i in xrange(1, t + 1):
    wc_c, people = 4,2#[int(s) for s in raw_input().split(" ")]
    wcs = [False] + wc_c * [True] + [False]
    for man in xrange(people):
        empty_wcs = {}
        for wc_i, wc_free in enumerate(wcs):
            if wc_free:
                l_s = abs(get_next_occupied_wc_c(wcs, wc_i, -1) - wc_i) -1
                r_s = get_next_occupied_wc_c(wcs, wc_i, +1) - wc_i -1
                empty_wcs[wc_i] = (l_s, r_s)
        wc_i = get_closest_empty_wc(empty_wcs)
        wcs[wc_i] = False
    print "Case #{}: {} {}".format(i, max(empty_wcs[wc_i]), min(empty_wcs[wc_i]))

