# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file, redirect
import json
import markdown
import os


app = Bottle()
 

# Chargement du fichier de config.
config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'BlazeKiss 0.1';

@app.route('/')
def home():
	return redirect("/Accueil")

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

@app.route('/<page_name>')
@app.route('/<page_name>/<action>')
@view('template.tpl')
def hello(page_name, action=''):
	config['PAGE_NAME'] = page_name;
	config['ACTION'] = action;

	file_path = "./pages/" + page_name + ".txt"
	
	print(" -- Chemin du ficheir " + file_path)

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

		print ' ----  ### CONTENT ### '
		print content


	if len(content) > 0:
		config['CONTENT'] = content
	else:
		config['CONTENT'] = ''
		print " -- Pas de contenu"

	return config
 

#  FOR THE PASSWORD PART. 
# @post('/login') # or @route('/login', method='POST')
# def do_login():
#     username = request.forms.get('username')
#     password = request.forms.get('password')
#     if check_login(username, password):
#         return "<p>Your login information was correct.</p>"
#     else:
#         return "<p>Login failed.</p>"

# MANAGING COOCKIES  http://bottlepy.org/docs/dev/tutorial.html#cookies 

# Lancement du serveur sur le port 8080

run(app, host='localhost', port=8080, reloader=True)