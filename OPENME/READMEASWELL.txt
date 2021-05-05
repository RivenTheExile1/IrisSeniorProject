To whom ever reads this,

Hello. My name is Connor Ferwreda. I am curretnly a senior in my final days of my spring 2021 semester. If you are reading this than you are 
continuing where I left off on Iris. In this doc, I will explain what Iris is, where I left off, what I have done, and much, much more. Get a 
good cup of tea ( my favorite is chamomile, or earl grey ) and indulge me in this trip.

~~~~~~~~~~~~~~~~~~~~ What is Iris? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Iris is a quadcopter drone engineered by 3DR robitics. She has a pixhawk2 navigational system that is atached to a raspberry pi zero w and 
rgb picamera that fits the zero w camera port ( some cameras modules don't fit to the zero w and the standard pis fyi ). 
She was aquired before I came here in the fall of 2017  and was worked on by a few students before me 
( IDK know who exactly but ask Tom, may cost you a dollar ). She also has a springRC sm-s3317R full rotaion servo motor
along with a dropper mechanism I designed and was printed by Dr. Phong Le. 
2 of the motors I have altered and drawn on to measure rotation and one is brand new.

~~~~~~~~~~~~~~~~~~~~~~~~ What is in this directory ~~~~~~~~~~~~~~~~~~~~~~

In here you will obviously find this file your reading ( duh ), photos of my math, sketches that I made on tinkercad, and what ever else I found relevant 
that wasn't code. This directory is supposed to help you pick up where I left off and finish this project.
Everything is also on my github: https://github.com/RivenTheExile1/IrisSeniorProject.
If you do have any more questions or want further insight my email address is: connor.a.ferwerda@gmail.com. 
I will gladly help since this drone and Dr.Kelliher were the only things I liked about this college and I would love to see Iris fly.
I digress.

~~~~~~~~~~~~~~~~~~~~~~~ Purpose of this file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is supposed to contain notes and info that may aid you in your flying and fixing of Iris. 
( Yes she does need to be fixed. sorry thats my fault. ) 

~~~~~~~~~~~~~~~~~~~~~~ History ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I konw of nothing of what happened to Iris before I got here. I was given 3 .py files. These files are: Flying/dronetest.py, 
Flying/dronetest3.py, and Flying/drontest5.py. There may be one ore two I have forgotten, If I did, I am sure Tom will find me and
hit me with the board of education ( if you don't know what the board of education is yet, you either got hit so hard 
or haven't met her yet.).  

****BEGGINNG OF IMPORTANT NOTE******
All the python files and repositories use python2. This will be annoying because support for python2 was starting to be dropped in spring of 2021. 
When you are coding or using libraries make sure they are python2.
****END OF IMPORTANT NOTE*********

When I picked up this drone in the spring fo 2019 ( my sophmore year ). She was flying perfectly ( Yet again sorry for crashing her ). 
I made my own two files Flying/Drone_test_search_v.2.py and Flying/Drone_test_search_v.3.py. The v.2 version worked perfectly. 
The v.3 version did not and was the file that was running when Iris crashed.
The purpose of these files are stated in the top of each one respectively 

During the fall of 2019 ( first semester junior year ). My goal was to fix the borken parts of Iris after her crash. If I remember correctly,
Iris had a few broken propellers and a few of the wires connecting to the motors were messed up. During this semester I fixed these issues.
At the start of 2020, there was not much I worked on besides more cosmetic fixes. This semester how ever was cut short due to Covid-19.
I then worked on the dropping mechanism for Iris in the fall of 2020 and did not touch her physically again till the spring of 2021.
At the start of my senior project I had these files that I coded for the motor: Motor/Servotest.py, Motor/Old_servo_motor_test_v1.py
and the aforementioned files in Flying.

~~~~~~~~~~~~~~~~~~~~~~~~ My senior project ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I worked on a bit during my senior project. I am gonna break this section in to 6 sections, 
Flying, vision, motor, simulation, all together and hardware. Lets start with....

~~~~~~~~~~~~~~~~~~~~~~~~ Hardware ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you open Iris up you will notice that there is a poor soldering job on one of the motors to the PCM board. 
At the start of my spring senior semester I was trying to arm and get Iris's motors to spin. I did but when using the controller only a few would
and they would not spin continiously. I thought that the motor or PCM board were broken. So I de-soldered and re-soldered one of the motors.
The problem was actually that I didn't give Iris enough power when flying her with the controller. She also has a few ziptie's on her. 
This is because the black bars you will see on some arms can come off, but are hard as hell to put back on so......... zipties. 
Thats particularly it when it comes to what hardware modifactions I made.

~~~~~~~~~~~~~~~~~~~~ Vision ~~~~~~~~~~~~~~~~~~~~~~~~~

Iris actually came with a thermal camera. During the fall of 2020 I had a rgb camera and Dr.Kelliher and I decided it would be better to use that
and look for a colored target. Image blobbing isn't too hard to compute. While my code is super simple, it works! In the /Vision you find: Blob3_11, drone




 
