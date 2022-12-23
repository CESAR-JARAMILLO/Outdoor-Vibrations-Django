from django.contrib import admin
from django import forms
from .models import BlogPost

class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm

admin.site.register(BlogPost, BlogPostAdmin)