import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

##print all topics
for t in topics:
    print(t.id, ' ', t.text)

##specific topic
t = Topic.objects.get(id = 1)

print(t.text)
print(t.date_added)

##access all entries related to a topic

entries = t.entry_set.all()

for e in entries:
    print(e)