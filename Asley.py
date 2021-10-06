# coded by hiccup 2021.10.6 to ashley
import sys
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", dest="file", default=False, action="store_true")
arg_parser.add_argument("input", type=str)
arg_parser.add_argument("output", type=str)
args = arg_parser.parse_args()

if args.file:
    with open(args.input, "r") as file:
        emails = file.readlines()
else:
    emails = [args.input]

for email in emails:
    if email.count("@hotmail") != 1:
        continue
    username, _ = email.split("@")
    username = ''.join([i for i in username if not i.isdigit()])
    if username.find(".") > 0:
    	firstname, lastname = username.split(".")
    else:
    	if username.find("_") > 0:
    		firstname, lastname = username.split("_")
    	else:
    		firstname = username
    		lastname = ""
    # print(f"Your username: {username}")
    with open('out.txt', 'a') as file:
    	file.write(f"First Name:{firstname}" + ',  ' + f"Last Name:{lastname}")
    	file.write('\n')
print("Hello Ashley,  see out.txt file in your input file directory")