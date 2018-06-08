import os


def get_view_builder(req):
    base_url = req.application_url
    return ViewBuilder(base_url)


class ViewBuilder(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def build(self, version_data):
        version = {
            "id": version_data["id"],
            "status": version_data["status"],
            "links": self._build_links(version_data),
        }
        return version

    def _build_links(self, version_data):
        """Generate a container of links that refer to the provided version."""
        href = self.generate_href(version_data["id"])

        links = [
            {
                "rel": "self",
                "href": href,
            },
        ]

        return links

    def generate_href(self, version_number):
        """Create an url that refers to a specific version_number."""
        return os.path.join(self.base_url, version_number, '')
