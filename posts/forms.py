from django import forms
from .models import Post  # 우리가 사용할 modelform
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': '제목 입력'}),
            'content': forms.Textarea(attrs={'placeholder': '내용입력'})
        }
        # 사전형 변수, 필드이름을 key로 적용할 위젯을 값으로 함
        # attrs --> 사전형 / 'class':'title' 은 form.css 속성

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다')

        return title
