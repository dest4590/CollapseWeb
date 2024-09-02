from datetime import datetime

from discord_webhook import DiscordEmbed, DiscordWebhook
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

from Core.settings import DISCORD_WEBHOOK_CLIENT, DISCORD_WEBHOOK_START

from .models import AnalyticsCounter, Client, Config


def is_admin(request: WSGIRequest):
    return request.user.is_superuser

def index(request: WSGIRequest):
    return render(request, 'index.html', {
        'clients': Client.objects.all(),
        'configs': Config.objects.all(),
        'is_admin': is_admin(request)
    })

def api(request: WSGIRequest):
    return render(request, 'api.html')

def analytics_start(request: WSGIRequest):
    counter, _ = AnalyticsCounter.objects.get_or_create(endpoint='api/analytics/start')
    counter.count += 1
    counter.save()

    if DISCORD_WEBHOOK_START:
        try:
            if request.GET.get('version', None) is None:
                return JsonResponse({'status': 'error', 'message': 'Version not set'}, status=400)
            
            webhook = DiscordWebhook(url=DISCORD_WEBHOOK_START)
            embed = DiscordEmbed(title="Loader run", description="", color="902bfb")
            embed.add_embed_field(name="Version", value=request.GET.get('version', 'None'))
            embed.add_embed_field(name="Timestamp", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            embed.add_embed_field(name="Start counter", value=str(counter.count))
            
            webhook.add_embed(embed)
            webhook.execute()
            
            return JsonResponse({'status': 'success', 'message': 'Analytics data sent successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Webhook not set'}, status=500)

def analytics_client(request: WSGIRequest):
    counter, _ = AnalyticsCounter.objects.get_or_create(endpoint='api/analytics/client')
    counter.count += 1
    counter.save()
    
    if DISCORD_WEBHOOK_CLIENT:
        try:
            if request.GET.get('username', None) is None:
                return JsonResponse({'status': 'error', 'message': 'Username not set'}, status=400)
            
            if request.GET.get('client_id', None) is None:
                return JsonResponse({'status': 'error', 'message': 'Client ID not set'}, status=400)
        
            webhook = DiscordWebhook(url=DISCORD_WEBHOOK_CLIENT)
            embed = DiscordEmbed(title="Client run", description="", color="2b2bfb")
            embed.add_embed_field(name="Username", value=request.GET.get('username', 'None'))
            embed.add_embed_field(name="Timestamp", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            embed.add_embed_field(name="Client counter", value=str(counter.count))
            
            client_id = request.GET.get('client_id', 0)
            client = Client.objects.filter(id=client_id).first()
            
            if client:
                embed.add_embed_field(name="Client", value=client.name)
            else:
                embed.add_embed_field(name="Client", value="None")
            
            webhook.add_embed(embed)
            webhook.execute()
            
            return JsonResponse({'status': 'success', 'message': 'Analytics data sent successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Webhook not set'}, status=500)
    
def handler404(request: WSGIRequest, exception):
    response = render(request, "418.html")
    response.status_code = 418
    return response