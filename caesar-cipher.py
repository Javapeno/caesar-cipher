print "Do you want to encrypt or decrypt the message (e/d)"
action = raw_input("> ")
while action != "e" and action != "d":
	action = raw_input( "(e/d): ")

abc_l_e = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
abc_u_e = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc_l_d = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
abc_u_d = "ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBA"
chars = "!\"#$%&'()*+-'-./:;<=>?@[]^_{}|~1234567890"

if action == "e":
	print "\nEnter the message to encrypt"
	message = raw_input("> ")

	print "\nEnter the key"
	try:
		key = input("> ")
		while not (key >= 1 and key <= 26):
			print "Number not in range (1-26). Try again"
			key = input("> ")
	except:
		print "That's not a correct integer. Try again."
		exit()

	e_message = ""
	for char in message:
		if char in abc_l_e:
			e_message += abc_l_e[(abc_l_e.index(char) + key)]
		if char in abc_u_e:
			e_message += abc_u_e[(abc_u_e.index(char) + key)]
		elif char == " ":
			e_message += " "
		elif char in chars:
			e_message += char
	print "Your encrypted message is:\n", e_message

elif action == "d":
	print "\nEnter the message to decrypt"
	message = raw_input("> ")
	print "\nEnter the key (enter \"n\" if you don't know)"
	try:
		key = raw_input("> ")
		if key != "n":
			while not (int(key) >= 1 and int(key) <= 26):
				print "Number not in range (1-26). Try again"
				key = input("> ") 
	except:
		print "That's not a correct integer nor \"n\". Try again."
		exit()

	d_message = ""
	if key != "n":
		key = int(key)	
		for char in message:
			if char in abc_l_d:			
				d_message += abc_l_d[(abc_l_d.index(char) + key)]
			elif char in abc_u_d:
				d_message += abc_u_d[(abc_u_d.index(char) + key)]
			elif char == " ":
				d_message += char
			elif char in chars:
				d_message += char
		print "Your decrypted message is:\n", d_message

	if key == "n":
		results = []
		for turn in range(1,26):
			d_message = ""
			for char in message:
				if char in abc_l_d:
					d_message += abc_l_d[(abc_l_d.index(char) + turn)]
				elif char in abc_u_d:	
					d_message += abc_u_d[(abc_u_d.index(char) + turn)]
				elif char == " ":
					d_message += char
				elif char in chars:
					d_message += char
			results.append(d_message)

		print "\nYour decrypted message is between one of the following:"
		for result in results:
			print "%d." % (results.index(result) + 1), result
