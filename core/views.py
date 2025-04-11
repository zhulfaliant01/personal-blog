from django.shortcuts import redirect
from django.views import View

class RootView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')   
        else:
            return redirect('login') 