import oslo_i18n
import webob.dec

from nca._i18n import _
from nca.api.views import versions as versions_view
from nca import wsgi


class Versions(object):

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls(app=None)

    @webob.dec.wsgify(RequestClass=wsgi.Request)
    def __call__(self, req):
        version_obj = [
            {
                "id": "v1.0",
                "status": "CURRENT"
            }
        ]

        if req.path != "/":
            if self.app:
                return req.get_response(self.app)
            language = req.best_match_lauguage()
            msg = _("Unknown Api version Specified")
            msg = oslo_i18n.translate(msg, language)
            return webob.exc.HTTPNotFound(explanation=msg)

        builder = versions_view.get_view_builder(req)
        versions = [builder.build(version) for version in version_obj]
        response = dict(version=versions)
        metadata = {}

        content_type = req.best_match_content_type()
        body = (wsgi.Serializer(metadata=metadata).serialize(response, content_type))

        response = webob.Response()
        response.content_type = content_type
        response.body = wsgi.encode_body(body)

        return response

    def __init__(self):
        self.app = app
