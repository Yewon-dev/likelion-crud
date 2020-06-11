from django import forms
from .models import Post


## 사용자로부터 데이터를 입력받는 form
## 날짜필드는 자동으로 추가되기때문에 field에 넣지 않아도 됨
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','body']