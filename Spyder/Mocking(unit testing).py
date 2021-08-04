# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 00:20:55 2021

@author: BHUVI
"""

class Employee:
    raise_amt = 1.05

def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

@property
def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

@property
def fullname (self):
    return '{}{}'.format(self.first, self.last)

def apply_raise (self):
    self.pay = int(self.pay*self.raise_ant)
