import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    posts = Passcard.objects.all()
    some_post=posts[0]
    published_posts=Passcard.objects.filter(is_active=True)
    print("Количество активных пропусков:",len(published_posts))
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
