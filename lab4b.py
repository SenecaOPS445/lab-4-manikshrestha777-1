#!/usr/bin/env python3

def join_lists(l1, l2):
    joined_set = set(l1) | set(l2)
    return list(joined_set)
    # join_lists will return a list that contains every value from both l1 and l2

def match_lists(l1, l2):
    match_set = set(l1) & set(l2)
    return list(match_set)
    # match_lists will return a list that contains all values found in both l1 and l2

def diff_lists(l1, l2):
    diff_set = set(l1) ^ set(l2)
    return list(diff_set)
    # diff_lists will return a list that contains all different values, which are not shared between the lists

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))