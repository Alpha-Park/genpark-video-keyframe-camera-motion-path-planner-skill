from client import VideoKeyframeCameraMotionPathPlannerClient

def main():
    client = VideoKeyframeCameraMotionPathPlannerClient()
    res = client.plan_camera_motion_path('Mountain flight', 'FORWARD_SWEEP', 4.0)
    print('Video Camera Motion Planner: ' + res['motion_plan_id'] + ' (' + res['camera_trajectory'] + ')')
    print('Keyframes: ' + str(res['total_keyframes']) + ' frames | Interpolation: ' + res['smoothness_interpolation'])
    print('Trajectory URL: ' + res['trajectory_visualization_url'])

if __name__ == '__main__':
    main()
