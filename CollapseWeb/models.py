import os
from io import BytesIO

from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image

from Core.settings import MEDIA_ROOT


def optimize_image(image, filename):
    file_extension = os.path.splitext(os.path.basename(filename))[1]

    if file_extension == '.gif':
        return image

    img = Image.open(image)

    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    img.thumbnail((512, 512))
    output = BytesIO()
    img.save(output, format='WEBP', quality=80)
    output.seek(0)
    return output

def image_file(instance, f):
    if os.path.splitext(os.path.basename(instance.image.path))[1] == '.gif':
        filename = mark_safe('clients/image/' + instance.name.replace(' ', '_') + '_' + instance.version + '.gif')
    else:
        filename = mark_safe('clients/image/' + instance.name.replace(' ', '_') + '_' + instance.version + '.webp')
        filename = ''.join(c for c in filename if c not in '()<>')
        
    if os.path.exists(MEDIA_ROOT + '/' + filename):
        os.remove(MEDIA_ROOT + '/' + filename)
        return filename
    
    return filename

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='Client', max_length=250, help_text='client name')
    version = models.CharField(default='1.16.5', max_length=250, help_text='client version, 1.12.2 or 1.16.5')
    filename = models.CharField(default='Client.jar', help_text='client filename on cdn', max_length=250)
    main_class = models.CharField(default='net.minecraft.client.main.Main', help_text='main class of jar', max_length=250)
    show_in_loader = models.BooleanField(default=True, help_text='whether the client is shown in loader')
    working = models.BooleanField(default=True, help_text='whether the client is running')
    internal = models.BooleanField(default=False, help_text='whether the client will use its own libraries and natives')
    fabric = models.BooleanField(default=False, help_text='whether the client is a fabric client')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.version}"
    
    class Meta:
        verbose_name_plural = "Clients in loader"
        ordering = ['-id']

class FabricClient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='Fabric Client', max_length=250, help_text='client name')
    version = models.CharField(default='1.21', max_length=250, help_text='client version, 1.12.2 or 1.16.5')
    filename = models.CharField(default='Client.jar', help_text='mod filename on cdn', max_length=250)
    show_in_loader = models.BooleanField(default=True, help_text='whether the client is shown in loader')
    working = models.BooleanField(default=True, help_text='whether the client is running')
    fabric = models.BooleanField(default=True, help_text='whether the client is a fabric client')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.version}"
    
    class Meta:
        verbose_name_plural = "Fabric Clients in loader"
        ordering = ['-id']

TYPE_CHOICES = (
    ('info','Info'),
    ('warn', 'Warn'),
    ('maintenance','Maintenance')
)

class Message(models.Model):
    id = models.AutoField(primary_key=True)

    body = models.TextField(default='Added new client', help_text='Body of message')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='info')
    hidden = models.BooleanField(default=False, help_text='whether the message is hidden')

    post_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

class Config(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='config_files', help_text='client config file', max_length=250)
    server = models.CharField(max_length=250, help_text='server', default='-')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, help_text='client', related_name='config')
    config_path = models.CharField(max_length=250, help_text='config path in client', default='configs/')

    def __str__(self):
        return f"{self.client.name} - {self.file}"
    
    @property
    def filename(self):
        return os.path.basename(self.file.name)