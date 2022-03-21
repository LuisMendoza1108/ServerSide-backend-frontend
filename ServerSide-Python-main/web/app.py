from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from logic.Document import Document
from logic.person import Author

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
authors = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/document', methods=['GET'])
def person():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def person_detail():
    id_document = request.form['id_document']
    title = request.form['title']
    number_of_pages = request.form['number_of_pages']
    category = request.form['category']

    authors = [Author(id_author=request.form['id_author'],
                      name_author=request.form['name_author'],
                      last_name_author=request.form['last_name_author'])]

    p = Document(id_document=id_document, number_of_pages=number_of_pages, title=title, category=category,
                 authors=authors)
    model.append(p)
    return render_template('document_detail.html', value=p)


@app.route('/documents')
def document():
    data = [(i.id_document,
             i.title,
             i.number_of_pages,
             i.category,
             i.authors[0].name + '  ' + i.authors[0].last_name) for i in model]
    print(data)
    return render_template('documents.html', value=data)


@app.route('/authors')
def authors():
    data_1 = [(i.authors[0].id_person,
               i.authors[0].name,
               i.authors[0].last_name,
               i.id_document)
              for i in model]
    print(data_1)
    return render_template('authors.html', value=data_1)


if __name__ == '__main__':
    app.run()
