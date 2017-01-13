from bottle import Bottle, run, route, static_file, view, template, post, request,default_app, debug

debug(True)

def htmlify(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
					<style>
						body {
							background-color: #f8e682 ;
							font-family: 'Times New Roman',sans-serif;
						}
						p {
							color: #000 ;
							font-size: 20px;
							margin-left: 60px ;
							margin-right: 60px;
							margin-top: 15px;
						}
						h2 {
							color: #0026ff;
							font-size: 25px;
							margin-top: 5px;
							margin-right: 60px;
							margin-left: 60px;
						}
						a:link{
							color: #808080;
						}
						a:visited{
							color: #b200ff;
						}
						a:hover{
							color: #ff6a00;
						}
						a:active{
							color: #f00;
						}
						ol{
							list-style-type: upper-roman;
						}
						input[type=text]{
							border: 3px solid red;
							border-radius: 4px;
						}
						input[type=text]:focus {
							background-color: light blue;
						}
						input[type=submit]{
							background-color: #ffd800;
							color: white;
							margin-top: 25px;
						}
					</style>
                    <title>""" + title + """</title>
                    <meta charset="utf-8" />
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page

n_queries=0
i=0
c=0
d=0
f=0
e=0
g=0
h=0
ı=0
k=0
m=0
s=0
v=0
def a3_homepage():
	content='''
		<form action="/index/" method="POST">
			Name: <input name="name" type="text"/></br>
			Surname: <input surname="surname" type="text" /></br>
			<input value="Login" type="submit" />
		</form>
	'''
	return htmlify("Welcome!", content)
def StaticFile(filename):
	return static_file(filename, root="static")
l=[]
def a3_index():
	global name
	global surname
	name =request.POST.getall('name')
	surname =request.POST.getall('surname')
	global l
	l = [] + [name[0]]
	if name == ['buse']:
		return "Thanks for creating me :))"
	content = "<h2>Choose One of These Four Category " + l[0] +". " "</h2><br>" +\
	'''
		<p>
			<ol>
				<li><a href="/eating/"> Eating </li>
				<li><a href="/travelling/"> Travelling </li>
				<li><a href="/holiday/"> Holiday </li>
				<li><a href="/animal/"> Animal </li>
			<ol>
		</p>
	'''
	return htmlify("Pop Quiz", content)
def a3_eating():		
	content= '''
	<form action="/final/" method="POST">
		<input type="radio" name="eating" value="Pizza"/>Pizza<br>
		<input type="radio" name="eating" value="Hamburger" />Hamburger<br>
		<input type="radio" name="eating" value="Pasta" /> Pasta<br>
		<input type="submit" value="Submit" />
	</form>
	'''
	return htmlify("Eating", content)
def a3_travelling():
	content='''
	<form action="/final/" method="POST">
		<input type="checkbox" name="travelling" value="ship"/>Travelling with ship <br>
		<input type="checkbox" name="travelling" value="plane" />Traveling with plane <br>
		<input type="checkbox" name="travelling" value="bus" />Travelling with bus <br>
		<input type="submit" value="Submit">
	</form>
	'''
	return htmlify("Travelling", content)
def a3_holiday():
	content='''
	<form action="/final/" method="POST">
		<input type="radio" name="holiday" value="culture"/> Culture Holiday<br>
		<input type="radio" name="holiday" value="sea"/> Sea Holiday <br>
		<input type="radio" name="holiday" value="ski" /> Skiing Holiday <br>
		<input type="submit" value="Submit">
	</form>
	'''
	return htmlify("Holiday" , content)
def a3_animal():
	content='''
		<form action="/final/" method="POST">
			<input type="checkbox" name="animal" value="bird"/> Bird <br>
			<input type="checkbox" name="animal" value="cat"/> Cat <br>
			<input type="checkbox" name="animal" value="dog" /> Dog <br>
			<input type="submit" value="Submit">
		</form>
	'''
	return htmlify("Animal", content)
def a3_final():
	travelling= request.forms.get('travelling')
	holiday= request.forms.get('holiday')
	eating= request.forms.get('eating')
	animal= request.forms.get('animal')
	tra = ["ship" , "plane" , "bus"]
	ho = [ "sea", "culture" , "ski" ]
	eat = ["Pizza", "Pasta", "Hamburger"]
	ani= ["bird", "cat" , "dog"]
	content=""
	if travelling in tra:
		if travelling==tra[0]:
			global n_queries
			n_queries +=1
			x= str(n_queries)
			content = "<p>" "Ship" + " takes" +  " "+ x + " votes!" "</p><br>"
		elif travelling==tra[1]:
			global c
			c+=1
			y = str(c)
			content = "<p>" "Plane" + " takes" + " "+ y + " votes!" "</p><br>"
		else:
			global i
			i+=1
			z= str(i)
			content = "<p>" "Bus" + " takes" + " " + z + " votes!" "</p><br>"
	elif holiday in ho :
		if holiday==ho[0]:
			global d
			d+=1
			w = str(d)
			content = "<p>" "Sea" + " takes" + " " + w + " votes!" "</p><br>"
		elif holiday==ho[1]:
			global e
			e+=1
			q = str(e)
			content = "<p>" "Culture" + " takes" + " " + q + " votes!" "</p><br>"
		else:
			global f
			f+=1
			p = str(f)
			content = "<p>" "Ski" + " takes" + " " + p + " votes!" "</p><br>"
	elif eating in eat:
		if eating==eat[0]:
			global g
			g+=1
			ü = str(g)
			content = "<p>" "Pizza" + " takes" + " " + ü + " votes!" "</p><br>"
		elif eating==eat[1]:
			global h
			h+=1
			ç = str(h)
			content = "<p>" "Pasta" + " takes" + " " + ç + " votes!" "</p><br>"
		else:
			global va
			v+=1
			ö = str(v)
			content = "<p>" "Hamburger" + " takes" + " " + ö + " votes!" "</p><br>"
	elif animal in ani:
		if animal==ani[0]:
			global k
			k+=1
			ğ = str(k)
			content = "<p>" "Bird" + " takes" + " " + ğ + " votes!" "</p><br>"
		elif animal==ani[1]:
			global m
			m+=1
			n = str(m)
			content = "<p>" "Cat" + " takes" + " " + n + " votes!" "</p><br>"
		else:
			global s
			s+=1
			j = str(s)
			content = "<p>" "Dog" + " takes" + " " + j + " votes!" "</p><br>"
	else:
		content= "Please choose one option."
	return htmlify("Ratings",content)

def website_index():
	return htmlify('My lovely homepage',
				   """
				   <p><a href="/assignment1/">Click for my assignment1.</a></p>
				   <p><a href="/assignment2/a2_output.html">Click for my assignment2.</a></p>
				   <p><a href="/assignment3/">Click for my assignment3.</a></p>
                   """)
route('/','GET', website_index)
route('/assignment3/','GET',a3_homepage)
route('/index/', ['GET','POST'],a3_index)
route('/travelling/','GET', a3_travelling)
route('/eating/','GET', a3_eating)
route('/holiday/','GET', a3_holiday)
route('/animal/','GET', a3_animal)
route('/final/','POST', a3_final)
route("/static/<filename>", "GET", StaticFile)




#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on PythonAnywhere
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
