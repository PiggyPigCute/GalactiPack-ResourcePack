block_path = "assets/galactipack/models/block"
item_path = "assets/galactipack/models/item"
item_block_path = "assets/galactipack/models/item/block"
display_dict = {"fixed": {"rotation": [-90, 0, 0],"translation": [0, 0, -16],"scale": [2.001, 2.001, 2.001]}}

from os import listdir, system, name, remove
from json import loads, dumps

def cls():
	if name == 'nt': system('cls')
	else: system('clear')
def model(path: str) -> str:return path.replace("/models/", ":", 1).replace("assets/", "", 1)

cls() 
for file in listdir(block_path):
	if file.endswith(".json") and not file in listdir(item_block_path):
		print("converting " + file)
		file_name = file[:-5]
		with open(block_path + "/" + file, "r") as f:
			block = loads(f.read())
		with open(block_path + "/" + file, "w+") as f:
			f.write(dumps(indent=4,
				obj = {"parent": f"{model(item_block_path)}/{file_name}" ,"display": display_dict}))
		with open(item_block_path + "/" + file, "w+") as f:
			if "display" in block and "fixed" in block["display"]:
				del block["display"]["fixed"]
				if block["display"] == {}: del block["display"] 
			f.write(dumps(indent=4, obj=block))
		if file in listdir(item_path):remove(item_path + "/" + file)
print("done")
