from django.core.management.utils import get_random_secret_key

with open('.env', 'a+', encoding='utf-8') as env:
    if 'SECRET_KEY' in env.read():
        pass
    else:
        env.write(f'SECRET_KEY={get_random_secret_key()}')
