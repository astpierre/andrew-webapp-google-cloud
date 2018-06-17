################################################################################
#### Filename: 		'main.py'
#### Written by:	Andrew St. Pierre
#### Last modified:	Jun-17-2018
################################################################################

# imports
import webapp2
import time

# functions
def calulator(val_1,val_2):
	'''performs addition operation on the two digits input by user'''
	try:
		sum = float(val_1) + float(val_2)
		return str(sum)
	except ValueError:
		return 'invalid input'

def log_user(username, location):
	'''logs username in storage'''
	try:
		return str(username)
	except ValueError:
		return 'invalid input'

# main
class MainPage(webapp2.RequestHandler):
    def get(self):
    	
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('''
        <html>
        <head><title>Andrew's Website</title></head>
        <body>
        <h1>Welcome to Andrew's Website</h1>
        <h2>Happy Father's Day</h2>
        </body></html>''')
        
        name = self.request.get('name')
    	location = self.request.get('location')
        self.response.write('''
        <html><body>
        <form action='/' method='get'>
        	<fieldset>
        		<legend>Log visit:</legend><br>
	        	name: <input type='text' name='name' value={}><br>
	        	location: <input type='text' name='location' value={}><br>
        		<input type='submit' value='log'>
        	</fieldset>
        </form></body></html>'''.format(name,location))
        
        val_1 = self.request.get('val_1')
    	val_2 = self.request.get('val_2')
    	result = calulator(val_1,val_2)
        self.response.write('''
        <html><body>
        <form action='/' method='get'>
        	<fieldset>
        		<legend>Addition:</legend><br>
	        	value: <input type='text' name='val_1' value={}><br>
	        	value: <input type='text' name='val_2' value={}><br>
        		<input type='submit'>
        		sum = {}
        	</fieldset>
        </form></body></html>'''.format(val_1,val_2,result))

# routing
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)