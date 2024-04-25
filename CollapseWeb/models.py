import os

from django.db import models
from django.utils.safestring import mark_safe


def image_file(instance, filename):
    image_filename = os.path.basename(instance.image.name)
    file_extension = os.path.splitext(image_filename)[1]

    return mark_safe('clients/image/' + instance.name.replace(' ', '_') + '_' + instance.version + file_extension)

class Client(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(default='Client', max_length=250, help_text='client name')

    version = models.CharField(default='1.16.5', max_length=250, help_text='client version, 1.12.2 or 1.16.5')

    filename = models.CharField(default='Client.jar', help_text='client file name on <a href="https://console.cloud.google.com/storage/browser/collapseloader" target="_blank">google cloud</a>', max_length=250)
    
    image = models.FileField(upload_to=image_file, default='clients/image/unknown.png')

    main_class = models.CharField(default='net.minecraft.client.main.Main', max_length=250)

    internal = models.BooleanField(default=False, help_text='whether to use folders within the client')

    hidden = models.BooleanField(default=False, help_text='whether to hide client in api')

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.version}'

    class Meta:
        ordering = ['-id']