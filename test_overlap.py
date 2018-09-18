#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:17:49 2018

@author: emmaworthington
"""

from overlap import overlap_area
from pytest import approx

def test_entirely_inside_not_touch():
    '''
    Tests that basic example works. One field is entirely inside
    the other with no sides touching.
    '''
    
    big_field = (1, 1, 4, 4)
    inner_field = (2, 2, 3, 3)
    
    assert overlap_area(big_field, inner_field) == 1
    
def test_corners_overlap():
    '''
    Two fields with only a corner of each overlapping.
    Use non-integer values
    '''
    
    field1 = (1, 1, 4.5, 3.5)
    field2 = (2, 2, 2.8, 3.9)
    
    assert overlap_area(field1, field2) == approx(1.19999, rel=1e-3)

def test_inside_touch():
    '''
    Two fields, one inside the other,
    touching on one side.
    '''
    
    field1 = (1, 1, 4, 4)
    field2 = (2, 3, 3, 4)
    
    assert overlap_area(field1, field2) == 1

def test_outside_touch():
    '''
    Two fields, one outside the other,
    touching on one side, no overlap.
    '''
    
    field1 = (1, 1, 4, 2)
    field2 = (2, 2, 3, 3)
    
    assert overlap_area(field1, field2) == 0
    
def test_corner_touch():
    '''
    Two fields with a single corner touching
    '''
    
    field1 = (1, 1, 2, 2)
    field2 = (2, 2, 3, 3)
    
    assert overlap_area(field1, field2) == 0
    
def test_separate():
    '''
    Two fields not touching
    '''
    
    field1 = (1, 1, 2, 2)
    field2 = (3, 3, 4, 4)
    
    assert overlap_area(field1, field2) == 0   
    
