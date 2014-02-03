# Pywikiss

Pywikiss is a Wiki developed with KISS (**K**eep **I**t **S**imple **S**tupid) principe. 
It is strongly inspired by [Blazekiss](http://projet.idleman.fr/blazekiss/) but written in python.
It use the micro framework [bottle](http://bottlepy.org). 
Pywikiss use the markdown syntax.

## Install it

* No needs to get bottle, it given with sources. 

* Need python-markdown
    pip install markdown

* Download and decompress Pywikiss archive
* Edit and modify config.json at your convenience, don't forget to change the password
* Make sure the Pywikiss directory and all subdirectories are writable and readable,  if this is not the case, do a chmod 775

## Run it

    python start.py


## TODO List 

* ~~Manage menu~~
* Manage pages backup  
* Manage toc 
* enregistrer le mot de passe en md5 dans le cookie.
* FIXME : problème d'authentification sur les nouvelles pages.
* ~~FIXME : gestion des liens vers les pages un peu douteuse.~~
* FIXME : mauvaise gestion des caractères accentués.
