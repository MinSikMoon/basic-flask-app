from asyncio.base_futures import _format_callbacks


from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello python'

@bp.route('/')
def index():
    return 'pybo index'
