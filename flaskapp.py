from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'


clockStateButton = 0


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    global clockStateButton
    if request.method == "POST":
        try:
            clockStateButton = int(request.form.get("clockStateButton"))
            print('this is the clockStateButton named clockStateButton: ',clockStateButton)
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for clockStateButton")
        return redirect(url_for('index'))
    return render_template('index.html', clockStateButton=clockStateButton)
    

def flaskRunner():

    app.run()
    
    

