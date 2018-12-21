def getData(request):
    login_uname = request.session.get('login_uname','')
    return {'login_uname':login_uname}