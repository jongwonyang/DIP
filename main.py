# Nahyuk
import sys

from face_alignment import face_alignment
from face_masking import face_masking
from face_reading import face_reading

image = sys.argv[1]

masking = face_masking(image)
alignment = face_alignment(masking)
reading = face_reading(alignment)

print(reading)