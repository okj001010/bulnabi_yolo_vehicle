# Requirements

1. v4l2_camera

   ```
   sudo apt update
   sudo apt install ros-${ROS_DISTRO}-v4l2-camera
   ```

2. (Optional) v4l2-ctl: change v4l2_camera settings

   ```
   sudo apt install v4l-utils

   v4l2-ctl -d /dev/video0 --list-formats-ex   # camera formats 확인
   v4l2-ctl -d /dev/video0 --set-fmt-video=width=640,height=480   # change settings
   ```

# Build

```
colcon build --symlink-install --packages-select my_bboxes_msg       // cbp my_bboxes_msg
colcon build --symlink-install                                       // cba
source ./install/local_setup.bash
```

# Run

```
ros2 launch yolo_detection yolo_detector.launch.py
```
