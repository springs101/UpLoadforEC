# forms.py
from django import forms

class UploadFileForm2(forms.Form):
    file1 = forms.FileField(label="钻展-单品：")