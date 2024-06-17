from scipy.spatial import distance as dist

def compute_ear(eye_points):
    A = dist.euclidean(eye_points[1], eye_points[5])
    B = dist.euclidean(eye_points[2], eye_points[4])
    C = dist.euclidean(eye_points[0], eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

def determine_gaze_direction(left_eye, right_eye):
    left_ear = compute_ear(left_eye)
    right_ear = compute_ear(right_eye)
    
    if left_ear < 0.21 and right_ear < 0.21:
        return "center"
    elif left_ear < right_ear:
        return "right"
    else:
        return "left"
