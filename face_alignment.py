import cv2
import mediapipe as mp

img = cv2.imread("1.jpeg")

input_data = {
    "eye_left": [],
    "eye_right": [],
    "nose": [],
    "mouth": []
}
points = [2, 6, 33, 61, 131, 133, 146, 175, 291, 263, 275, 360, 362]
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(static_image_mode=True, max_num_faces=1,
                               min_detection_confidence=0.5)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)


def face_alignment(data):
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = faceMesh.process(imgRBG)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id2, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                if id2 in points:
                    print(id2, x, y, )
                    img = cv2.circle(img, (x, y), 1, (0, 0, 255), 4)

    # This grabs the rightmost and leftmost points on the eyes
    # 이것은 눈의 가장 오른쪽과 가장 왼쪽의 점을 잡는다
    #
    # More facial details can be added by using the following landmarks:
    # https://github.com/tensorflow/tfjs-models/blob/838611c02f51159afdd77469ce67f0e26b7bbb23/face-landmarks-detection/src/mediapipe-facemesh/keypoints.ts
    input_data["eye_left"].append((results.multi_face_landmarks[0].landmark[33].x,
                                   results.multi_face_landmarks[0].landmark[33].y))
    input_data["eye_left"].append((results.multi_face_landmarks[0].landmark[133].x,
                                   results.multi_face_landmarks[0].landmark[133].y))

    input_data["eye_right"].append((results.multi_face_landmarks[0].landmark[263].x,
                                    results.multi_face_landmarks[0].landmark[263].y))
    input_data["eye_right"].append((results.multi_face_landmarks[0].landmark[362].x,
                                    results.multi_face_landmarks[0].landmark[362].y))

    input_data["nose"].append((results.multi_face_landmarks[0].landmark[2].x,
                               results.multi_face_landmarks[0].landmark[2].y))
    input_data["nose"].append((results.multi_face_landmarks[0].landmark[6].x,
                               results.multi_face_landmarks[0].landmark[6].y))
    input_data["nose"].append((results.multi_face_landmarks[0].landmark[131].x,
                               results.multi_face_landmarks[0].landmark[131].y))
    input_data["nose"].append((results.multi_face_landmarks[0].landmark[360].x,
                               results.multi_face_landmarks[0].landmark[360].y))

    input_data["mouth"].append((results.multi_face_landmarks[0].landmark[61].x,
                                results.multi_face_landmarks[0].landmark[61].y))
    input_data["mouth"].append((results.multi_face_landmarks[0].landmark[146].x,
                                results.multi_face_landmarks[0].landmark[146].y))
    input_data["mouth"].append((results.multi_face_landmarks[0].landmark[275].x,
                                results.multi_face_landmarks[0].landmark[275].y))
    input_data["mouth"].append((results.multi_face_landmarks[0].landmark[291].x,
                                results.multi_face_landmarks[0].landmark[291].y))

    cv2.imshow('', img)

    # Not required, this is just for testing
    # 필수는 아닙니다. 테스트용입니다
    # print(input_data["mouth"])
    # print("_______")
    # print(input_data["nose"])
    # print("_______")
    # print(input_data["eye_left"])
    # print("_______")
    # print(input_data["eye_right"])

    return input_data

    # cv2.imwrite('./output.jpg', )
