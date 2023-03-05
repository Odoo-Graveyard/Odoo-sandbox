from odoo import http


class MyController(http.Controller):
    @http.route('/test', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('hina_web.home_page')
