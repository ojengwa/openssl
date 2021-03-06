from htmlmin import Minifier


class HTMLMIN(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)

        default_options = {
            'remove_comments': True,
            'reduce_empty_attributes': True,
            'remove_optional_attribute_quotes': False
        }
        default_options.update(kwargs)

        self.html_minify = Minifier(
            **default_options)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', True)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response.direct_passthrough = False

            raw_data = response.get_data(as_text=True)

            response.set_data(
                self.html_minify.minify(raw_data)
            )

            return response
        return response
