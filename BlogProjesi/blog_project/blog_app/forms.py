from django import forms
from blog_app.models import Blog

class AddBlogForm(forms.Form):
    nickname_input = forms.CharField(label="Username",max_length=50)
    message_input=forms.CharField(label="Message",max_length=100,
                                  widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    
