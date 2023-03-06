from odoo import http


class MyController(http.Controller):
    @http.route('/test', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('hina_web.home_page')

    # @http.route('/test2', auth='public', website=True)
    # def home2(self, **kw):
    #     return http.request.render('hina_web.home_page2')
