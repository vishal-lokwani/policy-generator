from odoo import http
import requests

class PolicyController(http.Controller):
    @http.route('/policy/view/<model("policy.manager"):policy>', auth='user')
    def view_policy(self, policy, **kw):
        return http.request.render('policy_manager.report_policy_document', {
            'docs': policy
        })
    
    # @http.route('/api/countries', auth='public', type='json', methods=['GET'])
    # def get_countries(self, **kwargs):
    #     # Fetch the access token
    #     response = requests.get(
    #         "https://www.universal-tutorial.com/api/getaccesstoken",
    #         headers={
    #             "Accept": "application/json",
    #             "api-token": "RrFEbCsJWq7xCBok9wfenEwlKN4UkUrP7lu2V3iVgOzBVWosRK0OccST3CsT4OU76K0",
    #             "user-email": "pukhrajkumawat048@gmail.com"
    #         }
    #     )
    #     token = response.json().get('auth_token')

    #     # Fetch countries
    #     response = requests.get(
    #         "https://www.universal-tutorial.com/api/countries/",
    #         headers={
    #             "Accept": "application/json",
    #             "Authorization": f"Bearer {token}"
    #         }
    #     )
    #     countries = response.json()

    #     return {'countries': countries}
