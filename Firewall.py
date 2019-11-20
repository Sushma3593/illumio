csv_file_path = "firewall_rules.csv"

class Port:
	def __init__(self,port):
		self.port_range = False
		if "-" in port:
			pstart,pend = port.split("-")
			self.pstart = int(pstart)
			self.pend = int(pend)
			self.port_range = True
		else:
			self.port = int(port)

	def port_match(self, input_port):
		if self.port_range:
			return (self.pstart <= input_port and input_port <= self.pend)
		else:
			#should be individual port
			return (input_port == self.port)

		return False

class IpAddress:
	def __init__(self,address):
		self.ip_range = False
		if "-" in address:
			ipstart,ipend = address.split("-")
			self.ipstart = ipstart
			self.ipend = ipend
			self.ip_range = True
		else:
			self.address = address
	
	def convert_ipv4(self,ip):
		return tuple(int(n) for n in ip.split('.'))	

	def ip_address_match(self,input_address):
		if self.ip_range:
			return (self.convert_ipv4(self.ipstart) <= self.convert_ipv4(input_address) <= self.convert_ipv4(self.ipend))
		else:
			return (input_address == self.address)
		return False

class Rule:
	def match(self,direction, proto, port, ip_address):
		if direction != self.direction:
			return False
		elif proto != self.proto:
			return False
		elif self.port_obj.port_match(port) != True:
			return False
		elif self.ip_address_obj.ip_address_match(ip_address) != True:
			return False
	
		return True

	def __init__(self, rule_str):
		self.direction,self.proto,self.port,self.address = rule_str.split(",")

		self.address = self.address.rstrip()
		self.port_obj = Port(self.port)
		self.ip_address_obj = IpAddress(self.address)

class Firewall:
	def parse_input(self, file_name):
		with open(file_name) as fp:
			for rule in fp:
				rule_obj = Rule(rule)
				self.rule_list.append(rule_obj)

	def accept_packet(self, direction, proto, port, ip_address):
		for r in self.rule_list:
			if (r.match(direction, proto, port, ip_address)):
				return True
		return False

	def __init__(self, file_name):
		self.rule_list = []
		self.parse_input(file_name)

if __name__ == "__main__":
	fw_obj = Firewall(csv_file_path)
	test_output = fw_obj.accept_packet("inbound","udp",53,"192.168.1.1")
	print(test_output)
