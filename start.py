# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file, redirect, request, response
import json
import markdown
import os
import time

app = Bottle()

# TODO : Virer l'input dans le template si l'utilisateur est authentifié.
 
# Configuration file loading
config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'Pywikiss 0.1';

@app.route('/')
def home():
	"""
		The root of the wiki is redirected to the Home page.
	"""
	return redirect("/Accueil")

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Serving static files such as. Js,. Css, images, etc ...
    """
    return static_file(filename, root='./static/')

@app.route('/<page_name>')
@app.route('/<page_name>/<action>')
@view('template.tpl')
def all_pages(page_name, action=''):
	"""

	"""
	return show_page(page_name, action)

@app.route('/<page_name>/<action>', method='POST')
@view('template.tpl')
def save_page(page_name, action=''):
	'''

	'''
	print " --> save_page"

	params = {}
	if authentified():
		print (' -- save')
		do_save(page_name)
		return redirect("/%s" % page_name)
	else:
		params['ERROR'] = 'Password given incorrect.'
		action = 'edit'

	return show_page(page_name, action, params)

def show_page(page_name, action, params={}):

	params.update(config)
	params['PAGE_NAME'] = page_name
	params['ACTION'] = action

	file_path = "./pages/" + page_name + ".txt"
	
	print(" -- Show page : " + file_path)

	content = ''
	if os.path.exists(file_path):

		print " -- File exist"
		# Open file in read mode.
		page_file = open(file_path, "r")	 
		lines = page_file.readlines()
		lines = ''.join(lines)
		if action == 'edit':
			content = lines 
		else:
			# TODO :  Pour les besoins du wiki, remplacer [[XXX]] par [XXX](/XXX)
			content = markdown.markdown(lines)

		# Last modification date.
		nbs = os.path.getmtime(file_path) 
		print time.strftime('%d/%m/%y %H:%M:%S',time.gmtime(nbs))

		page_file.close()

	if len(content) > 0:
		params['CONTENT'] = content
	else:
		params['CONTENT'] = ''
		print " -- Empty Page."

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


	print time.strftime('%d/%m/%y %H:%M:%S',time.localtime())

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

		print " -- authenticated"
		return True
	else:
		print " -- Not authenticated"
		return False

# Launch server on port 8080
run(app, host='localhost', port=8080, reloader=True)