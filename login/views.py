from django.shortcuts import render
def login(request):
    return render(request,'login.html')
# Create your views here.
# def login_views(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(request, username = username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/login/dashboard')
#     return render(request, 'login/login_view.html')