from django import forms

class searchForm(forms.Form):
    search=forms.CharField(lable='Your name',max_length=100)
    