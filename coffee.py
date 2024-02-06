from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract data from form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Process data (e.g., save it to a database or send an email)
        # For now, we'll just flash a message
        flash(f"Message from {name} ({email}) received: {message}")

        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
     app.run(debug=True)


