from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def index(request):


    '''
    msg=EmailMessage('file','sending a file','sriharshanagulakonda@gmail.com',['jayakrishna7878@gmail.com'])
    msg.attach_file('/polls/detail.html')
    msg.send()
    
    for i in range(1,6):
        send_mail(
            'Hii raa edava',
            'edava  '+str(i),
            'sriharshanagulakonda@gmail.com',
        ['hemanthnambu@gmail.com'],
            fail_silently=False,
        )
    '''


    latest_question_list=Question.objects.order_by('pub_date')
    #template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    #output="\n".join([str(q.id)+" "+str(q) for q in latest_question_list])
    return  HttpResponse('hii')#template.render(context,request))
    #return render(request,'polls/index.html',context)




def admin(request):
    return render(request,'admin/admin.html')
    #HttpResponse("<I'm admin</b>")

def add_question(request):
    return render(request,'admin/add_question.html')
    #HttpResponse('add question here')

def insert_question(request):
    try:
        #selected_choice=question.choice_set.get(pk=request.POST['choice'])
        q=Question(question_text=request.POST['question'],pub_date=timezone.now())
        x=q
        q.save()
        for i in range(1,4):
            x.choice_set.create(choice_text=request.POST['choice'+str(i)],votes=0)

    except Exception as e:
        q.delete()
        return render(request,'admin/add_question.html',{
            'error_message':e,#"You didn't selected a choice",
        })
    else:
        x.save()
        return HttpResponse('''
        question inserted''')

def edit_question(request):
    latest_question_list=Question.objects.all()
    return render(request,'admin/edit.html',{'latest_question_list':latest_question_list})


def change_question(request,question_id):
    question=Question.objects.get(pk=question_id)
    return render(request,'admin/change.html',{'question':question})

def update(request,question_id):
    q=get_object_or_404(Question,pk=question_id)
    q.question_text=request.POST['question']
    q.save()
    j=1
    for i in q.choice_set.all():
        i.choice_text=request.POST['choice'+str(j)]
        j+=1
        i.save()
    return HttpResponse('updated')




def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse("You are looking at %s." % question_id)



def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

    #response="You are looking at results of question %s."
    #return HttpResponse(response % question_id)



def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't selected a choice",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        #return HttpResponse("You're voting on question %s." % question_id)







'''
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name='polls/results.html'

'''