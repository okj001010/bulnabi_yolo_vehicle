import launch
import launch_ros.actions
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    yolox_ros_share_dir = get_package_share_directory('vehicle_controller')

    webcam = launch_ros.actions.Node(
        package="v4l2_camera", executable="v4l2_camera_node",
        parameters=[
            {"image_size": [640,480]},
        ],
    )

    yolo_detector = launch_ros.actions.Node(
        package="yolo_detection", executable="yolo_detector",

    )
    
    vehicle_controller = launch_ros.actions.Node(
        package="vehicle_controller", executable="vehicle_controller", 
	    parameters=[
            '~/ws_vehicle_controller/src/vehicle_controller/config/waypoint.yaml'
        ],
    )

    rqt_graph = launch_ros.actions.Node(
        package="rqt_graph", executable="rqt_graph",
    )



    return launch.LaunchDescription([
        webcam,
        yolo_detector,
        vehicle_controller,
    ])
