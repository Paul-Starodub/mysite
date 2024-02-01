import datetime
from typing import Optional, Union

from django.contrib.sitemaps import Sitemap
from django.db.models import QuerySet

from .models import Post


class PostSitemap(Sitemap):
    changefreq: str = "weekly"
    priority: float = 0.9

    def items(self) -> QuerySet[Post]:
        return Post.published.all()

    def lastmod(self, obj: Post) -> Optional[Union[str, datetime]]:
        return obj.updated
