import os
from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image
from Core.settings import MEDIA_ROOT
from io import BytesIO

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
    link = models.CharField(default='sigma', help_text='moneyz link', max_length=250)
    image = models.ImageField(upload_to=image_file, default='clients/image/unknown.webp')
    hidden = models.BooleanField(default=False, help_text='whether to hide client in api')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image.file = optimize_image(self.image.file, self.image.path)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.version}'

    class Meta:
        ordering = ['-id']
