import pyautogui
import time
import cv2
from PIL import ImageGrab
import numpy as np
import os



pyautogui.FAILSAFE = True

#time.sleep(5)

#pyautogui.keyDown('up')
#pyautogui.keyUp('up')

#print(pyautogui.position())

#for _ in range(5) : 
    #pyautogui.move(-100 , 0)
    #time.sleep(0.5)
    #pyautogui.move(100  , 0)



#pyautogui.keyDown('up')
#i = 0
#frames = 0
while True : 
    screen = np.array(ImageGrab.grab(bbox =(0 , 40 , 710 , 770)))


    gray = cv2.cvtColor(screen , cv2.COLOR_BGR2GRAY)

    #gray = cv2.rectangle(gray , (335 , 281) , (405 , 351) , (0,255,210) , 2) #(335 , 281) , (405 , 351)

    clipped = gray[312:352 , 350:390]
    
    #if i>= frames : 
    for x in clipped : 
                
            
                    m = int(min(x))
                    if m == 83 : 
                        #i = 0
                        #print('jump dino!')

                       

                        pyautogui.keyDown('up')
                        time.sleep(0.005)
                        pyautogui.keyUp('up')

                        ''' time.sleep(0.065)

                        pyautogui.keyDown('down')
                        time.sleep(0.03)
                        pyautogui.keyUp('down')'''


                        #os.system('cls')
                        break

    #i += 1

           

        
            
           

    
           

    cv2.imshow('window',gray)
    if cv2.waitKey(25) & 0xFF == ord('q') : 
        cv2.destroyAllWindows()
        break

  