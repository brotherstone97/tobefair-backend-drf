from . import nlp

from rest_framework.response import Response
from rest_framework.views import APIView


class PostSentence(APIView):
    def post(self, request):
        # post에 key=sentence, value=값을 담아서 보냄
        sentence = request.data['sentence']
        result = nlp.extract(sentence)
        return Response(result)


