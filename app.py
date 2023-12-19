from flask import Flask, render_template

app = Flask(__name__)

# Sample data
items = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def item_list():
    return render_template('item_list.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)