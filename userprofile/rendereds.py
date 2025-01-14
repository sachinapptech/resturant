import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRendered(JSONRenderer):
    charset = "utf-8"

    def render(self,data,accepted_media_types=None,renderer_context=None):
        errors = data.get("errors",None)

        if errors is not None:
            return super(ProfileJSONRendered,self).render(data)
        
        return json.dumps({"profile":data})