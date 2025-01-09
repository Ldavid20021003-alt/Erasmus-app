from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Minta adatok
events = [
    {"id": 1, "title": "Ifjúsági csere - Spanyolország", "date": "2025-02-15"},
    {"id": 2, "title": "Képzés - Németország", "date": "2025-03-10"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def list_events():
    return render_template('events.html', events=events)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # Pályázati adatok kezelése
        form_data = request.form
        return f"Pályázat sikeresen elküldve: {form_data['name']}"
    return render_template('submit_form.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', user={"name": "Példa Felhasználó", "email": "user@example.com"})

if __name__ == '__main__':
    app.run(debug=True)