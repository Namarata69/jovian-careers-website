from flask import Flask, render_template #flask is module and Flask is class
app = Flask(__name__) #We create an object of the class
#Now, we need to create a route for our application
#route is simply the part of url after the domain name
JOBS=[
  {'id':1,
  'title': 'Bussiness Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'},
  {'id':2,
  'title': 'Data Analyst',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'},
  {'id':3,
  'title': 'Data Scientist',
  'location': 'Remote'},
  {'id':4,
   'title': 'Data Engineer',
   'location': 'Mumbai, India',
   'salary': 'Rs. 12,00,000'
   }
]

@app.route('/') #This is a decorator
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug="True")