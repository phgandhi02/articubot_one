import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
	robot_control = IncludeLaunchDescription(
	PythonLaunchDescriptionSource([os.path.join(
	get_package_share_directory('articubot_one'), 'launch'),
	'/launch_robot.launch.py'])
	)

	joystick = IncludeLaunchDescription(
	PythonLaunchDescriptionSource([os.path.join(
	get_package_share_directory('articubot_one'), 'launch'),
	'/joystick.launch.py'])
	)

	return LaunchDescription([
		robot_control,
		joystick
	])

