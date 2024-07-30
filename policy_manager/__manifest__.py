{
    'name': 'Policy Generator',
    'version': '1.0',
    'summary': 'Manage company details and generate policy documents',
    'description': """
        The Policy generator module allows users to input company details and generate 
        policy documents based on a predefined template. The generated policies can 
        be downloaded or saved as needed.
    """,
    'author': 'Vidhema technology',
    'website': 'https://vidhema.com',
    'category': 'Business',
    'depends': ['base'],
    'data': [        
        'security/ir.model.access.csv',
        'views/policy_action.xml',
        'views/policy_menu.xml',                
        'views/policy_template.xml',
        'views/policy_view.xml',                  
    ],
    "images":[
        'static/description/banner3.gif'
    ],
    'assets': {
        'web.assets_backend': [
            'policy_manager/static/src/css/policy_template.css',
        ],
         'web.assets_frontend': [
            'policy_manager/static/src/js/policy_manager.js',
        ],
    },
    "images":[
        'static/description/banner1.gif'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,

}





