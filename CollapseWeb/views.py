import os
from datetime import datetime
from discord_webhook import DiscordEmbed, DiscordWebhook
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

from .models import ClientLoader, Config

def is_admin(request: WSGIRequest):
    return request.user.is_superuser

def index(request: WSGIRequest):
    return render(request, 'index.html', {
        'clients': ClientLoader.objects.all(),
        'configs': Config.objects.all(),
        'is_admin': is_admin(request)
    })

def api(request: WSGIRequest):
    return render(request, 'api.html')

def analytics_start(request: WSGIRequest):
    discord_webhook = os.getenv('DISCORD_WEBHOOK_START')
    
    if discord_webhook:
        try:
            webhook = DiscordWebhook(url=discord_webhook)
            embed = DiscordEmbed(title="Loader run", description="", color="902bfb")
            embed.add_embed_field(name="Version", value=request.GET.get('version', 'None'))
            embed.add_embed_field(name="Timestamp", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            webhook.add_embed(embed)
            webhook.execute()
            
            return JsonResponse({'status': 'ok', 'message': 'Analytics data sent successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def analytics_client(request: WSGIRequest):
    discord_webhook = os.getenv('DISCORD_WEBHOOK_CLIENT')
    
    if discord_webhook:
        try:
            webhook = DiscordWebhook(url=discord_webhook)
            embed = DiscordEmbed(title="Client run", description="", color="2b2bfb")
            embed.add_embed_field(name="Username", value=request.GET.get('username', 'None'))
            embed.add_embed_field(name="Timestamp", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            client_id = request.GET.get('client_id', 0)
            client = ClientLoader.objects.filter(id=client_id).first()
            
            if client:
                embed.add_embed_field(name="Client", value=client.name)
            else:
                embed.add_embed_field(name="Client", value="None")
            
            webhook.add_embed(embed)
            webhook.execute()
            
            return JsonResponse({'status': 'ok', 'message': 'Analytics data sent successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
def handler404(request: WSGIRequest, exception):
    response = render(request, "418.html")
    response.status_code = 418
    return response