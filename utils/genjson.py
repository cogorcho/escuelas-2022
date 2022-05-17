import json
import codecs

#------------------------------------------------------------------
#
#------------------------------------------------------------------
def gendata(archivo):
	"""Abre el archivo csv de escuelas y genera una lista
		de dict, uno por escuela"""
	with open(archivo) as e:
		lines = e.readlines()

	keys = lines[0].rstrip("\n").split('|')
	data = []

	for i in range(1,len(lines)):
		values = lines[i].rstrip("\n").split('|')
		e = {}
		for k,v in zip(keys, values):
			if v == "X":
				val = "SI"
			elif v == "":
				val = "NO"
			else:
				val = v

			e[k.replace("Ed. ","")] = val
		data.append(e)

	return data


#------------------------------------------------------------------
#
#------------------------------------------------------------------
def jfile(data, archivo):
	print(archivo)
	"""Crea el archivo json de escuelas"""
	with codecs.open(archivo,'w',encoding='utf-8') as f:
		for i in range(0,len(data)):
			if i == 0:
				f.write("[")
			else:
				f.write(",\n")
			json.dump(data[i], f, ensure_ascii=False)
		f.write("]")
	print("OK!")

jfile(gendata('csv/escuelas.csv'),'Json/Escuelas.json')
jfile(gendata('csv/tiposeducacion.csv'),'Json/TiposEducacion.json')
jfile(gendata('csv/niveles_comun.csv'),'Json/NivelesComun.json')
jfile(gendata('csv/niveles_artistica.csv'),'Json/NivelesArtistica.json')
jfile(gendata('csv/niveles_adultos.csv'),'Json/NivelesAdultos.json')
jfile(gendata('csv/niveles_hospitalaria.csv'),'Json/NivelesHospitalaria.json')
jfile(gendata('csv/niveles_especial.csv'),'Json/NivelesEspecial.json')
jfile(gendata('csv/niveles_complementarios.csv'),'Json/NivelesComplementarios.json')

