from django.shortcuts import render
from django.views import View
import pyrebase

config={
    "apiKey": "AIzaSyAZlJ3wVIPqghyFSRO7uwFi9ueRwj38FJU",
    "authDomain": "coursematch-9c80a.firebaseapp.com",
    "databaseURL": "https://coursematch-9c80a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "coursematch-9c80a",
    "storageBucket": "coursematch-9c80a.appspot.com",
    "messagingSenderId": "241564717139",
    "appId": "1:241564717139:web:5f82de325c2fa5d65a36a6",
    "measurementId": "G-892697DN9C",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

# Create your views here.
class indexView(View):
    template_name="main/index.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        email = request.POST.get('email')
        psw = request.POST.get('psw')

        try:
            auth.sign_in_with_email_and_password(email, psw)
            print("success!")
        except:
            print("invalid credentials")
        
        return render(request, self.template_name)