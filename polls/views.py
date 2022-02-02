from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

@api_view(['GET'])
def get_questions(request):
    """
    Get the list of questions on our website
    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_question(request, pk):
    """
    Get the list of questions on our website
    """
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, data=request.data, partial=True)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)