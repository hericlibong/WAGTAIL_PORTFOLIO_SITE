# from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from my_portfolio.models import BlogPage

class HomePage(Page):
    introduction = RichTextField(
        blank=True,
        help_text='Text to describe the home page',
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['recent_articles'] = BlogPage.objects.live().order_by('-first_published_at')[:5]
        return context