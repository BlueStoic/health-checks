#!/usr/bin/env python3
import os
import shutil
import sys

def check_reebot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exist("/run/reoot-required")

def check_disk_full(disk, min_gb, min_percent):
	""" Returns true if there isn't enough disk space, false otherwise."""
	du = shutil.disk_usage(disk)
	percent_free = 100 * du.free / du.total
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False


""" The main function contains the call to all the other functions"""
def main():
	if check_reebot():
		print("Pending reboot.")
		sys.exit(1)
	if check_disk_full(disk='/', min_gb=2, min_percent=10):
		print('Disk full')
		sys.exit(1)
	print('Everything ok')
	sys.exit(0)

main()
