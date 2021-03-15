import pyttsx3

robot_branch = "Quan handsome"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_branch)
robot_mouth.runAndWait()