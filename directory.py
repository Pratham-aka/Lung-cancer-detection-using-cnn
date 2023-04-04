import os
main_dir = "C:\\Users\\pratham sharma\\Desktop\\Pose detection"
dir_train = os.path.join(main_dir,'train')
dir_val = os.path.join(main_dir,'val')
dir_grab = os.path.join(main_dir,'grab_dataset')

dir_handshake = os.path.join(dir_train,'handshake') 
dir_sitting = os.path.join(dir_train,'sitting')
dir_standing = os.path.join(dir_train,'standing')
dir_walking = os.path.join(dir_train,'walking')

os.mkdir(dir_train)
os.mkdir(dir_test)
os.mkdir(dir_sitting)
os.mkdir(dir_standing)
os.mkdir(dir_walking)
os.mkdir(dir_handshake)


