#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:49:16 2018

@author: emmaworthington
"""

#adding a comment for github testing

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def show_field(field1, field2):
    '''
    Plot 2 rectangles, given the
    bottom left and top right co-ordinates of each.
    '''
    
    def vertices(left, bottom, right, top):
        verts = [(left, bottom), (left, top), (right, top), (right, bottom), (left, bottom)]
        return verts
    
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    p1 = Path(vertices(* field1), codes)
    p2 = Path(vertices(* field2), codes)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    pa1 = patches.PathPatch(p1, facecolor='orange', lw=2)
    pa2 = patches.PathPatch(p2, facecolor='blue', lw=2)
    ax.add_patch(pa1)
    ax.add_patch(pa2)
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    fig.show()


def overlap_area(field1, field2):
    '''
    Calculates the overlapping area between 2 rectangles, given the
    bottom left and top right co-ordinates of each.
    '''
    
    left1, bottom1, right1, top1 = field1
    left2, bottom2, right2, top2 = field2
    overlap_left = max(left1, left2)
    overlap_bottom = max(bottom1, bottom2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)
    
    # Check that height and width are positive, if not are zero
    overlap_height = max((overlap_top - overlap_bottom), 0)
    overlap_width = max((overlap_right - overlap_left), 0)
    
    area = overlap_height * overlap_width
    
    return area