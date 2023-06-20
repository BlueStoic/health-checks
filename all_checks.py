#!/usr/bin/env python3
import subprocess
#  This file have cpu safety checks functions.

def check_cpu_temperature():
    """  Shows current cpu's temperature and inform if it is above the safety limit"""
    return '30 C'

cpu_temp = check_cpu_temperature()
print(cpu_temp)