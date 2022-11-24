import cv2
import mediapipe as mp

faceDetails_eye_left = set()
faceDetails_eye_right = set()
faceDetails_nose = set()
faceDetails_mouth = set()

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)


def face_alignment(data):
 imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceMesh.process(imgRBG)

if results.multi_face_landmarks:
    for faceLms in results.multi_face_landmarks:
        mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS)

# This grabs the rightmost and leftmost points on the eyes
# 이것은 눈의 가장 오른쪽과 가장 왼쪽의 점을 잡는다
#
# More facial details can be added by using the following landmarks:
# https://github.com/tensorflow/tfjs-models/blob/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/src/mediapipe-facemesh/keypoints.ts
faceDetails_eye_left.add((results.multi_face_landmarks[0].landmark[33].x,
                        results.multi_face_landmarks[0].landmark[33].y))
faceDetails_eye_left.add((results.multi_face_landmarks[0].landmark[133].x,
                        results.multi_face_landmarks[0].landmark[133].y))

faceDetails_eye_right.add((results.multi_face_landmarks[0].landmark[263].x,
                        results.multi_face_landmarks[0].landmark[263].y))
faceDetails_eye_right.add((results.multi_face_landmarks[0].landmark[362].x,
                        results.multi_face_landmarks[0].landmark[362].y))

faceDetails_nose.add((results.multi_face_landmarks[0].landmark[2].x,
                        results.multi_face_landmarks[0].landmark[2].y))
faceDetails_nose.add((results.multi_face_landmarks[0].landmark[6].x,
                        results.multi_face_landmarks[0].landmark[6].y))
faceDetails_nose.add((results.multi_face_landmarks[0].landmark[131].x,
                        results.multi_face_landmarks[0].landmark[131].y))
faceDetails_nose.add((results.multi_face_landmarks[0].landmark[360].x,
                        results.multi_face_landmarks[0].landmark[360].y))

faceDetails_mouth.add((results.multi_face_landmarks[0].landmark[61].x,
                        results.multi_face_landmarks[0].landmark[61].y))
faceDetails_mouth.add((results.multi_face_landmarks[0].landmark[146].x,
                        results.multi_face_landmarks[0].landmark[146].y))
faceDetails_mouth.add((results.multi_face_landmarks[0].landmark[275].x,
                        results.multi_face_landmarks[0].landmark[275].y))
faceDetails_mouth.add((results.multi_face_landmarks[0].landmark[291].x,
                        results.multi_face_landmarks[0].landmark[291].y))

cv2.imshow('', img)

# Not required, this is just for testing
# 필수는 아닙니다. 테스트용입니다
print(faceDetails_mouth)
print("_______")
print(faceDetails_nose)
print("_______")
print(faceDetails_eye_left)
print("_______")
print(faceDetails_eye_right)

# cv2.imwrite('./output.jpg', )
k = cv2.waitKey(0)