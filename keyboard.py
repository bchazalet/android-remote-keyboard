#!/usr/bin/python -tt

#import sys
#import os
import subprocess

# $adb shell
# input text hello
# input keyevent 26 !! 26 turns off the screen!
# input text world
# input keyevent 66 --> ENTER


def main():
	# Listen for user input including ENTER
	print 'Input your text'
	try:
		while(True):
			process_input()

	except KeyboardInterrupt: #Ctrl-C
		print "\nCtrl^C received --> dying now"
	

def process_input():
	user_input = raw_input('')
	# Split sentence into words
	words = user_input.split(' ');

	# loop on all words
	for word in words:
		# Call adb shell input
		send_word(word)
		send_space()

	send_key(22) # Right to reach the Send button
	send_enter() # ENTER to push the Send button
	send_key(21) # Left to give the focus back to the text input

def send_space():
	send_key(62)

def send_enter():
	send_key(66)

# Key should be an it
def send_key(key):
  # Here we should check if key is an int and return error
  try:
    process = subprocess.Popen(["adb", "shell", "input", "keyevent", str(key)], shell=False) #os.system(cmd) --> issue with unicode chars
    process.wait()
  except KeyboardInterrupt: #Ctrl-C
    process.terminate()
    print "The process has been interrupted --> dying now"
  except:
    print "Oops, something unexpected happened while running adb shell input keyevent"	

def send_word(text):
	# Here we should check if there is any space in the text and return error if so
	try:			
		process = subprocess.Popen(["adb", "shell", "input", "text", text], shell=False) #os.system(cmd) --> issue with unicode chars
		process.wait()
	except KeyboardInterrupt: #Ctrl-C
		process.terminate()
		print "The process has been interrupted --> dying now"
	except:
		print "Oops, something unexpected happened while running adb shell input text"

if __name__ == '__main__':
	main()
