import RPi.GPIO as GPIO
import pigpio
from vidgear.gears import NetGear
from vidgear.gears import PiGear

options = {"hflip": True, "exposure_mode": "auto", "iso": 800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0}

stream = PiGear(resolution=(800, 600), framerate=60, logging=True, **options).start()

options = {'bidirectional_mode': True} 

server = NetGear(address = '192.168.0.19', port = '5757', protocol = 'tcp',  pattern = 1, logging = True, **options)

forwardpin = 17

backwardpin = 27

leftpin = 22

rightpin = 23

panpin = 12

tiltpin = 13

forward = pigpio.pi()

backward = pigpio.pi()

left = pigpio.pi()

right = pigpio.pi()


pan = pigpio.pi()

pan.set_mode(panpin, pigpio.OUTPUT)

pan.set_PWM_frequency(panpin, 50)

tilt = pigpio.pi()

tilt.set_mode(tiltpin, pigpio.OUTPUT)

tilt.set_PWM_frequency(panpin, 50)

panpulsewidth = 1250

tiltpulsewidth = 1250

pan.set_servo_pulsewidth(panpin, panpulsewidth)

tilt.set_servo_pulsewidth(tiltpin, tiltpulsewidth)

while True:

    try: 

        frame = stream.read()


        if frame is None:

            break

        target_data = 'Video Received'

        recv_data = server.send(frame, message = target_data)



        if not(recv_data is None): 

            print(recv_data)

        if recv_data == 'no':

            forward.write(forwardpin, 1)

            backward.write(backwardpin, 1)

            left.write(leftpin, 0)

            right.write(rightpin, 0)

        if recv_data == 'w':

            forward.write(forwardpin, 1)

            backward.write(backwardpin, 0)

            left.write(leftpin, 0)

            right.write(rightpin, 0)


        if recv_data == 's':

            forward.write(forwardpin, 0)

            backward.write(backwardpin, 1)

            left.write(leftpin, 0)

            right.write(rightpin, 0)

        if recv_data == 'a':


            forward.write(forwardpin, 0)

            backward.write(backwardpin, 0)

            left.write(leftpin, 1)

            right.write(rightpin, 0)


        if recv_data == 'd':

            forward.write(forwardpin, 0)

            backward.write(backwardpin, 0)

            left.write(leftpin, 0)

            right.write(rightpin, 1)

        if recv_data == 'i':

            tiltpulsewidth = tiltpulsewidth - 50

            tilt.set_servo_pulsewidth(tiltpin, tiltpulsewidth)

        if recv_data == 'k':

            tiltpulsewidth = tiltpulsewidth + 50

            tilt.set_servo_pulsewidth(tiltpin, tiltpulsewidth)


        if recv_data == 'j':


            panpulsewidth = panpulsewidth + 50


            pan.set_servo_pulsewidth(panpin, panpulsewidth)

        if recv_data == 'l':

            panpulsewidth = panpulsewidth - 50

            pan.set_servo_pulsewidth(panpin, panpulsewidth)
    
    
        print(panpulsewidth,",",tiltpulsewidth)

    except KeyboardInterrupt:

        break

tilt.set_PWM_dutycycle(panpin, 0)

tilt.set_PWM_frequency(panpin, 0 )

pan.set_PWM_dutycycle(tiltpin, 0)

pan.set_PWM_frequency(tiltpin, 0 )

stream.stop()

server.close()