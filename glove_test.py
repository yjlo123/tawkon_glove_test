import sys
import os

def code_to_country(code):
	if code in (1, 2):
		return 'IL'
	elif code in (3, 4):
		return 'US'
	else:
		return 'unknown'

def code_to_lang(code):
	if code in (1, 3):
		return 'en'
	elif code in (2, 4):
		return 'he'
	else:
		return 'unknown'

def select_country():
	print "Select country(language):"
	print "1. IL(English)"
	print "2. IL(Hebrew)"
	print "3. US(English)"
	print "4. US(Hebrew)"
	country_language = input("country: ")
	if str(country_language).isdigit():
		return int(country_language)
	else:
		print "Invalid country"
		select_country()

def print_menu(code):
	print "=== Glove Testing ("+code_to_country(code)+"["+code_to_lang(code)+"]) ==="
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
	code = select_country()
	country = code_to_country(code)
	language = code_to_lang(code)
	print_menu(code)
	command = input_command()
	while command != 6:
		if command == 1:
			print "Test Glove("+country+")"
			os.system('monkeyrunner test.py '+country+' '+language)
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
			code = select_country()
			country = code_to_country(code)
			language = code_to_lang(code)
		else:
			print "Invalid command"
		print_menu(code)
		command = input_command()
	print "Finished."
	exit()

main_loop()