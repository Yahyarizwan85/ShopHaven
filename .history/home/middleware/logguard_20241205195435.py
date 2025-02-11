def auth_middleware(get_response):
    
    
    def middleware(request):
        if request.user.is_authenticated:
            response = get_response(request)
            return response
        
     
     return middleware
    