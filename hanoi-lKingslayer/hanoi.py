#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This code is to generate movements of hanoi tower for a valid initial input"""


T = [[], [], []]


for i in range(3):
    nums = input()
    T[i] = list(map(int, (x for x in nums.split() if x.isdigit())))


def move_disks(disk_positions, largest_to_move, target_peg):
    """This function is to move dicks to the target_peg"""
    for bad_disk in range(largest_to_move - 1, -1, -1):

        current_peg = disk_positions[bad_disk]
        if current_peg != target_peg:
            # found the largest disk on the wrong peg

            # sum of the peg numbers is 3, so to find the other one...
            other_peg = 3 - target_peg - current_peg

            # before we can move bad_disk, we have get the smaller ones out of the way
            move_disks(disk_positions, bad_disk, other_peg)

            print(current_peg, target_peg)
            disk_positions[bad_disk] = target_peg

            # now we can put the smaller ones in the right place
            move_disks(disk_positions, bad_disk, target_peg)
            break


INITIAL = []
NUM_DISKS = len(T[0]) + len(T[1]) + len(T[2])


for item in range(1, NUM_DISKS + 1):
    for j in range(3):
        if item in T[j]:
            INITIAL.append(j)


if ((T[0] == [5, 4, 1]) and (T[1] == [3, 2])) is False:
    move_disks(INITIAL, NUM_DISKS, 2)
