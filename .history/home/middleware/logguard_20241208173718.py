from django.shortcuts import redirect

def auth_middleware(get_response):
    def middleware(request):
        returnUrl = ""
        print(request.class Meta
            verbose_name_plural = 'ModelNames')
        # If the user is not logged in, redirect to login page
        if not request.session.get('customer_id'):
            return redirect('login')
        
        # Otherwise, proceed with the normal response
        response = get_response(request)
        return response

    return middleware
