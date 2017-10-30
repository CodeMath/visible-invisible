"""
https://github.com/zplab/zbar-py
https://sourceforge.net/p/zbar/discussion/664595/thread/875f2242/
workon cv2
redis
src/redis-server
"""

import zbar

from PIL import Image
import cv2
"""
symbol.location[1]    symbol.location[3]
symbol.location[0]    symbol.location[2]
"""

"""
http://jybaek.tistory.com/575
slack bot
@qrcoder
1 hour => 5000 rate
1 min => 83.333 rate
1 sec => 1.3888 rate
"""
import time
import requests
import json

def main():

    capture = cv2.VideoCapture(0)
    
    while True:
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
        ret, frame = capture.read()

        

        cv2.imshow('Current', frame)

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', str(gray.data))


        
        scanner = zbar.ImageScanner()
        results = scanner.scan(zbar_image)
        
        for symbol in zbar_image:
            try:
                cen_x = (symbol.location[1][0] + symbol.location[3][0])
                cen_y = (symbol.location[0][1] + symbol.location[2][1])
                
                params = {
                    'x':cen_x/2 ,
                    'y':cen_y/2 ,
                }
                headers = {'Content-type': 'application/json; charset=utf-8', }
                requests.put('http://127.0.0.1:5000/stream', data=json.dumps(params), headers=headers)
                print "x: %s , y: %s" %(cen_x/2,cen_y/2)
            except:
                print "none"
            
                



if __name__ == "__main__":
    main()
    