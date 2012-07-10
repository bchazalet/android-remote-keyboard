#!/usr/bin/python -tt

#import sys
#import os
import subprocess

# $adb shell
# input text hello
# input keyevent 26 !! 26 turns off the screen!
# input text world
# input keyevent 66 --> ENTER

adb = None

def main():
	# Listen for user input including ENTER
	print 'Input your text'
	global adb
	# Needs the stdout PIPE otherwise gets automatically redirected in my stdout
	adb = subprocess.Popen(["adb", "shell"], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	try:
		while(True):
			process_input()

	except KeyboardInterrupt: #Ctrl-C
		print "\nCtrl^C received --> dying now"
		adb.stdin.write("exit\n")
		adb.terminate()

def process_input():
	user_input = raw_input('')
	# Split sentence into words
	words = user_input.split(' ');

	# loop on all words
	for word in words:
		# Call adb shell input
		send_word(word)
		send_space()

	#send_key(22) # Right to reach the Send button
	#send_enter() # ENTER to push the Send button
	#send_key(21) # Left to give the focus back to the text input

def send_space():
	send_key(62)

def send_enter():
	send_key(66)

# Key should be an int
def send_key(key):
	adb.stdin.write("input keyevent %d\n" % key)

def send_word(text):
	adb.stdin.write("input text %s\n" % text)

if __name__ == '__main__':
	main()
