Testing
	I ran test cases covering the sample inputs first. In addition I also ensured that the rules containing improper format for direction and protocol fields and out of range values for ports and addresses are blocked. 

Code explanation:
	I have structured my code into 4 classes (Firewall, Rule, Port and IpAddress):
		
	1) Firewall:
		This class has a constructor which takes the file path as the argument and creates an object of the rule by parsing each rule in the file one line after the other. It also has an "accept_packet" method which takes in arguments direction,protocol,port and ip addres and compares with each rule set read from the csv file.
	
	2) Rule:
		This class has a constructor which takes each rule set parsed by the Firewall class from the csv file. In addition an object of Port and IpAddress has been initialized in this constructor.
		It also has a method "match" which takes the arguments direction,protocol,port and ip address and compares each field with that of provided input.

	3) Port:
		This class has a constructor which takes as the argument port which is parsed by the csv file. It checks if the port is a single entity or range and initializes the start and the end ports accordingly. It also has a method "port_match" which checks if the input port is within the range provided in the csv file.

	4) IpAddress:
                This class has a constructor which takes as the argument ip address which is parsed by the csv file. It checks if the ip address is a single entity or range and initializes the start and the end address accordingly. It also has a method "ip_address_match" which checks if the input address is within the range provided in the csv file.

Code Execution:
	1) Code has a variable "csv_file_path" which needs to be initialized with the exact path of the csv file.
	
	2) We can create an object of the Firewall class. Example: fw_obj = Firewall(csv_file_path)
	
	3) Then we can call the "accept_packet" method of the Firewall class. Example: test_output = fw_obj.accept_packet("outbound","udp",53,"192.168.1.1")
										       print(test_output)
	
	4) We can run the code as: python Firewall.py

Team:
	First preference: Data team
	Second preference: Platform team
	Third preference: Policy team
