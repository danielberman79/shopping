from flask import Blueprint

from routes.base import locale, \
                        api_id, \
                        contentful, \
                        render_with_globals, \
                        raw_breadcrumbs, \
                        VIEWS_PATH
from routes.errors import wrap_errors
from lib.breadcrumbs import refine


index = Blueprint('index', __name__, template_folder=VIEWS_PATH)


@index.route('/')
@wrap_errors
def show_index():
    landing_page = contentful().landing_page('home', api_id(), locale().code)

    # TODO: Attach entry state

    return render_with_globals(
        'landingPage',
        landing_page=landing_page,
        breadcrumbs=refine(
            raw_breadcrumbs(),
            landing_page
        )
    )
