# forms.py
from django import forms

class UploadFileForm3(forms.Form):
    file1 = forms.FileField(label="钻展-全店：")