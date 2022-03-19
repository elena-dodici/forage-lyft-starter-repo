# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:00:18 2022

@author: 吴佳琦
"""

def addYears(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result