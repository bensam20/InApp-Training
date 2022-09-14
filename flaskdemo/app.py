#importing Flask class from flask library
from flask import Flask, redirect, url_for, request, jsonify, abort
import requests

#creating an application instance
#the argument for the constructor is the main module name
#main module  name will be there in the dunder __name__
app = Flask(__name__)


#defining a route  in flask using the app.route decorator
#app is our flask application object
#/ is the root of the website, like the index.html in html
#greet() function will be executed when accessing default route
@app.route('/')
def greet():
    return 'Have a Good Day'

@app.route('/hello')
def hello():
    return '<h1>Hi Hello World!!</h1>'


#demonstrate dynamid url building in flask
@app.route('/admin')
def welcome_admin():
    return 'Welcome admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'<h2> Hello {guest} You are our guest</h2>'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/mylogin', methods=['POST'])
def mylogin():
    username = request.form['username']
    password = request.form['password']
    if username == 'abhi' and password == 'abhipass':
        return 'Welcome %s'%username
    else:
        return 'Username or password is not valid'



#list of dictionaries for demonstrating REST API methods
#'id' field should be id itself because there is a built in fn which process it
books = [{'id':1,'title':'Harry Potter', 'author':'JK Rowling'},
        {'id':2,'title':'Jungle Book', 'author':'Rudyard Kipling'},
        {'id':3,'title':'Alice in Wonderland', 'author':'Lewis Carroll'}]


# GET request to get the data in json format
@app.route('/books', methods=['GET'])
def get_books():
    #jsonify will convert dictionary to json
    return jsonify({'books':books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    #List comprehension, iterate through a list and obtain a sublist
    book = [book for book in books if book['id']==book_id]
    if len(book) == 0:
        abort(404)
    else:
        return jsonify({'books':book[0]})


# POST request to save the data into the list
@app.route('/books', methods=['POST'])
def create_book():
    #checking if the string is a valid json
    if not request.json:
        abort(400) #400 means a bad request
    # create a new book as an item which can be inserted into the list
    # the id will be the next id number, use negative index for the last item
    book = {'id':books[-1]['id']+1,
    'title':request.json['title'],
    'author':request.json['author']}
    #append the new item into the books list
    books.append(book)
    #jsonify will convert dictionary to json
    return jsonify({'book':book}),201


#PUT request to edit the data
@app.route('/books/<int:book_id>', methods=['PUT'])
def upadate_book(book_id):
    #List comprehension, iterate through a list and obtain a sublist
    book = [book for book in books if book['id']==book_id]
    if len(book) == 0:
        abort(404)
    #checking if the json from the client has valid title, author keys
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'author' in request.json and type(request.json['author']) != str:
        abort(400)

    # if no abort conditions occur, update the entry with the specific id
    book[0]['title'] = request.json['title']
    book[0]['author'] = request.json['author']

    #return the updated record
    return jsonify({'books':book[0]})


#DELETE request to delete the data
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    #List comprehension, iterate through a list and obtain a sublist
    book = [book for book in books if book['id']==book_id]
    if len(book) == 0:
        abort(404)

    #remove that item from the list
    books.remove(book[0])

    #return the status
    return jsonify({'status':'deleted'})


#install a module called requests to send the API request
#using the command pip install requests
#defining the API url
API_URL = ('https://api.genderize.io/?name={}')

#createw a new function for sending the api requeset to the url
def send_api(name):
    print(API_URL)
    #trying to send the api request using requsts.get() method
    try:
        data = requests.get(API_URL.format(name)).json()
    except Exception as exec:
        print(exec)
        data = None
    return data

#if we are using browser, default http method will be GET
@app.route('/gender/<name>')
def gender(name):
    #call the send_api method and pass the name and receive the response
    response = send_api(name)
    return_text = "Your name "+ response['name']+" is "+response["gender"]
    return return_text

 


#check if its the main module, then run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)