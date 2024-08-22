import os

from discord_webhook import DiscordEmbed, DiscordWebhook
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

from .models import ClientLoader, Config


def index(request: WSGIRequest):
    return render(request, 'index.html', {
        'clients': ClientLoader.objects.all(),
        'configs': Config.objects.all()
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