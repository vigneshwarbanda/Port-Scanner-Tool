import socket
import termcolor

def scan(target,ports):
	print('\n' + 'Starting Scan For '+ str(target))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress,port):
	try:
		sock=socket.socket()
		sock.connect((ipaddress,port))
		print("[+] Port Opened :" + str(port))
		sock.close()
	except:
		pass
target = input("[*] Enter Targets To Scan (split them bt,): ")
ports=int(input("[*] Enter How Many Ports You Want To scan: "))
if ',' in target:
	print(termcolor.colored(("[*] Scanner Multiple Targets"),'green'))
	for ip_addr in target.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(target,ports)
