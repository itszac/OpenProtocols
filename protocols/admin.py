from django.contrib import admin

from protocols.models import Protocol, Step, Tag, UserProfile, Comment, Media, Material

admin.site.register(Protocol)
admin.site.register(Step)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(Material)