from users.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate


class SignUpView(APIView):
    def post(self, request):
        user = User.objects.create_user(age=request.data['age'], sex=request.data['sex'], phone=request.data['phone'],
                                        password=request.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        # 토큰을 뿌려줌 잘 활용해보자
        return Response({'Token': token.key})


class SignInView(APIView):
    def post(self, request):
        user = authenticate(phone=request.data['phone'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            print('Success')
            return Response({'Token': token.key})
        else:
            print('failed')
            return Response(status=401)
