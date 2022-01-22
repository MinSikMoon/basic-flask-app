from asyncio.base_futures import _format_callbacks


from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'hello python'