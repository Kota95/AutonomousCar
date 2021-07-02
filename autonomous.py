import cv2
import numpy as np
import matplotlib.pyplot as plt 
import keyboard


class autonomous:

    def __init__(self,frame): 
       
        self.frame = frame
        self.height = self.frame.shape[0]
        self.width = self.frame.shape[1]

    def coordinates(self,image,line):
     try:
        y1 = image.shape[0]
        y2 = 0

        x1 = int((y1-line[1])/line[0])
        x2 = int((y2-line[1])/line[0])

        return [(x1,y1),(x2,y2)]
     except:
         return None

    def canny_image_cvt(self,frame):

        self.gray_scale_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        self.blurred_image_gaussian = cv2.GaussianBlur(self.gray_scale_image, (5,5), 0)
        self.canny_image = cv2.Canny(self.blurred_image_gaussian, 100, 200)  #note
        return self.canny_image
    
    def region_of_intrest(self):

        self.polygons = np.array([[(0,475),(150,250),(750,250),(self.width,475)]])
        self.region = np.zeros_like(self.frame)
        self.region_of_interest_image = cv2.polylines(self.frame, self.polygons, True, [0,0,255], 10) #note
        return self.region_of_interest_image

    def bird_eye_view(self):

        self.bird_eye_view_input_points = np.float32([(0,475),(150,250),(750,250),(self.width,475)]) #note
        self.bird_eye_view_output_points = np.float32([(0, self.height),(0, 0),(self.width, 0),(self.width,self.height)])
        self.bird_eye_view_transform = cv2.getPerspectiveTransform(self.bird_eye_view_input_points, self.bird_eye_view_output_points)
        self.bird_eye_view_image = cv2.warpPerspective(self.frame,self.bird_eye_view_transform,(self.width,self.height),flags = cv2.INTER_LINEAR)
        return self.bird_eye_view_image

    def lane_lines(self):
        
        frame = self.canny_image_cvt(self.bird_eye_view()).astype('uint8')
        self.lines = cv2.HoughLinesP(frame,2,np.pi/90,50,np.array([]),minLineLength=5,maxLineGap=5)
        self.left_lines = []
        self.right_lines = []
        
        for line in self.lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1,x2),(y1,y2),1)
            slope = parameters[0]
            intercept = parameters[1]

            if slope<0:
                self.left_lines.append((slope,intercept))
            else:
                self.right_lines.append((slope,intercept))

        self.left_average_slope_intercept = np.average(self.left_lines, axis = 0)
        self.right_average_slope_intercept = np.average(self.right_lines, axis = 0)

        self.left_final = self.coordinates(frame,self.left_average_slope_intercept)
        self.right_final = self.coordinates(frame,self.right_average_slope_intercept)

        if self.left_final != None or self.right_final != None:
            self.final_lines = np.float64(np.array([self.left_final+self.right_final]))

            self.lane_lines_image = cv2.line(self.bird_eye_view_image,self.left_final[0],self.left_final[1],[255,0,0], 10)
            self.lane_lines_image = cv2.line(self.lane_lines_image,self.right_final[0],self.right_final[1],[255,0,0], 10)

            return self.lane_lines_image
        
        else: 
            return self.frame

    def follow_lane_lines(self):

  
        self.x_average = []
        for i in range(0,601):
            x_left = (i - self.left_average_slope_intercept[1])/self.left_average_slope_intercept[0]
            x_right = (i - self.right_average_slope_intercept[1])/self.right_average_slope_intercept[0]
            self.x_average = self.x_average + [(x_left + x_right)/2]
        self.x = np.array(self.x_average)
        self.path_slope = -(600/(self.x[0]-self.x[599]))
        print(self.path_slope)
        
        if keyboard.is_pressed('n'):
            if self.path_slope > 10:
                return 'a'
            elif self.path_slope < 0:
                return 'd'
            else:    
                return 'w'
            
        else:
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
            return target_data






if __name__ == "__main__":
    pass