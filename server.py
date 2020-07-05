from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html') 

@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename) 

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', mode='a') as database:
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as database2:   
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
        csv_writer.writerow([email,subject,message])  

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() 
        # write_to_file(data)
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try Again'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')   

# @app.route('/components.html')
# def components():
#     return render_template('components.html')   

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')    

# @app.route('/work.html')
# def work():
#     return render_template('work.html')   

# @app.route('/works.html')
# def works():
#     return render_template('works.html')                







# @app.route('/')
# def hello_world():
#     return 'Hello, Sujeet!'

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/blob')
# def blob():
#     return 'welcome to blob part'  

# @app.route('/blob/2020/dogs')
# def blob2():
#     return 'this is a dog'  

# @app.route('/<username>/<int:post_id>')
# def variable_rules(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)     

             