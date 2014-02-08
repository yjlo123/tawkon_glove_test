import sys
import os

def code_to_country(code):
	if code == 1:
		return 'IL'
	elif code == 2:
		return 'US'
	else:
		return 'unknown'

def select_country():
	print "Select country:"
	print "1. IL"
	print "2. US"
	country = input("country: ")
	if str(country).isdigit():
		return int(country)
	else:
		print "Invalid country"
		select_country()

def print_menu(country_code):
	print "=== Glove Testing ("+code_to_country(country_code)+") ==="
	print "1. Test Glove"
	print "2. Generate raw report"
	print "3. Generate final report"
	print "4. Clean and uninstall"
	print "5. Change country"
	print "6. Exit"

def input_command():
	command = input("Command: ")
	if str(command).isdigit():
		return int(command)
	else:
		print "Invalid command"
		input_command()

def main_loop():
	country_code = select_country()
	country = code_to_country(country_code)
	print_menu(country_code)
	command = input_command()
	while command != 6:
		if command == 1:
			print "Test Glove("+country+")"
			os.system('monkeyrunner test.py '+country)
		elif command == 2:
			print "Generate raw report"
			os.system('python report.py '+country)
		elif command == 3:
			print "Generate final report"
			os.system('python report_final.py '+country)
		elif command == 4:
			print "Clean screenshots"
			os.system('monkeyrunner clean.py')
		elif command == 5:
			country_code = select_country()
			country = code_to_country(country_code)
		else:
			print "Invalid command"
		print_menu(country_code)
		command = input_command()
	print "Finished."
	exit()

main_loop()