from protocols.models import Protocol, Tag, ProtocolForm
from django.contrib import admin
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
admin.autodiscover()

def index(request):
    tag_list = Tag.objects.all().order_by('name')[:5]
    return render_to_response('protocols/index.html', {'tag_list': tag_list})

def tags(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    protocol_list = Protocol.objects.all().filter(tags=tag)
    return render_to_response('protocols/tag_detail.html', {'protocol_list': protocol_list})

def detail(request, protocol_id):
    p = get_object_or_404(Protocol, pk=protocol_id)
    return render_to_response('protocols/template.html', {'protocol': p},context_instance=RequestContext(request),)

def add_protocol(request):
    if request.method == 'POST':
        form = ProtocolForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        form = ProtocolForm()

    return render_to_response('protocols/add_protocol.html', {
        'form':form,
    },context_instance=RequestContext(request),)

def view_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    protocol_list = Protocol.objects.all().filter(author=user)
    return render_to_response('protocols/user.html', {'user': p},context_instance=RequestContext(request),)