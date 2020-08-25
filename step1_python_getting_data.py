import os
import pickle
import numpy as np
from scipy import io

with open('L20WVV215_20200527172601.pkl','rb') as loadf:
    data = pickle.load(loadf)
    
Steering_Wheel_Angle_ts5  = data['StrgWhlAngHSC2']['ts']
Steering_Wheel_Angle5  = data['StrgWhlAngHSC2']['value']
Steering_Wheel_Angle_Gradient_ts5 = data['StrgWhlAngGrdHSC2']['ts']
Steering_Wheel_Angle_Gradient5 = data['StrgWhlAngGrdHSC2']['value']

RDOT5 = data['RDircnIOHSC7']['ts']
RDO5 = data['RDircnIOHSC7']['value']
LDOT5= data['LDircnIOHSC7']['ts']
LDO5 = data['LDircnIOHSC7']['value']


io.savemat('Steering_Wheel_Angle_ts5', {'matrix': Steering_Wheel_Angle_ts5})
io.savemat('Steering_Wheel_Angle5', {'matrix': Steering_Wheel_Angle5})
io.savemat('Steering_Wheel_Angle_Gradient_ts5', {'matrix': Steering_Wheel_Angle_Gradient_ts5})
io.savemat('Steering_Wheel_Angle_Gradient5', {'matrix': Steering_Wheel_Angle_Gradient5})

io.savemat('RDOT5', {'matrix': RDOT5})
io.savemat('RDO5', {'matrix': RDO5})
io.savemat('LDOT5', {'matrix': LDOT5})
io.savemat('LDO5', {'matrix': LDO5})


