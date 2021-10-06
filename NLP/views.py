import nlp

from users.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate


class PostSentence(APIView):
    def post(self, request):
        #post에 key=sentence, value=값을 담아서 보냄
        sentence = request.data['sentence']
        nlp.tokenizer(sentence)

        # 토큰을 뿌려줌 잘 활용해보자
        return Response({'Success POST'})


class GetText(APIView):
    def post(self, request):
        user = authenticate(phone=request.data['phone'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            print('Success')
            return Response({'Token': token.key})
        else:
            print('failed')
            return Response(status=401)

# class PostOrder:
