#!/usr/bin/env python3
import os
import sys

def check_reebot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exist("/run/reoot-required")


def main():
	if check_reebot():
		print("Pending reboot.")
		sys.exit(1)
	print("Everything is OK")
	sys.exit(0)


main()
