from django.shortcuts import re

def auth_middleware(get_response):
    
    
    def middleware(request):
        if not request.session.get('customer_id'):
            
            response = get_response(request)
            return response
        
     
    return middleware
    