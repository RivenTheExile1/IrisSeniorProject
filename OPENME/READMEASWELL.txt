To whom ever reads this,

Hello. My name is Connor Ferwreda. I am currently a senior in my final days of my spring 2021 semester. If you are reading this than you are 
continuing where I left off on Iris. In this doc, I will explain what Iris is, where I left off, what I have done, and much, much more. Get a 
good cup of tea ( my favorite is chamomile, or earl grey ) and indulge me in this trip.

~~~~~~~~~~~~~~~~~~~~ What is Iris? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Iris is a quadcopter drone engineered by 3DR robotics. She has a pixhawk2 navigational system that is attached to a raspberry pi zero w and 
rgb picamera that fits the zero w camera port ( some cameras modules don't fit to the zero w and the standard pis fyi ). 
She was acquired before I came here in the fall of 2017  and was worked on by a few students before me 
( IDK know who exactly but ask Tom, may cost you a dollar ). She also has a springRC sm-s3317R full rotation servo motor
along with a dropper mechanism I designed and was printed by Dr. Phong Le. 
2 of the motors I have altered and drawn on to measure rotation and one is brand new.

~~~~~~~~~~~~~~~~~~~~~~~~ What is in this directory ~~~~~~~~~~~~~~~~~~~~~~

In here you will obviously find this file your reading ( duh ), photos of my math, sketches that I made on tinkercad, and what ever else I found relevant 
that wasn't code. This directory is supposed to help you pick up where I left off and finish this project.
Everything is also on my github: https://github.com/RivenTheExile1/IrisSeniorProject.
If you do have any more questions or want further insight my email address is: connor.a.ferwerda@gmail.com. 
I will gladly help since this drone and Dr.Kelliher were the only things I liked about this college and I would love to see Iris fly.

~~~~~~~~~~~~~~~~~~~~~~~ Purpose of this file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is supposed to contain notes and info that may aid you in your flying and fixing of Iris. 
( Yes she does need to be fixed. sorry thats my fault. ) 

~~~~~~~~~~~~~~~~~~~~~~ History ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I know of nothing of what happened to Iris before I got here. I was given 3 .py files. These files are: Flying/dronetest.py, 
Flying/dronetest3.py, and Flying/drontest5.py. There may be one ore two I have forgotten, If I did, I am sure Tom will find me and
hit me with the board of education ( if you don't know what the board of education is yet, you either got hit so hard you don't remember
or haven't met her yet.).  

****BEGGINNG OF IMPORTANT NOTE******
All the python files and repositories use python2. This will be annoying because support for python2 was starting to be dropped in spring of 2021. 
When you are coding or using libraries make sure they are python2.
****END OF IMPORTANT NOTE*********

When I picked up this drone in the spring for 2019 ( my sophomore year ). She was flying perfectly ( Yet again sorry for crashing her ). 
I made my own two files Flying/Drone_test_search_v.2.py and Flying/Drone_test_search_v.3.py. The v.2 file is the file I ran that crashed
Iris and I don't remember the v.3 version working.
The purpose of these files are stated in the top of each one respectively 

During the fall of 2019 ( first semester junior year ). My goal was to fix the broken parts of Iris after her crash. If I remember correctly,
Iris had a few broken propellers, a broken arm or tow, and a few of the wires connecting to the motors were messed up. During this semester 
I fixed these issues. At the start of 2020, there was not much I worked on besides more cosmetic fixes. 
This semester how ever was cut short due to Covid-19. I then worked on the dropping mechanism for Iris in the fall of 2020 
and did not touch her physically again till the spring of 2021.
At the start of my senior project I had these files that I coded for the motor: Motor/Servotest.py, Motor/Old_servo_motor_test_v1.py
and the aforementioned files in Flying.

~~~~~~~~~~~~~~~~~~~~~~~~ My senior project ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I worked on a bit during my senior project. I am gonna break this section in to 6 subsections, 
Flying, vision, motor, simulation, all together and hardware. Lets start with....

~~~~~~~~~~~~~~~~~~~~~~~~ Hardware ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you open Iris up you will notice that there is a poor soldering job on one of the motors to the PCM board. 
At the start of my spring senior semester I was trying to arm and get Iris's motors to spin. I did but when using the controller only a few would
and they would not spin continuously. I thought that the motor or PCM board were broken. So I de-soldered de-soldered one of the motors and 
re-soldered a new one. The problem was actually that I didn't give Iris enough power when flying her with the controller. 
She also has a few ziptie's on her.  This is because the black bars you will see on some arms can come off,
but are hard as hell to put back on so......... zipties. Thats particularly it when it comes to what hardware modifications I made.

~~~~~~~~~~~~~~~~~~~~ Vision ~~~~~~~~~~~~~~~~~~~~~~~~~

Iris actually came with a thermal camera. During the fall of 2020 I had a rgb camera and Dr.Kelliher and I decided it would be better to use that
and look for a colored target. Image blobbing isn't too hard to compute. While my code is super simple, it works! In the /Vision you find: Blob3_11,
Drone_Blob4_15, Old_Blob3_8, Old_Blobv2, Old_cambimag3_17_21, Old_ImageBlobbing, Old_VIB_v1_10_06, not all of these files are relevant ( Some are actually empty....)

Old_VIB_v1_10_06, Old_ImageBlobbing, and Old_Blobv2 are empty or are a few  lines of code. They are still in here because I wanted to keep all files I toucher when working 
on my senior project or related to it. You can completely ignore these files if you want.
Old_cambimag3_17_21 was an older version of vision processing from Cambridge. I think it required python3 so I stopped using it.
Blob3_11 will not only does the image blobbing but will also display to the screen what the camera sees. 
Drone_Blob4_15 does the same exact thing as Blob3_11 with out the display. this is because you need another program or something when you 
ssh in to the pi to see the image and i just didn't care to do that.
Old_Blob3_8 does almost the same thing as 3_11 minus a couple print statements.

~~~~~~~~~~~~~~~ Simulation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this there is a simple pygame program that just simulates iris looking for a blue square in a snake pattern. I honestly didn't use much of 
this code in my final files. You can ignore if you want.

~~~~~~~~~~~~~~~~~~~~~~ Motor ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Old_servo_motor_test_v1 is an old file that really doesnt do alot. I don't remember what it does actually or even if it works for
the motor we are using now. Sometimes servos can be super annoying and there are different libraries that just make some servos work and some don't. 
ServoTest is the file that actually works ( with the aforementioned servo. and can turn to certain degrees )
As you will see there is a file that I made in tinkercad that shows how the dropping mechanism that I designed.
Its not to hard to see how it works, one of the parts cover the well and the well is connected to the motor and turns.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Flying ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So as I have stated before that I was handed dronetest, dronetest3, and drontest5. dronetest5 is the only one that have run before and it runs the 
drone in a 20 x 20 feet square. This code runs perfectly I don't know about the other. The first code I wrote was Drone_test_search_v.2

Drone_test_search_v.2's base is very similar to dronetest5. Drone_test_search_v.2 tells the drone to move in a snake pattern instead of a square. 
Drone_test_search_v.2 was the code that was running when the drone crashed. I believe that I fixed the file after it crashed and it should be working 
fine. but don't bet your money on it. Drone_test_search_v.3 is very similar to v.2 but i can't figure out what is really different about it.
But since its quiet similar to v.2. You may not want to run it....

hello_drone and up_down are two files to just see if the drone can turn on and can go up and down respectively.  You can find the file 
hello_drone in dronekit's documentation  https://dronekit-python.readthedocs.io/en/latest/. ( This is just the generic link to the library ). 

I was not able to get Iris to fly before my senior project was complete. 

~~~~~~~~~~~~~~~~~~~~~~~~ All Together ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So as you can see there is a directory called All_together. The directory contains everything that is necessary for the drone to run. All these files
are supposed to be in their final forms. AT_Blob3_11 is the essential the same as Vision/Blob3_11. There is also a similar version of this file in 
all_together. Iris_vision_simulation is also the same as the samely named file in the simulation directory.

the all_together file is the code I would run to make the drone search in a square, scan for blue along the way, and if it finds the blue go to it.
If it doesn't find the blue then it will just land after completing the square. This file should be well commented but if you do have any questions
don't be afraid to contact me.

~~~~~~~~~~~~~~~~~~~~~~~~~~ Where I left off ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So when I tried to fly Iris the final time I ran Iris using code I was getting an error that the heartbeat doesn't exist. 
This will make the code timeout. I found some documentation that said to update firmware using
Qgroundcontrol http://qgroundcontrol.com/ and that didn't seem to work. 
I was also was using APMPlanner2 to check on the values that the drone was giving me and I couldn't get anything meaningful. 
You can connect Iris to your computer using a usb to micro-usb.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

That seems to be everything I can think of. 

Thank you,
Connor F.
