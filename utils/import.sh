mongoimport --jsonArray --db Escuelas --collection Escuelas --file Json/Escuelas.json 
mongoimport --jsonArray --db Escuelas --collection TiposEducacion --file Json/TiposEducacion.json

mongoimport --jsonArray --db Escuelas --collection NivelesAdultos --file Json/NivelesAdultos.json 
mongoimport --jsonArray --db Escuelas --collection NivelesArtistica --file Json/NivelesArtistica.json 
mongoimport --jsonArray --db Escuelas --collection NivelesComplementarios --file Json/NivelesComplementarios.json 
mongoimport --jsonArray --db Escuelas --collection NivelesComun --file Json/NivelesComun.json 
mongoimport --jsonArray --db Escuelas --collection NivelesEspecial --file Json/NivelesEspecial.json 
mongoimport --jsonArray --db Escuelas --collection NivelesHospitalaria --file Json/NivelesHospitalaria.json 

# Escuelas.json
# TiposEducacion.json
# NivelesAdultos.json
# NivelesArtistica.json
# NivelesComplementarios.json
# NivelesComun.json
# NivelesEspecial.json
# NivelesHospitalaria.json

# --------------------------------------------
# Conectado a mongo, use Tusi y copio las 
# colecciones a la db Escuelas
# --------------------------------------------
# db.Provincias.find().forEach(function(d){ db.getSiblingDB('Escuelas')['Provincias'].insert(d); });
# db.Municipios.find().forEach(function(d){ db.getSiblingDB('Escuelas')['Municipios'].insert(d); });
# db.Localidades.find().forEach(function(d){ db.getSiblingDB('Escuelas')['Localidades'].insert(d); });
# db.Departamentos.find().forEach(function(d){ db.getSiblingDB('Escuelas')['Departamentos'].insert(d); });