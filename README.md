# Tutorial-Makeblock-XY-plotter

This is a tutorial to draw the current weather directly by your Makeblock XY plotter. 

----------------------------------------------  TUTO ------------------------------------------------
What do you need:
-Makeblock XY Plotter
-Python 2.7 (not 3.4) -> Software
-Arduino Software -> Software

1)	Preparing the plotter board 
Firstly you have to upload the correct Arduino code in the XY plotter. This code will manage motors and sensors. Open the Arduino code, located in the Arduino folder, in the software and upload it directly in the plotter via USB. In the GCodeParser.ino, you can change the value of “Fast_XY_Feedrate” to increase or reduce the stepping motors speed, but you have to take care, increasing the speed will reduce the accuracy of the drawing. You can also change the final size of the drawing by increasing/decreasing the “X_STEPS_PER_MM” and “Y_STEPS_PER_MM”, don’t forget to change the steps per inch as well. Currently, values give a final result around 18x18cm.

2)	Setting the weather location
In the folder “Code”, open the “Data.py” file with Python IDLE 2.7, not 3.4 because the code is write on 2.7. The following link manages the weather location, it is currently located in Valetta in Malta. “http://api.openweathermap.org/data/2.5/weather?q=Valetta,MT&appid=77a9c4104f54722fbbeb8c6048122c56 ”

You can change it to your place, replace “Valetta” by your place and “MT” by the initial of your country. Please try on internet if it works, else replace the city name by the biggest city closest to your current location, because every cities don’t be registered.
When it works, you have to replace your final link in the “Data.py”.

3)	Setting & Initiate the serial port
Now you have to have to select the correct serial port to send data directly to the plotter.
Go in your “Control panel”, in “Device Manager” and find the correct COM of your plotter.
Then replace the value instead of “COM5” already written.

4)	Let’s draw!
Everything is ready, so you just have to run Data.py, the shortcut is F5. Please be insured that you have all the libraries needed. You need also to have an internet connection because the software downloads weather data from the web. Enjoy!

