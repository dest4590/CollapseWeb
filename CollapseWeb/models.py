import os

from django.db import models


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
    category = models.CharField(default='HVH', max_length=250, help_text='client category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.version}"
    
    class Meta:
        verbose_name_plural = "Clients"
        ordering = ['-id']

class FabricClient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='Fabric Client', max_length=250, help_text='client name')
    version = models.CharField(default='1.21', max_length=250, help_text='client version, 1.12.2 or 1.16.5')
    filename = models.CharField(default='Client.jar', help_text='mod filename on cdn', max_length=250)
    show_in_loader = models.BooleanField(default=True, help_text='whether the client is shown in loader')
    working = models.BooleanField(default=True, help_text='whether the client is running')
    fabric = models.BooleanField(default=True, help_text='whether the client is a fabric client')
    category = models.CharField(default='HVH', max_length=250, help_text='client category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.version}"
    
    class Meta:
        verbose_name_plural = "Fabric Clients"
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

class AnalyticsCounter(models.Model):
    endpoint = models.CharField(max_length=200, unique=True)
    count = models.IntegerField(default=0)

class CreditsText(models.Model):
    text = models.TextField()
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return f"{self.text[:50]}..."

    class Meta:
        verbose_name_plural = "Credits Text"
        
class HeaderText(models.Model):
    line = models.CharField(max_length=100)
    language = models.CharField(max_length=10, default='en')
    
    def __str__(self):
        return f"{self.line[:50]}..."
    
    class Meta:
        verbose_name_plural = "Header Text"