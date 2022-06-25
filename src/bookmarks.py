from flask import Blueprint, jsonify, request
import validators
from src.constants.http_status_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from src.database import Bookmark, db
from flask_jwt_extended import get_jwt_identity, jwt_required


bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

@bookmarks.route("/", methods=['POST','GET'])
@jwt_required()
def handle_bookmarks():
    current_user = get_jwt_identity()

    if request.method == 'POST':
        body = request.get_json().get('body', '')
        url = request.get_json().get('url', '')
    
        if not validators.url(url):
            return jsonify({
                'error': 'enter a valid URL!'
            }), HTTP_400_BAD_REQUEST
        
        if Bookmark.query.filter_by(url=url).first():
            return jsonify({
                'error': 'URL already exists!'
            }), HTTP_409_CONFLICT
        
        bookmark = Bookmark(url=url,body=body,user_id=current_user)
        db.session.add(bookmark)
        db.session.commit()

        return jsonify({
            'id': bookmark.id,
            'url': bookmark.url,
            'short_url': bookmark.short_url,
            'visits': bookmark.visits,
            'created_at': bookmark.created_at,
            'updated_at': bookmark.updated_at
        }), HTTP_201_CREATED
    
    else:
        page = request.args.get('page',1,type=int)
        per_page = request.args.get('per_page',1,type=int)

        bookmarks = Bookmark.query.filter_by(user_id=current_user).paginate(page=page,per_page=per_page)
        
        data = []
        for bookmark in bookmarks.items:
            data.append({
                'id': bookmark.id,
                'url': bookmark.url,
                'short_url': bookmark.short_url,
                'visits': bookmark.visits,
                'created_at': bookmark.created_at,
                'updated_at': bookmark.updated_at
            })
        
        meta = {
            'page': bookmarks.page,
            'pages': bookmarks.pages,
            'total': bookmarks.total,
            'prev_page': bookmarks.prev_num,
            'next_page': bookmarks.next_num,
            'has_prev': bookmarks.has_prev,
            'has_next': bookmarks.has_next
        }
        
        return jsonify({
            'data': data,
            'meta': meta
            }), HTTP_200_OK