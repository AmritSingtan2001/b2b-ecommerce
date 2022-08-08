from django.shortcuts import redirect

def admin_required(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('account_login')
    return wrap