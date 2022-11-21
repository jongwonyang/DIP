input_data = {
    "eye_left": [
        (1.0, 3.0),
        (1.5, 3.5),
        (2.2, 3.9),
        (3.1, 4.1),
        (4.4, 4.1),
        (5.1, 3.7),
        (5.8, 3.2),
        (6.0, 2.7),
        (1.6, 2.6),
        (2.4, 2.3),
        (3.5, 2.0),
        (4.3, 2.1),
        (5.2, 2.3),
        (3.8, 4.2),
    ],
    "eye_right": [
        (1.0, 3.0),
        (1.5, 3.5),
        (2.2, 3.9),
        (3.1, 4.1),
        (4.4, 4.1),
        (5.1, 3.7),
        (5.8, 3.2),
        (6.0, 2.7),
        (1.6, 2.6),
        (2.4, 2.3),
        (3.5, 2.0),
        (4.3, 2.1),
        (5.2, 2.3),
        (3.8, 4.2),
    ],
    "nose": [
        (1.2, 1.4),
        (1.5, 2.2),
        (1.7, 2.9),
        (1.9, 3.6),
        (2.2, 4.4),
        (2.5, 5.1),
        (2.9, 4.7),
        (3.2, 3.9),
        (3.3, 3.1),
        (3.6, 2.2),
        (3.8, 1.6),
        (3.6, 1.0),
        (2.7, 1.0),
        (2.0, 1.0),
    ],
    "mouth": [
        (1.0, 2.0),
        (1.8, 2.7),
        (2.6, 3.0),
        (3.4, 3.0),
        (4.3, 2.7),
        (5.2, 3.0),
        (6.3, 2.7),
        (7.0, 2.0),
        (1.1, 1.6),
        (2.1, 1.4),
        (4.3, 1.1),
        (3.1, 1.1),
        (5.2, 1.1),
        (5.8, 1.4),
        (6.4, 1.6),
    ],
}
# 수평으로 정렬된 좌표여야 한다.
# Must be horizontally aligned coordinates.
# 좌표의 정밀도는 상관없다. (실수 범위)
# The precision of the coordinates does not matter. (real number range)
# 점의 갯수는 상관 없다. 
# The number of points does not matter.


def face_reading(data):
    # Return result or just print the result
    process_eye(data["eye_left"])


def process_eye(data):
    left = min(data, key=lambda x: x[0])
    right = max(data, key=lambda x: x[0])
    top = max(data, key=lambda x: x[1])
    bottom = min(data, key=lambda x: x[1])
    width = right - left
    height = top - bottom
    ratio = width / height
    # ratio
    # (봉황눈 > 용눈) > (호랑이 > 사자 > 학 > 공작) > 원앙 > 소 > 참새 (1.0)
    # 괄호 안은 left, right 의 높낮이로 비교
    # https://m.blog.naver.com/knk8884/220895457093
    # https://www.esquirekorea.co.kr/article/63686


def process_nose(data):
    pass


def process_mouth(data):
    pass


face_reading(input_data)
