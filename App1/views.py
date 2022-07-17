import json

from App1.models  import User
from django.views import View
from django.http  import JsonResponse


class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)

        User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = data['phone_number']
        )

        return JsonResponse({"message":"Created"},status=201)

class LogInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if User.objects.filter(email=email,password=password):
                return JsonResponse({"message":"Success"},status=201)
            return JsonResponse({"message":"Error"},status=400)

        except KeyError:
            return JsonResponse({"message":"KeyError"},status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"message":"Your Fault,,, Try Again.."},status=400)

        