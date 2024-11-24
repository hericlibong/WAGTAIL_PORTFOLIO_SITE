from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class BlogIndexPage(Page):
    intro = RichTextField(
        blank=True, 
        help_text="Introduction in front of the blog list"
        )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        # add articles to the context
        context = super().get_context(request)
        context["articles"] = BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, help_text="Article summary")
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    body = RichTextField(
        features=["h2", "h3", "h4", "bold", "italic", "link", 'hr', 'code'],
        blank=True, 
        help_text="Article content")
    
    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]

class AboutPage(Page):
    body = RichTextField(blank=True, 
                         help_text="About page content",
                        features=["h2", "h3", "h4", "bold", "italic", "link", 'image']
                         )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

