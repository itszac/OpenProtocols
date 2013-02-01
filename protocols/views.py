# Create your views here.

from django.contrib.auth.models import User
from protocols.models import Protocol, Step, Tag, UserProfile, Comment, Media
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('index.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def about(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('about.html', 
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
    step_comments = []
    for step in steps:
        step_comments.append(Comment.objects.filter(document = step))
    return render_to_response('protocol_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "protocol": protocol, 
        "steps": steps, 'materials':materials, "protocol_comments":protocol_comments, 
        "step_comments": step_comments},
        context_instance=RequestContext(request))

def protocol_new(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    tags = Tag.objects.all()
    return render_to_response('protocol_new.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def tag_list(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    tags = Tag.objects.all()
    return render_to_response('tag_list.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "tags": tags},
        context_instance=RequestContext(request))

def tag_detail(request, tag_id):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    tag = Tag.objects.get(name = name)
    protocols = tag.protocol_set.all()
    return render_to_response('tag_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, "tag": tag, "protocols": protocols},
        context_instance=RequestContext(request))

def user_detail(request, user_id):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('user_detail.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))

def user_new(request):
    recent_protocols = Protocol.objects.order_by('-date_created')[:5]
    popular_protocols = Protocol.objects.order_by('votes')[:5]
    tags = Tag.objects.all()
    return render_to_response('user_new.html', 
        {"tags": tags, "recent_protocols": recent_protocols, 
        "popular_protocols": popular_protocols, },
        context_instance=RequestContext(request))