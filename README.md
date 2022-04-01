# Floof - An Interactive Toy
A toy created with a Raspberry Pi 4B, a micro:bit and an associated iPad app, designed to keep children off screens.

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/92370926/161159538-84e4c866-3736-40bc-93b5-753e501ab385.png">


## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General Info
The project consists of a toy that provides interactive activities to children in the 4-9 yr age group. Research indicates that children in this age group spend an alarmingly increasing amount of time on screens per day. Floof is designed to pull children away from screens by engaging them in interesting activities when at times set by parents or when time limits have been reach, including fun facts to foster learning, friendly chatter, and a dance activity to encourage physical movement. The toy is designed to emit a glow from its belly when interacting with the child and when combined with its speech show a warmth towards the user.

## Technologies
The project has 2 components:

### The toy:
Hardware:
* Raspberry Pi 4B
* BBC micro:bit V2
* Sense Hat (accelerometer and LED Matrix)
* Bluetooth Speaker
* Servos

Software:
* Python 3.8.9
* JavaScript

Libraries:
* SenseHat 2.2.0 - to program the sense Hat
* Flask - to implement a web server on the Pi
* pydub 0.25.1 - for playing audio files (pip install pydub)
* Serial - for serial connection with the micro:bit

### The iOS App:
Software:
* XCode 13.2.1 (IDE)
* Swift 5

## Setup
To run this project,
* Clone the 'Floof' code onto the Raspberry Pi. 
* Install the latest version of the hex file (v1) to the micro:bit.
* Install the iOS app on an iPad or run it in the simulator.
* Connect the Sense Hat to the Raspberry Pi. 
* Connect the micro:bit to the Pi using a micro USB cable. 
* Connect servos to the pins P0, P1 and P2 of the micro:bit. 
* Pair and connect a Bluetooth speaker to the Pi.
