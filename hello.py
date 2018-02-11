from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we are running the file
                                          # directly, or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return render_template('index.html')

@app.route('/start')
def start():
  return render_template('start.html')

@app.route('/riddle')
def riddle():
  return render_template('riddle.html')

@app.route('/trust')
def trust():
  return render_template('trust.html')

@app.route('/paperclip')
def paperclip():
  return render_template('paperclip.html')

@app.route('/3+doors')
def doors():
  return render_template('3+doors.html')

@app.route('/death')
def death():
  return render_template('death.html')

@app.route('/end')
def end():
  return render_template('end.html')

app.run(debug=True)      # Run the app in debug mode