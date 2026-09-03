class VideoKeyframeCameraMotionPathPlannerClient:
    def plan_camera_motion_path(self, scene_description='A futuristic neon city at sunset', camera_movement='ORBIT_AND_DOLLY_ZOOM', duration_seconds=5.0):
        return {
            'motion_plan_id': 'cam_mot_8812',
            'scene_description': scene_description,
            'camera_trajectory': camera_movement,
            'total_keyframes': int(duration_seconds * 24),
            'keyframes_3d_spline': [
                {'t_sec': 0.0, 'cam_x': 0.0, 'cam_y': 10.0, 'cam_z': -50.0, 'fov_deg': 45.0},
                {'t_sec': 2.5, 'cam_x': 35.0, 'cam_y': 15.0, 'cam_z': -25.0, 'fov_deg': 52.0},
                {'t_sec': 5.0, 'cam_x': 50.0, 'cam_y': 5.0, 'cam_z': 0.0, 'fov_deg': 60.0}
            ],
            'smoothness_interpolation': 'BEZIER_EASE_IN_OUT',
            'trajectory_visualization_url': 'https://video.luma.genpark.ai/trajectories/8812.json'
        }
