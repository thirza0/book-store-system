from django import forms

from .models import Book, Tag


class BookForm(forms.ModelForm):
    # forms.ModelMultipleChoiceField
    #       ManyToManyField
    # tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    class Meta:
        fields = '__all__'
        model = Book

    def __init__(self, *args, **kwargs):
        
        super(BookForm, self).__init__(*args, **kwargs)
        
        self.fields["tags"].widget = forms.CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()
