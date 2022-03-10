#SCANNING FUNCTION

marker_value = None
person_value = None

def vision_recognized_marker_number_one(msg):
    global marker_value
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_value = 1
    gimbal_ctrl.recenter()

def vision_recognized_marker_number_two(msg):
    global marker_value
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_value = 2
    gimbal_ctrl.recenter()
    
def vision_recognized_marker_number_three(msg):
    global marker_value
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_value = 3
    gimbal_ctrl.recenter()

def vision_recognized_marker_letter_F(msg):
    global marker_value
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_value = "F"
    gimbal_ctrl.recenter()

def vision_recognized_people(msg):
    global person_was_detected
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    person_was_detected = True
    print("Person Detected!")

def scanning():
    global marker_value
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_value = None
    while marker_value == None:
        gimbal_ctrl.yaw_ctrl(-250)
        gimbal_ctrl.yaw_ctrl(250)
        

    if(marker_value == 1):
        print("Marker 1 Found!")

    elif(marker_value == 2):
        print("Marker 2 Found!")
    
    elif(marker_value== 3):
        print("Marker 3 Found!")

    elif(marker_value == "F"):
        print("Fire Found!")

def scanning_for_people():
    global person_was_detected
    print("SCANNING FOR PEOPLE!")
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_was_detected = False
    gimbal_ctrl.pitch_ctrl(35)

    while person_was_detected == False:
        gimbal_ctrl.yaw_ctrl(250)
        gimbal_ctrl.yaw_ctrl(-250)
        
        
    
    if(person_was_detected == True):
        print("Person was detected!")
        media_ctrl.play_sound(rm_define.media_sound_attacked, wait_for_complete=True)
 
def scanning_for_fire():
    print("SCANNING FOR FIRE")
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    led_ctrl.gun_led_on()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    led_ctrl.gun_led_off()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)


    


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    time.sleep(3)
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
    
    chassis_ctrl.set_trans_speed(1)
    gimbal_ctrl.pitch_ctrl(10)

    print("program start")
    chassis_ctrl.move_with_distance(0,5)

    chassis_ctrl.move_with_distance(0,2.39)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    time.sleep(3)
    scanning()
    
    if(marker_value == 1):
        print("Enter room")

        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(3)
        scanning_for_fire()
        chassis_ctrl.move_with_distance(0,1)
        gimbal_ctrl.recenter()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45)
        chassis_ctrl.move_with_distance(0,2.4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,47)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,1)
        time.sleep(10)
        chassis_ctrl.move_with_distance(0,4.65)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        time.sleep(3)
    elif (marker_value == 2):
        print("Skip room")
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45)
        chassis_ctrl.move_with_distance(0,2.4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,47)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,1)
        time.sleep(10)
        chassis_ctrl.move_with_distance(0,4.65)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        time.sleep(3)
    elif(marker_value == 3):
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(3)
        scanning_for_people()
        
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.39)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.39)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45)
        chassis_ctrl.move_with_distance(0,2.4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,47)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,1)
        time.sleep(10)
        chassis_ctrl.move_with_distance(0,4.65)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        time.sleep(3)
        
    scanning()
    if (marker_value == 1):
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        gimbal_ctrl.recenter()
        scanning_for_fire()
        time.sleep(3)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        gimbal_ctrl.recenter()


    elif (marker_value == 2):
        print("Skip room")
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    elif (marker_value == 3):
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        scanning_for_people()
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        gimbal_ctrl.recenter()

        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.39)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4.0)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45)
        
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,47)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,1)
        time.sleep(10)
        chassis_ctrl.move_with_distance(0,4.65)
        time.sleep(3)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        # room 3
    scanning()
    if (marker_value == 1):
        chassis_ctrl.move_with_distance(0,2.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.2)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        
        time.sleep(3)
        scanning_for_fire()
        
        
        
        chassis_ctrl.move_with_distance(0,1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,2.7)
        gimbal_ctrl.recenter()
        
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    elif (marker_value == 2):
        print("Skip Room")
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

    elif (marker_value == 3):
        chassis_ctrl.move_with_distance(0,3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.5)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        gimbal_ctrl.recenter()
        time.sleep(3)
        scanning_for_people()
        
        
        chassis_ctrl.move_with_distance(0,1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()

        #Bringing person home from door #3

        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
        chassis_ctrl.move_with_distance(0,2.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
        
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,3.5)
    
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        gimbal_ctrl.recenter()

        #Moving to door 4
    
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.39)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,45)
        chassis_ctrl.move_with_distance(0,1.1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,47)
        gimbal_ctrl.recenter()
        time.sleep(10)

        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.move_with_distance(0,5)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        

        #room #4
        
    scanning()
    if (marker_value == 1):
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.move_with_distance(0,1.5)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        gimbal_ctrl.recenter()
        time.sleep(3)


        scanning_for_fire()
        chassis_ctrl.move_with_distance(0,1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        gimbal_ctrl.recenter()
        time.sleep(3)
        #Going home from door 4


        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        time.sleep(10)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
        chassis_ctrl.move_with_distance(0,1.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(3)
        gimbal_ctrl.recenter()

    
    elif (marker_value == 2):
        print("Skip room")
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
        chassis_ctrl.move_with_distance(0,2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(3)
        gimbal_ctrl.recenter()
        

    elif (marker_value == 3):

        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0,1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

        scanning_for_people()

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0,1.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)

        #Going home from door 4


        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,47)
        chassis_ctrl.move_with_distance(0,1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,45)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3.5)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,2.5)
        chassis_ctrl.move_with_distance(0,3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
        time.sleep(3)
        gimbal_ctrl.recenter()