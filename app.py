from flask import Flask, render_template #flask is module and Flask is class
app = Flask(__name__) #We create an object of the class
#Now, we need to create a route for our application
#route is simply the part of url after the domain name
@app.route('/') #This is a decorator
def hello_jovian():
  return render_template('home.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug="True")