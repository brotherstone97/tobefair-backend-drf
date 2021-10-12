from . import nlp

from rest_framework.response import Response
from rest_framework.views import APIView


class PostSentence(APIView):
    def post(self, request):
        # post에 key=sentence, value=값을 담아서 보냄
        sentence = request.data['sentence']
        result = nlp.extract(sentence)
        return Response(result)
    # def get(self, response):


# class GetText(APIView):
#     def post(self, request):
#         user = authenticate(phone=request.data['phone'], password=request.data['password'])
#         if user is not None:
#             token = Token.objects.get(user=user)
#             print('Success')
#             return Response({'Token': token.key})
#         else:
#             print('failed')
#             return Response(status=401)

# class PostOrder:
