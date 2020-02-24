import face_recognition
from PIL import Image
import numpy as np
import os
import pickle

def learn_faces():
	known_faces = []
	known_faces_names = []
	working_dir = os.getcwd() + '/' + 'Faces'
	for file in os.listdir(working_dir):
	    if file[0] == ".":
	        continue
	    else:
	        print(file)
	        known_faces.append((face_recognition.face_encodings(face_recognition.load_image_file(working_dir + '/' + file))[0]))
	        known_faces_names.append(file.rsplit('.', 1)[0])

	with open("faces.txt", "wb") as fp:
		pickle.dump(known_faces, fp)
	with open("names.txt", "wb") as fp:
		pickle.dump(known_faces_names, fp)

def give_match(file_path):
	with open("faces.txt", "rb") as fp:
		known_faces = pickle.load(fp)
	with open("names.txt", "rb") as fp:
		known_faces_names = pickle.load(fp)
	unknown_faces = face_recognition.face_encodings(face_recognition.load_image_file(file_path))
	people_found = []
	for face in unknown_faces:
		face_distances = list(face_recognition.face_distance(known_faces, face))
		max_index = face_distances.index(min(face_distances))
		max_match_person = known_faces_names[max_index]
		known_faces.pop(max_index)
		known_faces_names.pop(max_index)
		people_found.append(max_match_person)
	return people_found

def update_count(people_found, count_map):
	for name in people_found:
		clean_name = ''.join([i for i in name.replace("_", " ") if not i.isdigit()])
		count_map[clean_name] += 1

def delete_files(folder):
	import os, shutil
	for filename in os.listdir(folder):
	    file_path = os.path.join(folder, filename)
	    try:
	        if os.path.isfile(file_path) or os.path.islink(file_path):
	            os.unlink(file_path)
	        elif os.path.isdir(file_path):
	            shutil.rmtree(file_path)
	    except Exception as e:
	        print('Failed to delete %s. Reason: %s' % (file_path, e))