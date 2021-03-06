# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file, redirect, request, response
import os, time, re
import json, markdown
import logging

app = Bottle()

MENU_PATH = "./pages/Menu.txt"

# Configuration file loading
config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'Pywikiss 0.1';

# logs DEBUG dans pywikiss-server.log
DEBUG_LEVEL = {'CRITICAL':50, 'ERROR':40, 'WARNING':30, 'INFO':20, 'DEBUG':10}
logging.basicConfig(filename='pywikiss-server.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filemode='w')
logger = logging.getLogger(__name__)

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
@view('templates/template.tpl')
def all_pages(page_name, action=''):
	"""

	"""
	logger.info(" -- Show page : %s" % page_name)
	return show_page(page_name, action, {})

@app.route('/<page_name>/<action>', method='POST')
@view('templates/template.tpl')
def save_page(page_name, action=''):
	'''

	'''
	logger.info(" -- Save page : %s" % page_name)

	params = {}
	if authentificated():
		logger.debug("page saved")
		do_save(page_name)
		return redirect("/%s" % page_name)
	else:
		logger.warning('Password given incorrect')
		params['ERROR'] = 'Password given incorrect.'
		action = 'edit'

	content = request.forms.get('content')
	return show_page(page_name, action, params, content)

def show_page(page_name, action, params={}, content = ''):

	params.update(config)
	params['PAGE_NAME'] = page_name
	params['ACTION'] = action

	file_path = "./pages/" + page_name + ".txt"
	
	logger.info("page path: " + file_path)

	if os.path.exists(file_path):

		# Open file in read mode.
		page_file = open(file_path, "r")
		lines = page_file.readlines()
		lines = ''.join(lines).decode('utf-8')

		# Edit mode
		if action == 'edit' and content == '':
			content = lines					
		elif not action == 'edit':
			# Replace this wiki syntax [[URL]] to the markdown syntax [URL](URL)
			patternStr = ur'\[{2}([^\]]*)\]{2}'   # OR '\[\[([^\]]*)\]\]'  
			repStr = ur'[\1](\1)'
			content = re.sub(patternStr, repStr, lines)

			# Markdown transformation
			content = markdown.markdown(content)

		page_file.close()

	# Add content parameter.
	if len(content) > 0:
		params['CONTENT'] = content
	else:
		params['CONTENT'] = ''
		logger.debug("Empty page")

	# Is user authentificated for edition mode.
	if action == 'edit':
		if authentificated() == True:
			logger.debug("je mets AUTHENTIFICATED à true")
			params['AUTHENTIFICATED'] = "True"
		else:
			logger.debug("je mets AUTHENTIFICATED à false")
			if 'AUTHENTIFICATED' in params:
				del(params['AUTHENTIFICATED'])

	# Add menu content parameter.
	params['MENU'] = compute_menu()

	# Add last file modification date label parameter.
	params['CHANGE'] = 'Dernière modification'

	# Add last file modification date parameter.
	if os.path.exists(file_path):
		params['TIME'] = time.ctime(os.path.getmtime(file_path))

	return params

def compute_menu():

	try:
		if os.path.exists(MENU_PATH):
			page_file = open(MENU_PATH, "r")
			lines = page_file.readlines()
			lines = ''.join(lines)
			# Replace this wiki syntax [[URL]] to <li><a href="./URL">URL</a></li>
			patternStr = ur'\[{2}([^\]]*)\]{2}'   # OR '\[\[([^\]]*)\]\]'  
			repStr = ur'<li><a href="./\1">\1</a></li>'
			menu = re.sub(patternStr, repStr, lines)
			if len(menu) > 0:
				return "<ul>" + menu + "</ul>"

	except IOError:
		logger.warning("Can't open " + MENU_PATH)

	return ""

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

#	print time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
# ou time.ctime()

	content = request.forms.get('content')

	fichier = open(file_path, "w")
	fichier.write(content)
	fichier.close()

def authentificated():
	"""
		Check if user is correctly authenfificated.
	"""
	u_pass = request.forms.get('password')
	g_pass = config['PASSWORD']

	# TODO : enregistrer le mot de passe en md5 dans le coockie.
	if request.get_cookie("AutorisationPyWiKiss") and request.get_cookie("AutorisationPyWiKiss") == g_pass or u_pass and u_pass == g_pass or g_pass == '':
		if request.get_cookie("AutorisationPyWiKiss") == None or request.get_cookie("AutorisationPyWiKiss") != g_pass:
			response.set_cookie("AutorisationPyWiKiss", g_pass, max_age=60*60*24, path="/")
			logger.debug("enregistrement dans le cookie")

		logger.debug("authentificated :o)")
		return True
	else:
		logger.debug("Not authentificated :o(")
		return False

# Launch server on port 5000
run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
