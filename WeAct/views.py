from flask import Flask
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'WeAct 해외 봉사 도움 어플리케이션에 오신 것을 환영합니다'
