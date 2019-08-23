import esp300, gauss460

from time import sleep

import numpy as np

esp = esp300.esp300(1, 0)
gauss = gauss460.gauss460(8,1)

while True:

    stepsize = float(input('stepsize: '))
    
    x = float(input('x coord: '))
    y = float(input('y coord: '))
    z = float(input('z coord: '))
    
    esp.axis1.pos = z
    
    sleep(1)
    esp.axis2.pos = x - stepsize / 2
    
    sleep(1)
    esp.axis3.pos = y
    
    sleep(1)
    field_x1 = gauss.allf()
    
    esp.axis2.pos = x + stepsize / 2
    
    sleep(1)
    field_x2 = gauss.allf()
    
    field_x2_diff = np.subtract(field_x2, field_x1) / (stepsize/10)
    
    esp.axis1.pos = z
    
    sleep(1)
    esp.axis2.pos = x 
    
    sleep(1)
    esp.axis3.pos = y - stepsize / 2
    
    sleep(1)
    field_y1 = gauss.allf()
    
    esp.axis3.pos = y + stepsize / 2
    
    sleep(1)
    field_y2 = gauss.allf()
    
    field_y2_diff = np.subtract(field_y2, field_y1) / (stepsize/10)
    
    grad_y = field_y2_diff[3] / np.mean((field_y1[3],field_y2[3]))
    grad_x = field_x2_diff[3] / np.mean((field_x1[3],field_x2[3]))
    
    print(np.sqrt(grad_x**2 + grad_y**2))
    
    input()
