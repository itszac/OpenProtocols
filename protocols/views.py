# Create your views here.

from django.contrib.auth.models import User
from protocols.models import Document, Protocol, Step, Tag, UserProfile, Comment, Media
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from protocols.forms import *
from datetime import datetime

def index(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('index.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            pass
            # Return a 'disabled account' error message
    else:
        pass
        # Return an 'invalid login' error message.
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('index.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('index.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def protocol_detail(request, protocol_id):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    protocol = Protocol.objects.get(id = protocol_id)
    steps = Step.objects.filter(protocol = protocol)
    materials = protocol.materials.all()
    protocol_comments = Comment.objects.filter(document = protocol)
    protocol_tags = Tag.objects.filter(protocol = protocol)
    step_comments = []
    for step in steps:
        step_comments.append(Comment.objects.filter(document = step))
    steps = zip(steps,step_comments)
    return render_to_response('protocol_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "protocol": protocol, 
        "steps": steps, 'materials':materials, "protocol_comments":protocol_comments, 
        "step_comments": step_comments, "protocol_tags":protocol_tags},
        context_instance=RequestContext(request))

def protocol_new(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ProtocolForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            user = request.user
            p = Protocol(name = name, description = description, author = user, date_created = datetime.now())
            return HttpResponseRedirect('') # Redirect after POST
    else:
        form = JoinForm() #unbound
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('protocol_new.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def tag_list(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('tag_list.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "tags": tags},
        context_instance=RequestContext(request))

def tag_detail(request, tag_name):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    tag = Tag.objects.get(name = tag_name)
    protocols = tag.protocol_set.all()
    return render_to_response('tag_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "tag": tag, "protocols": protocols},
        context_instance=RequestContext(request))

def user_detail(request, user_id):
    user = User.objects.get(id = user_id)
    user_protocols = Protocol.objects.filter(author = user)
    user_profile = UserProfile.objects.get(user = user)
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('user_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def user_new(request):
    if request.method == 'POST': # If the form has been submitted...
        form = JoinForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            profile = form.cleaned_data['profile']
            u = User.objects.create_user(username, email, password)
            u.save()
            p = UserProfile(user = u, profile = p)
            p.save()
            login(request, user)
            return HttpResponseRedirect('') # Redirect after POST
    else:
        form = JoinForm() #unbound
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('user_new.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

@csrf_exempt
def vote(request,document_id):
    document=Document.objects.get(pk=document_id)
    votes = document.vote_up()
    document.save()
    return HttpResponse(votes)

@csrf_exempt
def add_tag(request,protocol_id,tag):
    protocol=Protocol.objects.get(pk=protocol_id)
    tag = '_'.join(tag.split()).lower()
    tag, created = Tag.objects.get_or_create(name = tag)
    protocol.tags.add(tag)
    protocol.save()
    return HttpResponse(tag.name)

@csrf_exempt
def add_comment(request,document_id,tag):
    protocol=Document.objects.get(pk=document_id)
    comment = Comment(author = request.user, date_created = datetime.now(), 
        document = document, content = request.POST['comment'])
    comment.save()
    return HttpResponse(comment.content)