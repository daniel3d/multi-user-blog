### ( Multi User Blog ) 

## For Udacity Full Stack Web Developer Nanodegree

#### Installation instructions

 * First make sure you have installed [Google Cloud SDK](https://cloud.google.com/sdk/docs)
 * To get App engine for python run `gcloud components install app-engine-python`
 * Install python libs by runing this command in the root of the folder `pip install -t lib -r requirements.txt`
 * Install node libs `npm install`
 * Run `gulp` your browser will open [http://localhost:8000/instances](http://localhost:8000/instances) the app engine admin and [http://localhost:9999](http://localhost:9999) for the app

#### Common errors
 * If you get error `ValueError: virtualenv: cannot access lib: No such virtualenv or site directory` make sure you run step 3 from the 'Installation instructions' run `pip install -t lib -r requirements.txt`

### Stuff used to make this:

 * [Simple Markdown Editor](https://simplemde.com) The blog editor
 * [Webapp2](https://webapp2.readthedocs.io/en/latest) Python web framework compatible with Google App Engine’s 
 * [Google App Engine SDK](https://cloud.google.com/appengine/downloads?csw=1) The app engine
 * [Python Development Server](https://cloud.google.com/appengine/docs/python/tools/using-local-server) To emulate google app engine
 * [Pep8online](http://pep8online.com/) Check the code is compatable with PEP8 standard
 * [PEP8 Autoformat](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat) To format the files in PEP8 requirements
 * [PEP257 checker](https://pypi.python.org/pypi/pep257) Python docstring style checker
 * [Trianglify](https://qrohlf.com/trianglify-generator/) Nice Background Image
 * [Python Slugify](https://pypi.python.org/pypi/python-slugify) Generate url slugs from the post title