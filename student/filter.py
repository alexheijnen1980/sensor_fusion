# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
from math import gamma
from multiprocessing import set_executable
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############

        # See lesson 6.7.

        dt = params.dt

        F = np.matrix([[1,0,0,dt,0,0],
                    [0,1,0,0,dt,0],
                    [0,0,1,0,0,dt],
                    [0,0,0,1,0,0],
                    [0,0,0,0,1,0],
                    [0,0,0,0,0,1]])

        return F
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        # See lesson 6.8.

        dt = params.dt
        q = params.q

        q_3 = (1/3) * dt**3 * q
        q_2 = (1/2) * dt**2 * q
        q_1 = dt * q

        Q = np.matrix([[q_3,0,0,q_2,0,0],
                    [0,q_3,0,0,q_2,0],
                    [0,0,q_3,0,0,q_2],
                    [q_2,0,0,q_1,0,0],
                    [0,q_2,0,0,q_1,0],
                    [0,0,q_2,0,0,q_1]])

        return Q
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        # See lesson 6.6.

        x = track.x
        P = track.P
        F = self.F()
        
        x = F * x # State prediction
        P = F * P * np.transpose(F) + self.Q() # Covariance prediction
        
        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        # See lesson 6.12.

        x = track.x
        P = track.P
        dim_state = params.dim_state

        H = meas.sensor.get_H(x)
        gamma = self.gamma(track, meas)
        S = self.S(track, meas, H)

        K = P * np.transpose(H) * np.linalg.inv(S) # Kalman gain
        x = x + K * gamma
        I = np.identity(dim_state)
        P = (I - K * H) * P

        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        # See lesson 6.12.

        z = np.matrix(meas.z)
        x = track.x
        H = meas.sensor.get_hx(x)

        gamma = z - H # Residual

        return gamma
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        # See lesson 6.12.

        P = track.P
        R = meas.R

        S = H * P * np.transpose(H) + R # Covariance of residual

        return S
        
        ############
        # END student code
        ############ 