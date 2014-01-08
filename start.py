# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file, redirect, request, response
import json
import markdown
import os


app = Bottle()
 
# Configuration file loading
config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'Pywikiss 0.1';

@app.route('/')
def home():
	"""
		La racine du wiki est rediriger vers la page Accueil.
	"""
	return redirect("/Accueil")

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, images, etc...
    """
    return static_file(filename, root='./static/')

@app.route('/<page_name>')
@app.route('/<page_name>/<action>')
@view('template.tpl')
def all_pages(page_name, action=''):
	"""

	"""
	return show_page(page_name, action)

#  FOR THE PASSWORD PART.
@app.route('/<page_name>/<action>', method='POST')
@view('template.tpl')
def save_page(page_name, action=''):
	print " --> save_page"

	params = {}
	if authentified():
		print (' -- save')
		do_save(page_name)
		return redirect("/%s" % page_name)
	else:
		params['ERROR'] = 'Mot de passe spécifié incorrect.'
		action = 'edit'

	return show_page(page_name, action, params)

def show_page(page_name, action, params={}):

	params.update(config)

	params['PAGE_NAME'] = page_name
	params['ACTION'] = action

	file_path = "./pages/" + page_name + ".txt"
	
	print(" -- Affiche la page " + file_path)

	content = ''
	if os.path.exists(file_path):

		print " -- le fichier exist"
		# Ouverture d'un fichier en *lecture*:
		fichier = open(file_path, "r")	 
		lines = fichier.readlines()
		lines = ''.join(lines)
		if action == 'edit':
			content = lines 
		else:
			content = markdown.markdown(lines)

		fichier.close()

	if len(content) > 0:
		params['CONTENT'] = content
	else:
		params['CONTENT'] = ''
		print " -- Page vide."

	return params

def do_save(page_name):

	file_path = "./pages/" + page_name + ".txt"

# GROS TODO 
# Si contenu == vide : effacer le ficheir existant. 
# TODO if fichier exist : faire un backup.
#	if os.path.exists(file_path):
# si le rep de backup n'existe pas le créer 
# tester les droits etc.
# faire un fichier de backup AAAAMMJJ-HHMM.back
# en dans le ficheir backup : // 2013/02/13 10:30 /  90.83.105.41
# regarder method php   urlencode(stripslashes($PAGE_TITLE) 


	content = request.forms.get('content')

	fichier = open(file_path, "w")
	fichier.write(content)
	fichier.close()

def authentified():
	"""
		Check if user is correctly authenfified.l
	"""
	u_pass = request.forms.get('password')
	g_pass = config['PASSWORD']

	# TODO : enregistrer le mot de passe en md5 dans le coockie.
	if request.get_cookie("AutorisationPyWiKiss") and request.get_cookie("AutorisationPyWiKiss") == g_pass or u_pass and u_pass == g_pass or g_pass == '':
		if request.get_cookie("AutorisationPyWiKiss") == None or request.get_cookie("AutorisationPyWiKiss") != g_pass:
			response.set_cookie("AutorisationPyWiKiss", g_pass, max_age=60*60*24)
			print " -- enregistrement dans le coockie"

		print " -- Authentifié"
		return True
	else:
		print " -- Non Authentifié"
		return False

# Lancement du serveur sur le port 8080
run(app, host='localhost', port=8080, reloader=True)