import os
import json
import tempfile
import argparse

def write_json(data):
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	try:
		with open(storage_path, 'r') as file:
			old = json.load(file)
			file.close()
	except:
		old = []
	
	old = struct_append(old, data)
	with open(storage_path, 'w') as file:
		json.dump(old, file)
		file.close()

def read_json(key):
	try:
		storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
		with open(storage_path, 'r') as file:
			struct = json.load(file)
			found = False
			for item in struct:
				if item[0] == key:
					found = True 
					print(str(item[1]).replace('[', '').replace(']', '').replace('\'', ''))
			file.close()
	except: 
		found = False		
	if not found:	
		# print(f'Ключ \'{key}\' отсутствует')
		print(None)

def struct_append(struct, data):
	key, val = data
	for item in struct:
		if item[0] == key:
			unique = True
			for list_item in item[1]:
				if list_item == val:
					unique = False	
					break	
			if unique:
				item[1].append(val)
			return struct
	struct.append((key,[val]))
	return struct 

parser = argparse.ArgumentParser()
parser.add_argument("--key", help = "key_name")
parser.add_argument("--val", help = "value")
parser.add_argument("-clean", help = "Use, if you want to clean a storage")
args = parser.parse_args()

key, val, clean = args.key, args.val, args.clean

if clean:	
	answer = input('Вы уверены, что хотите стереть хранилище(Y/N):')
	if answer == 'Y':
		storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
		with open(storage_path, 'w'):
			print('Очищено!')
	else:
		print('Отмена. Выход.')
	exit()

if key and not val:
	read_json(key)
elif key and val:
	write_json((key, val))
else:
	print('Вы не ввели ключ! Введенное значение будет проигнорировано!')



