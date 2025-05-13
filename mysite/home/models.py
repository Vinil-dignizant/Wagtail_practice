from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

class HomePage(Page):
    """A model representing the home page of the site."""

    template = "home/home_page.html"
    max_count = 1  # Limit to one instance of this page type

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic", "link"], blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        FieldPanel("banner_cta")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"



