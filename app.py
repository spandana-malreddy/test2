from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Simple authentication logic
    if username == 'sample' and password == 'password':
        response_data = '<response><message>Welcome, ' + username + '!</message></response>'
    else:
        response_data = '<response><message>Authentication failed</message></response>'

    # Return XML response
    return Response(response_data, content_type='application/xml')

if __name__ == '__main__':
    app.run(debug=True)