import speech_recognition as sr
import RPi.GPIO as GPIO;
from os import path
from subprocess import call

GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);
GPIO.cleanup();
first= 14;
second = 15;
third = 18;
fourth= 23;

GPIO.setup(first, GPIO.OUT);
GPIO.setup(second, GPIO.OUT);
GPIO.setup(third, GPIO.OUT);
GPIO.setup(fourth, GPIO.OUT);


GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnon(led):
        GPIO.output(led, 1);
def turnoff(led):
        GPIO.output(led, 0);



while True :
        input_state = GPIO.input(25)
        if input_state == False :
                print ('Button Pressed')
                call(["arecord" ,"-D" , "plughw:2,0" ,"-d" , "5" ,"test.wav"])
                AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
                r = sr.Recognizer()
                with sr.AudioFile(AUDIO_FILE) as source:
                        audio = r.record(source) # read the entire audio file
                try:
                        # for testing purposes, we're just using the default API key
			txt =  r.recognize_google(audio) 
                        print("Alfred: " + txt )
			if "first" in txt:
				if "on" in txt:
					turnon(first);
				if "of" in txt:
					turnoff(first);
			if "second" in txt:
                                if "on" in txt:
                	                turnon(second);
                                if "of" in txt:
                        	        turnoff(second);
			if "light" in txt:
                                if "on" in txt:
                       	        	turnon(third);
                                if "of" in txt:
                        	        turnoff(third);
			if "television" in txt:
                                if "on" in txt:
                       		        turnon(fourth);
                                if "of" in txt:
                             		turnoff(fourth);
   			if "all" in txt:
                                if "on" in txt:
                                        turnon(first);
					turnon(second);
					turnon(third);
					turnon(fourth);
                                if "of" in txt:
                                        turnoff(first);
					turnoff(second);
                                        turnoff(third);
                                        turnoff(fourth);
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""                   
finally:
        GPIO.cleanup();
"""
