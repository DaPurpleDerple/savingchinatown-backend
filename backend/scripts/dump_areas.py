import django
import sys
import os
import json
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
sys.path.append(os.path.dirname(__file__) + '/..')
django.setup()
from places.models import Area
import pandas as pd
fl = sys.argv[1]

template = """

const Areas = 
%s;
export default Areas;
"""

with open(fl, 'w') as out:
    all_output = {}
    for area in Area.objects.all():
        all_output[area.key] = area.display_name
    out.write(template % json.dumps(all_output))
