#!/usr/bin/env python3
import os

def check_reebot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exist("/run/reoot-required")


def main():
	pass


main()
