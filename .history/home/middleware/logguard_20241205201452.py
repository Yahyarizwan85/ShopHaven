def auth_middleware(get_response):
    
    
    def middleware(request):
        if not request.session.get('cus')
            response = get_response(request)
            return response
        
     
    return middleware
    