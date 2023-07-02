from django import forms
from .models import Post,Category

choices = [('coding','coding'),('linux','linux'),('How to','How to')]

cats = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','title_tag', 'author','category','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a title place holder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cats,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }






class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','title_tag', 'author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a title place holder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

