from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from blog.models import Post, Category


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'views']
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'created_at')
    save_on_top = True
    fields = ('title', 'category', 'content', 'photo', 'created_at')
    # readonly_fields = ('created_at',)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
