
#importa utilerias necesarias
import requests
from textblob import TextBlob

# Libreria auxiliar para el entrenamiento web
from StringTagger.StringClf import Classifier
from StringTagger.getPage import getTextPage


def salary(a):
	busqueda_money = ''
	busqueda_money = a["salary"]
	if busqueda_money.find('No especificado') == -1:
		return 1
	else:
		return 0

def anios(escri,a):
	#busqueda de años en base a idioma Years o Años
	if escri == "es":
		## Buscador de años y comparacion con senior , junior, semi senior
		busqueda_senior_job = ''
		busqueda_senior_job = a["job"]
		busqueda_senior_job.lower()
		if busqueda_senior_job.find('senior') == -1 or busqueda_senior_job.find('sr') == -1:
			busqueda_senior = ''
			busqueda_senior = a["description"]
			busqueda_senior.lower()
			if busqueda_senior.find('años') == -1:
				return 0
			else:
				return 1

		elif busqueda_senior_job.find('junior') == -1 or busqueda_senior_job.find('jr') == -1:
			busqueda_junior = ''
			busqueda_junior = a["description"]
			busqueda_junior.lower()
			if busqueda_junior.find('años') == -1:
				return 0
			else:
				return 1
		else:
			return 2
	else :
		## Buscador de años y comparacion con senior , junior, semi senior ingles
		busqueda_senior_job = ''
		busqueda_senior_job = a["job"]
		busqueda_senior_job.lower()
		if busqueda_senior_job.find('senior') == -1 or busqueda_senior_job.find('sr') == -1:
			busqueda_senior = ''
			busqueda_senior = a["description"]
			busqueda_senior.lower()
			if busqueda_senior.find('years') == -1:
				return 0
			else:
				return 1

		elif busqueda_senior_job.find('junior') == -1 or busqueda_senior_job.find('jr') == -1:
			busqueda_junior = ''
			busqueda_junior = a["description"]
			busqueda_junior.lower()
			if busqueda_junior.find('years') == -1:
				return 0
			else:
				return 1

		else:
			return 2



"""def idioma(a):
	##definicion de idioma
	idioma = TextBlob(a['description'])
	escri = idioma.detect_language()
	##fin definicion idioma
	#en base al idioma se crea la lista para busquedas en o es
	if escri == "en":
	
		training_data_es = {
			# Entrenamos al clasificador con paginas de wikipedia.
			# Datos para entrenar al clasificador
			"Desarrollador JavaScript": [
			'https://es.wikipedia.org/wiki/Java_(lenguaje_de_programación)',
			'https://es.wikipedia.org/wiki/JavaScript'
			],
			"Desarrollador Java": [
			'https://www.iebschool.com/blog/herramientas-desarrolladores-java-tecnologia/',
			'https://es.wikipedia.org/wiki/Java_(lenguaje_de_programación)'
			],
			"Desarrollador Python": [
			'https://es.wikipedia.org/wiki/Python',
			'https://bbvaopen4u.com/es/actualidad/herramientas-basicas-para-los-desarrolladores-en-python'
			],
			"Desarrollador PHP": [
			'https://es.wikipedia.org/wiki/PHP'
			],
			"Desarrollador Full Stack": [
			'https://clouding.io/blog/desarrollador-full-stack/',
			'https://keepcoding.io/es/blog/8-requisitos-full-stack-developer/',
			],
			"Network": [
			'https://resources.workable.com/senior-network-engineer-job-description'
			]
		}
	else:
		
		training_data_es = {
			# Entrenamos al clasificador con paginas de wikipedia.
			# Datos para entrenar al clasificador
			"Desarrollador JavaScript": [
			'https://es.wikipedia.org/wiki/Java_(lenguaje_de_programación)',
			'https://es.wikipedia.org/wiki/JavaScript'
			],
			"Desarrollador Java": [
			'https://www.iebschool.com/blog/herramientas-desarrolladores-java-tecnologia/',
			'https://es.wikipedia.org/wiki/Java_(lenguaje_de_programación)'
			],
			"Desarrollador Python": [
			'https://es.wikipedia.org/wiki/Python',
			'https://bbvaopen4u.com/es/actualidad/herramientas-basicas-para-los-desarrolladores-en-python'
			],
			"Desarrollador PHP": [
			'https://es.wikipedia.org/wiki/PHP'
			],
			"Desarrollador Full Stack": [
			'https://clouding.io/blog/desarrollador-full-stack/',
			'https://keepcoding.io/es/blog/8-requisitos-full-stack-developer/',
			],
		}
	return training_data_es, escri
#conexion
def entrena(data):
	#training_data_es, idio = idioma(data[0])
	vAnios =  anios(idio,data[0])
	
	#categorizacion de titulo
	clf = Classifier()  # Instancia del clasificador
	for category, urls in training_data_es.items(): # Entrenamos al clasificador con el contenido de cada pagina
		for url in urls:
			clf.train(getTextPage(url), category)
	return clf, vAnios
	# Iniciamos el proceso de clasificación con el metodo "String"
	# Solo le pasamos como argumento el texto que deseamos etiquetar (clasificar)"""

