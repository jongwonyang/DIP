# Nahyuk
import sys

from face_alignment import face_alignment
from face_masking import face_masking
from face_reading import face_reading
import cv2

image = sys.argv[1]

masking = face_masking(image)
alignment = face_alignment('5.jpg')
reading = face_reading(alignment)

##INPUT
bg_path = './background.jpeg'
face_path = './output.jpg'

# Loading Background
bg = cv2.imread(bg_path)
#bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)

# Add result image
face = cv2.imread(face_path)
#face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
face = cv2.resize(face, (250,250))
bg[120:370, 240:490] = face

### EYE ###

e = reading['eye'] # Classified eye class (0~8)

# Circle
x_positions = [65, 145, 220, 290, 365, 435, 515, 590, 660]
cv2.circle(bg, center=(x_positions[e],475), radius=30, color=(255,0,0), thickness=2)

# Description
text_font = cv2.FONT_ITALIC 
text = [# 봉황눈
    'The phoenix eye is considered the best in physiognomy. The shape of the eyes is thin and continues to \nbecome longer towards the end, and the pupil is very black and the white part is transparent. It is \nsaid that he has a benevolent personality and wisdom to look into the future with eyes that fit the saying \n"nothing is impossible". King Sejong and So Ji-seop are applicable, and Yoo Seung-ho also has phoenix eyes.',
        # 용눈
    'The dragon\'s eyes, which symbolize good fortune, are clearly black and white and are characterized by long \ntears. A person with dragon eyes is a fortune that has a high possibility of becoming the emperor or empress \nof a country. After the phoenix eye, which is the best eye contemplation, the auspicious sign is the dragon eye.',
        # 호랑이눈
    'The tiger\'s eyes have large eyes and small pupils, slightly yellowish, and are round and curved. He has a strong \npersonality, has a sense of justice, is active in community service, and is destined to enjoy wealth and honor.',
        # 사자눈
    'Lion eyes have large eyes with double eyelids, and the corners of the eyes are raised upward. With a wise \nand generous personality, he likes to wear official uniforms and rises in the world early. Eyes with raised \neyebrows are a contemplation of good brains and longevity, and if you do not make enemies of those around \nyou, you will be lucky to succeed in business or politics.',
        # 학눈
    'Crane eyes are the most common form for Asians without double eyelids, and are of an appropriate size \nand have clear black and white pupils. Integrity and innocence, ideals are high, and the people around them \nhave a lot of trust and wealth luck is good.',
        # 공작눈
    'The peacock eye is wise and discerning. They belong to large eyes, are sensitive and expressive. The downside \nis that the mind is weak.',
        # 원앙눈
    'He is good at collecting wealth and has a good marital relationship.',
        # 소눈
    'He has a benevolent personality, has a strong patience, makes few mistakes, and has a diligent personality. \noften become very wealthy.',
        # 참새눈
    'He has a clear brain and a strong sense of responsibility, so he is diligent and doesn\'t know much about \nmoney, but he has an impatient personality and is stubborn.']
for i, line in enumerate(text[e].split('\n')):
    cv2.putText(bg, text=line, org=(25,550+i*15), fontFace = text_font, fontScale=0.37, color=(0,0,0), thickness=1)

### NOSE ###

n = reading['nose'] # Classified nose class (0~3)

# Nose
x_positions = [167, 292, 425, 543]
cv2.circle(bg, center=(x_positions[n],715), radius=40, color=(255,0,0), thickness=2)

# Description
text_font = cv2.FONT_ITALIC 
text = [# 긴 코
    'People with long noses are proud of themselves. They also like noble things, so they often have luxurious \nhobbies from an early age. They usually have a strong sense of responsibility, so no matter what task they \nare entrusted with, they feel safe around them.',
        # 짧은 코
    'They are fast-paced. Wherever they go, they adapt well and behave in a snappy manner. He doesn\'t get \nexcited about most things, and even if something bad happens, he\'s a simple person who doesn\'t get angry \nand goes over it smoothly.',
        # 큰 코
    'They are egoistic and self-centered. They say that there are cases where they become lonely because they \nare not considerate of the other person in interpersonal relationships.',
        # 작은 코
    'They often lack self-confidence. There are cases where you hesitate a lot in everything and end up in failure \nbecause you hesitate to do something that will come true.'
]
for i, line in enumerate(text[n].split('\n')):
    cv2.putText(bg, text=line, org=(25,775+i*15), fontFace = text_font, fontScale=0.37, color=(0,0,0), thickness=1)

### MOUTH ###

m = reading['mouth'] # Classified nose class (0~1)

# Nose
x_positions = [140, 605]
cv2.circle(bg, center=(x_positions[m],895), radius=35, color=(255,0,0), thickness=2)

# Description
text_font = cv2.FONT_ITALIC 
text = [# 얇은 입
    'They are affectionate, loyal, and affectionate, and if their lips are bright, they have strong vitality and are \nwell-off financially. They may also be acclaimed as gourmets. They are said to be lucky with their health \nbecause they prefer delicious food.',
        # 두꺼운 입
    'They are sensitive and irritable, prone to stress, lack of affection, often indifferent to others, and can be \ncallous. Also, they have no affection, so it can be said that they lack understanding for others. They have a \nless emotional side of themselves and have an unusual competitive spirit and ability to overcome difficulties.'
]
for i, line in enumerate(text[m].split('\n')):
    cv2.putText(bg, text=line, org=(25,960+i*15), fontFace = text_font, fontScale=0.37, color=(0,0,0), thickness=1)
    
cv2.imshow('face reading', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./face_reading.jpg', bg)