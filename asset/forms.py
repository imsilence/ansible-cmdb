#encoding: utf-8

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Host

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'

    def clean_ip(self):
        ip = self.cleaned_data.get('ip', '')
        try:
            host = Host.objects.get(ip=ip)
            if self.instance is None or self.instance != host:
                raise forms.ValidationError('IP已存在')
        except ObjectDoesNotExist as e:
            pass

        return ip


    def clean_cpu(self):
        cpu = self.cleaned_data.get('cpu', '')
        try:
            cpu = int(cpu);
            if cpu < 1 or cpu > 256:
                raise forms.ValidationError('CPU范围必须为1-256(核)')
        except BaseException as e:
            raise forms.ValidationError('CPU范围必须为1-256(核)')

        return cpu


    def clean_mem(self):
        mem = self.cleaned_data.get('mem', '')
        try:
            mem = int(mem);
            if mem < 512 or mem > 1049600:
                raise forms.ValidationError('内存范围必须为512-1049600(M)')
        except BaseException as e:
            raise forms.ValidationError('内存范围必须为512-1049600(M)')

        return mem
