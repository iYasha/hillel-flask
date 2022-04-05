from flask import Flask

app = Flask(__name__)

"""
https://code.visualstudio.com/docs/supporting/faq - ссылка

https - протокол
code.visualstudio.com - домен
/docs/supporting/faq - путь (route)
"""

articles = [
	{
		'id': 1,
		'title': 'Article 1',
		'description': 'Description 1',
	},
	{
		'id': 2,
		'title': 'Article 2',
		'description': 'Description 2',
	},
	{
		'id': 3,
		'title': 'Article 3',
		'description': 'Description 3',
	},
]


@app.route('/')
def home_page():
	with open('html/index.html', 'r') as f:
		return f.read()


@app.route('/articles')
def get_all_articles():
	response = ''
	for article in articles:
		response += f'<a href="/article/{article["id"]}"><h1>{article["title"]}</h1></a><p>{article["description"]}</p>'
	return response


@app.route('/article/<int:id>')
def get_article(id: int):
	for article in articles:
		if article['id'] == id:
			return f'<h1>{article["title"]}</h1><p>{article["description"]}</p>'
	return '<p style="color:red;">Article not found</p>'


@app.route('/delete-article/<int:id>')
def delete_article(id: int):
	global articles
	index_for_delete = None
	for idx, article in enumerate(articles):
		if article['id'] == id:
			index_for_delete = idx
			break
	if index_for_delete is not None:
		del articles[index_for_delete]
		return 'Успешно удалено'
	else:
		return '<p style="color:red;">Article not found</p>'


@app.route('/<string:first>/<int:second>')
def get_sum(first: str, second: int):
	print(type(first), type(second))
	return first


app.run('localhost', 8000)


"""
Задание:
Создать глобальную переменную ALL_USERS в которую поместить 4 пользователя
Нужно написать два запроса /users и /user/<id>
Первый запрос должен возвращать список всех пользователей
Второй запрос должен возвращать пользователя с заданным id
"""
