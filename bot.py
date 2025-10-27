from flask import Flask, redirect, render_template_string

app = Flask(__name__)

# ✅ Homepage (default)
@app.route('/')
def home():
    return render_template_string('''
        <h1>🚀 Guruji Ads Portal</h1>
        <p>Select any ad below:</p>
        <ul>
            <li><a href="/ads1">Watch Ad 1</a></li>
            <li><a href="/ads2">Watch Ad 2</a></li>
            <li><a href="/ads3">Watch Ad 3</a></li>
        </ul>
    ''')

# ✅ Ad pages (redirect to external URLs)
@app.route('/ads1')
def ad1():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # replace with your ad link

@app.route('/ads2')
def ad2():
    return redirect("https://www.example.com/ad2")  # replace with your link

@app.route('/ads3')
def ad3():
    return redirect("https://www.example.com/ad3")  # replace with your link

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
