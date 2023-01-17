def Typeuse(request):
    if request.method == 'post':
        usertype = request.POST.get('user_type')
        usertype = authenticate(request,usertype)
        if usertype == 'farmer':
            return render(' farmerdashboard.html')
        elif usertype == 'investor':
            return render('investordashboard.html')
        else:
            return redirect('login')