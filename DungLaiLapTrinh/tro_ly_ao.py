import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

i=0
while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listenning")
		audio = robot_ear.listen(mic)
	print("Robot: ...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Viet Quan handsome"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "bye" in you:
		robot_brain = "bye Viet Quan"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")

	else:
		robot_brain = "I'm fine thank you, and you"

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

	i = i+1
	if i==10:
		break