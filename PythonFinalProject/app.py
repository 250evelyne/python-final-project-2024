from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

# In-memory storage for simplicity (just for learning purposes)
users = {}
recipes = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')

        if action == 'login':

            if username in users and users[username] == password:
                session['username'] = username
                flash('Login successful!')
                return redirect('/dashboard')
            else:
                flash('Invalid login credentials. Please try again.')
        elif action == 'signup':

            if username in users:
                flash('Username already exists. Please choose a different one.')
            else:
                users[username] = password
                flash('Sign-up successful! Please log in.')

    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        flash('Please log in to access the dashboard.')
        return redirect('/')

    username = session['username']
    user_recipes = recipes.get(username, [])

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        user_recipes.append({'title': title, 'description': description})
        recipes[username] = user_recipes
        flash('Recipe added successfully!')

    return render_template('dashboard.html', recipes=user_recipes)


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
