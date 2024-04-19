from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(default='Client', max_length=250, help_text='client name')

    version = models.CharField(default='1.16.5', max_length=250, help_text='client version, 1.12.2 or 1.16.5')

    filename = models.CharField(default='Client.jar', help_text='client file name on <a href="https://console.cloud.google.com/storage/browser/collapseloader" target="_blank">google cloud</a>', max_length=250)
    
    main_class = models.CharField(default='net.minecraft.client.main.Main', max_length=250)

    internal = models.BooleanField(default=False, help_text='whether to use folders within the client')

    hidden = models.BooleanField(default=False, help_text='whether to hide client in api')

    def __str__(self):
        return f'{self.name} - {self.version}'

    class Meta:
        ordering = ['-id']

# {'name': 'Rockstar', 'link': 'https://storage.googleapis.com/collapseloader/Rockstar.zip', 'filename': 'Rockstar.zip', 'path': 'data/Rockstar.zip', 'path_dir': 'data/Rockstar/', 'jar': 'Rockstar.jar', 'main_class': 'net.minecraft.client.main.Main', 'version': '1.12.2', 'internal': True, 'silent': True}