#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    bam = len(my_list)
    if idx < 0 or idx >= bam or bam == 0:
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)
