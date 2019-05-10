# forms.py
from django import forms

class UploadFileForm1(forms.Form):
    file1 = forms.FileField(label="直通车：")