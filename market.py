from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form.get('name')
    price = request.form.get('price')
    barcode = request.form.get('barcode')
    description = request.form.get('description')
    new_item = Item(name=name, price=price, barcode=barcode, description=description)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('market_page'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)