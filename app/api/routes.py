from app.api import bp
from app import db
from app.models import Article
from flask import request, url_for
import sqlalchemy as sa
from app.api.errors import bad_request


@bp.route('/articles/<int:id>', methods=['GET'])
def get_article(id: int):
    return db.get_or_404(Article, id).to_dict()


@bp.route('/articles', methods=['GET'])
def get_articles():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 10)
    return Article.to_collection_dict(sa.select(Article), page, per_page, 'api.get_articles')


@bp.route('/articles', methods=['POST'])
def create_article():
    data = request.get_json()
    if 'body' not in data or 'tags' not in data:
        return bad_request('article must include body and tags')
    
    article = Article()
    article.from_dict(data)
    db.session.add(article)
    db.session.commit()
    return article.to_dict(), 201, {'Location': url_for('api.get_article', id=article.id)}


@bp.route('/articles/<int:id>', methods=['DELETE'])
def delete_article(id: int):
    article = db.get_or_404(Article, id)
    db.session.delete(article)
    db.session.commit()
    return 204, {}


@bp.route('/articles/<int:id>', methods=['PUT'])
def update_article(id: int):
    article = db.get_or_404(Article, id)
    data = request.get_json()
    if 'body' not in data and 'tags' not in data:
        return bad_request('no changes included')
    article.from_dict(data)
    #db.session.add(article)
    db.session.commit()
    return article.to_dict()
