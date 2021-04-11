
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            raw_password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('Home')
    loginform = AuthenticationForm()
    return render(request, 'registration/login.html', {'loginform': loginform})



