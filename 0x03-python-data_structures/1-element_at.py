#!/usr/bin/python3
def element_at(my_list, idx):
    bam = len(my_list)
    if idx < 0 or idx >= bam or bam == 0:
        return None
    else:
        return my_list[idx]
