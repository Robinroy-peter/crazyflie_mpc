from launch import LaunchDescription
from launch_ros.actions import Node
# import argparse



def generate_launch_description():
    return LaunchDescription([
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_1',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_2',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_3',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_4',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_5',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_6',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_7',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_8',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_9',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_10',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_11',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_12',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_13',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_14',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_15',
    ),
    Node(
        package='crazyflie_mpc',
        executable='crazyflie_multiagent_mpc',
        name='cf_16',
    ),
    ])