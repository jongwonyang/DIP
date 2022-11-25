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
    # Jongwon
    # Return result or just print the result
    eye = process_eye(data["eye_left"])
    nose = process_nose(data["nose"])
    mouth = process_mouth(data["mouth"])

    # return format
    # {
    #   'eye': [
    #           "Eye's name (e.g. Dragon's Eye)",
    #           "description"
    #           ],
    #   'nose': "description",
    #   'mouth': "description"
    # }
    return {
        'eye': eye,
        'nose': nose,
        'mouth': mouth
    }


# left eye
def process_eye(data):
    left = min(data, key=lambda x: x[0])
    right = max(data, key=lambda x: x[0])
    top = max(data, key=lambda x: x[1])
    bottom = min(data, key=lambda x: x[1])
    width = right[0] - left[0]
    height = top[1] - bottom[1]
    ratio = width / height

    if ratio >= 4.0:
        if left[1] < right[1]:
            # 봉황눈
            return 0 #['Phoenix Eye', 'The phoenix eye is considered the best in physiognomy. The shape of the eyes is thin and continues to become longer towards the end, and the pupil is very black and the white part is transparent. It is said that he has a benevolent personality and wisdom to look into the future with eyes that fit the saying “nothing is impossible”. King Sejong and So Ji-seop are applicable, and Yoo Seung-ho also has phoenix eyes.']
        else:
            # 용눈
            return 1 #['Dragon\'s Eye', 'The dragon\'s eyes, which symbolize good fortune, are clearly black and white and are characterized by long tears. A person with dragon eyes is a fortune that has a high possibility of becoming the emperor or empress of a country. After the phoenix eye, which is the best eye contemplation, the auspicious sign is the dragon eye.']
    elif ratio >= 2.0:
        slope = (right[1] - left[1]) / (right[0] - left[0])
        if slope > 0.5:
            # 호랑이눈
            return 2 #['Tiger\'s Eye', 'The tiger\'s eyes have large eyes and small pupils, slightly yellowish, and are round and curved. He has a strong personality, has a sense of justice, is active in community service, and is destined to enjoy wealth and honor.']
        elif slope > 0.3:
            # 사자눈
            return 3 #return ['Lion\'s Eye', 'Lion eyes have large eyes with double eyelids, and the corners of the eyes are raised upward. With a wise and generous personality, he likes to wear official uniforms and rises in the world early. Eyes with raised eyebrows are a contemplation of good brains and longevity, and if you do not make enemies of those around you, you will be lucky to succeed in business or politics.']
        elif slope > 0.1:
            # 학눈
            return 4 #return ['Crane Eye', 'Crane eyes are the most common form for Asians without double eyelids, and are of an appropriate size and have clear black and white pupils. Integrity and innocence, ideals are high, and the people around them have a lot of trust and wealth luck is good.']
        else:
            # 공작눈
            return 5 # return ['Peacock Eye', 'The peacock eye is wise and discerning. They belong to large eyes, are sensitive and expressive. The downside is that the mind is weak.']
    elif ratio >= 1.5:
        # 원앙눈
        return 6 #return ['Mandarin Duck Eye', 'He is good at collecting wealth and has a good marital relationship.']
    elif ratio >= 1.0:
        # 소눈
        return 7 #return ['Cow\'s Eye', 'He has a benevolent personality, has a strong patience, makes few mistakes, and has a diligent personality. often become very wealthy.']
    else:
        # 참새눈
        return 8 # #return ['Sparrow\'s Eye', 'He has a clear brain and a strong sense of responsibility, so he is diligent and doesn\'t know much about money, but he has an impatient personality and is stubborn.']
    # ratio
    # (봉황눈 > 용눈) > (호랑이 > 사자 > 학 > 공작) > 원앙 > 소 > 참새 (1.0)
    # 괄호 안은 left, right 의 높낮이로 비교
    # https://m.blog.naver.com/knk8884/220895457093


def process_nose(data):
    left = min(data, key=lambda x: x[0])
    right = max(data, key=lambda x: x[0])
    top = max(data, key=lambda x: x[1])
    bottom = min(data, key=lambda x: x[1])
    width = right[0] - left[0]
    height = top[1] - bottom[1]
    ratio = height / width
    if ratio >= 2.0:
        # 긴 코
        return 0 #'People with long noses are proud of themselves. They also like noble things, so they often have luxurious hobbies from an early age. They usually have a strong sense of responsibility, so no matter what task they are entrusted with, they feel safe around them.'
    elif ratio >= 1.8:
        # 큰 코
        return 1 #'They are egoistic and self-centered. They say that there are cases where they become lonely because they are not considerate of the other person in interpersonal relationships.'
    elif ratio >= 1.5:
        # 작은 코
        return 2 #'They often lack self-confidence. There are cases where you hesitate a lot in everything and end up in failure because you hesitate to do something that will come true.'
    else:
        # 짧은 코
        return 3 #'They are fast-paced. Wherever they go, they adapt well and behave in a snappy manner. He doesn\'t get excited about most things, and even if something bad happens, he\'s a simple person who doesn\'t get angry and goes over it smoothly.'


def process_mouth(data):
    left = min(data, key=lambda x: x[0])
    right = max(data, key=lambda x: x[0])
    top = max(data, key=lambda x: x[1])
    bottom = min(data, key=lambda x: x[1])
    width = right[0] - left[0]
    height = top[1] - bottom[1]
    ratio = width / height
    if ratio >= 3.0:
        # 얇은
        return 0 #'They are affectionate, loyal, and affectionate, and if their lips are bright, they have strong vitality and are well-off financially. They may also be acclaimed as gourmets. They are said to be lucky with their health because they prefer delicious food.'
    else:
        # 두꺼운
        return 1 #'They are sensitive and irritable, prone to stress, lack of affection, often indifferent to others, and can be callous. Also, they have no affection, so it can be said that they lack understanding for others. They have a less emotional side of themselves and have an unusual competitive spirit and ability to overcome difficulties.'
