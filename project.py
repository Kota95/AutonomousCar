from vidgear.gears import NetGear
import cv2
import keyboard 
import numpy as np
import matplotlib.pyplot as plt
from autonomous import autonomous

options = {'bidirectional_mode': True} 
client = NetGear(address = '192.168.0.19', port = '5757', protocol = 'tcp',  pattern = 1, receive_mode = True, logging = True, **options)

manual = True
target_data = 'no'

while True:


    try:

        data = client.recv(return_data = target_data)
        target_data = 'no'


        if data is None:
            break

        server_data, frame = data
        
        if frame is None:
            break

        frame = cv2.flip(frame, 1)

        if not(server_data is None): 
                print(server_data)

        if manual == True:

            if keyboard.is_pressed('i'):
                target_data = 'i'
            elif keyboard.is_pressed('j'):
                target_data = 'j'
            elif keyboard.is_pressed('k'):
                target_data = 'k'
            elif keyboard.is_pressed('l'):
                target_data = 'l'
            elif keyboard.is_pressed('w'):
                target_data = 'w'
            elif keyboard.is_pressed('a'):
                target_data = 'a'
            elif keyboard.is_pressed('s'):
                target_data = 's'
            elif keyboard.is_pressed('d'):
                target_data = 'd'
            else:
                target_data = 'no'

            car = autonomous(frame)
            bev = car.bird_eye_view()
            roi = car.region_of_intrest()

            cv2.imshow("Output Frame", frame)
            cv2.imshow("Bird Eye View Frame", bev)


            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            if keyboard.is_pressed('b'):
                cv2.imwrite('test_image2.jpg',frame)

            if keyboard.is_pressed('t'):
                plt.imshow(frame)
                plt.show()

            
        else:

            car = autonomous(frame)
            region_of_intrest = car.region_of_intrest()
            lane_lines = car.lane_lines()

            cv2.imshow("Region of Intrest", region_of_intrest)
            cv2.imshow("Lane Lines", lane_lines)

            target_data = car.follow_lane_lines()

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    
        if keyboard.is_pressed("m"):

            manual = not manual

    except KeyboardInterrupt:
        break

cv2.destroyAllWindows()
client.close()