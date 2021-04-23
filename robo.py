def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.5)
    gimbal_ctrl.pitch_ctrl(10)
#chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
print("program start")
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,2.39)
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
gimbal_ctrl.recenter()
print("Entering Room !")
#vision_recognized_marker(msg)
#if vision_recognized_marker_number_one(msg) == True
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
gimbal_ctrl.recenter()
chassis_ctrl.move_with_distance(0,1.3)
#vision_recognized_marker_F(msg)
#if vision_recognized_marker_letter_F(msg):
chassis_ctrl.move_and_rotate_with_degree(0,180)
gimbal_ctrl.recenter()
chassis_ctrl.move_and_rotate_with_degree(0,-180)
gimbal_ctrl.recenter()
media_ctrl.play_sound(rm_define.media_sound_recognize_success, wait_for_complete_flag=True)
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
#vision_ctrl.enable_detection(rm_define.vision_detection_people) 
#gimbal_ctrl.yaw_ctrl(-250)
#gimbal_ctrl.yaw_ctrl(250)
chassis_ctrl.move_with_distance(-180,1.3)
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
chassis_ctrl.move_with_distance(0,4.7)
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,270)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,2)
chassis_ctrl.rotate_with_degree(rm_define.clockwise,-45)
chassis_ctrl.move_with_distance(0,2.5)
chassis_ctrl.rotate_with_degree(rm_define.clockwise,-45)
chassis_ctrl.move_with_distance(0,3.3)
#chassis_ctrl.move_with_distance(0,) 
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,5)




 
chassis_ctrl.move_with_distance(0,2)
 


 
 
 
 
 
#Add scan for fire\