# Writeup: Track 3D-Objects Over Time

Please use this starter template to answer the following questions:

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?

## Tracking
* Line 112 in filter.py uses meas.sensor.get_H(x) instead of meas.sensor.get_h(x) in the update function.
* Line 138 in filter.py uses meas.sensor.get_h(x) in the gamma function to compute the residual.
* ![](1_RMSE_tracking.png)

## Track Management
* Line 123 in trackmanagement.py should reduce track score. However, track 0 is never deleted.
* ![](2_RMSE_track_management.png)

## Data Association
* 

## Sensor Fusion

### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 


### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?


### 4. Can you think of ways to improve your tracking results in the future?