#impresion de comparativas
def lectura(text,desc):
    archivo = open("%s.txt"%text, "r")
    texto=archivo.read()
    vect=texto.split('\n')
    cont=0
    for m in desc:
        for k in m:    
            for n in vect: 
                if k.lower()==n:
                    cont=cont+1
    return cont

def contador(a):
    cont =[['frontend',0],['backend',0],['QA',0],['fullStack',0],['android',0]]
    may=['',0]
    for n in cont:
        n[1]=lectura(n[0],a)
        if n[0]=="fullStack":
            if n[1]<10:
                
                n[1]=0
        if n[1]>may[1]:
            may[0]=n[0]
            may[1]=n[1]
    if may[1]==0:
        may[0]="definir mas"
    
    return may[0]
def punt_title(clas,job):
    Fs=['fullstack','full','stack','full-stack']
    Fe=['frontend','front','fornt-end']
    Be=['backend','back','back-end']
    Qa=['qa','tester','qa/tester']
    Ad=['android','movil']
    j=[pareja.split() for pareja in job.split(".")]
    p=0
    
    if clas.lower() == 'fullstack':
        print("entro")
        p=comp_tit(Fs,j)
    if clas == 'frontend':
        p=comp_tit(Fe,j)
        if(p==0):
            p=comp_tit(['web',''],j)-1
    if clas == 'backend' :
        p=comp_tit(Be,j)
        if(p==0):
            p=comp_tit(['web',''],j)-1
    if clas == 'QA' :
        p=comp_tit(Qa,j)
    if clas == 'android' :
        p=comp_tit(Ad,j)
    if p<0:
        p=1    
    return p

def comp_tit(clas,j):
    point=0
    for n in clas:
        for m in j:
            for k in m:
                if k.lower()==n:
                    point=5
                    break
    
    return point

def puntuacion_es(texto):
        diccionario = { 'funciones': ['funciones','conocimientos', 'actividades', 'tareas a desempeñar','Perfil Técnico','Perfil Tecnico'],
        'prestaciones':['prestaciones', 'ofrecemos'],
        'horario': ['horario']
        }      
        agregar = []
        cadena = texto
        cadena = cadena.lower()
        #Verifica si en el texto viene espeficado el campo de funciones, prestaciones u horario
        for llaves in diccionario.keys():
            palabras = diccionario[llaves]
            for palabra in palabras:
                if cadena.find(palabra) != -1:
                    agregar.append(llaves)
                    break  

        return agregar 

#Si el texto esta en ingles lo procesa en esta funcion
def puntuacion_en(texto):
        diccionario = { 'functions': ['functions','activities', 'tasks', 'requirements','requiered','requiered:'],
        'benefits':['benefits', 'offer'],
        'schedule': ['schedule']
        }      
        agregar = []
        cadena = texto
        cadena = cadena.lower()
        # Verifica si en el texto viene espeficado el campo de funciones, prestaciones u horario
        for llaves in diccionario.keys():
            palabras = diccionario[llaves]
            for palabra in palabras:
                if cadena.find(palabra) != -1:
                    agregar.append(llaves)
                    break
        return agregar 


# Retorna una lista con los campos encontrados
def puntuar(texto):
    # Verifica el lenguaje del texto por default lo manda a Ingles
    b = TextBlob(texto)
    language = b.detect_language()
    if language == 'es':
        return puntuacion_es(texto)
    else:
        return puntuacion_en(texto)


def entrenado():
	r = requests.get("https://empleosti.com.mx/api/v2/vacancies?token=LeSNJYC3Nd&take=400")
	data = r.json()
		
	a = data[394]
	string = a["description"]
	desc=[pareja.split() for pareja in string.split(".")]
	clas=contador(desc)
	print(a["job"])
	print("Calificacion del titulo vs contenido: ", punt_title(clas,a["job"]))
	contenido = puntuar(string)
	print("Calificacion del contenido: ", len(contenido),contenido )
	vMoney =  salary(data[0])
	print("Calificacion de salario: ",vMoney)
	idioma = TextBlob(a['description'])
	escri = idioma.detect_language()
	vAnios =  anios(escri,data[0])
	print("Calificacion de especificacion de anios: ",vAnios)
	print("Etiqueta del titulo recomendada: %s" % clas)

    #print(string)

entrenado()