from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'


variable = 0


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    global variable
    if request.method == "POST":
        try:
            variable = int(request.form.get("variable"))
            print('this is the variable named variable: ',variable)
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for variable")
        return redirect(url_for('index'))
    return render_template('index.html', variable=variable)
    

def flaskRunner():

    app.run()
    
    

