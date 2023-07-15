from django.shortcuts import render
from django.views import View
import pyrebase

config={
  "apiKey": "AIzaSyCljBmvAw4Ot48uTyb41IVZhBwO_QRtZc8",
  "authDomain": "coursematch-5a396.firebaseapp.com",
  "databaseURL": "https://coursematch-5a396-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "coursematch-5a396",
  "storageBucket": "coursematch-5a396.appspot.com",
  "messagingSenderId": "769922977544",
  "appId": "1:769922977544:web:0730ee51cd69e8812de6bd",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
class indexView(View):
    template_name="students/index.html"

    def get(self, request):
    #     student_first_name = database.child('Students').child('First Name').get().val()
    #     student_last_name = database.child('Students').child('Last Name').get().val()

    #     return render(request, self.template_name, {'student_first_name': student_first_name, 'student_last_name': student_last_name})

            return render(request, self.template_name)

def signin(request):
    return render(request, "students/signIn.html");

def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message="Invalid credentials"
        return render(request,"students/signIn.html", {"message":message})
    print(user)
    session_id = user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "students/postSign.html", {"e":email});

def logout(request):
    pass