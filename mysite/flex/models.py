"""Flexible models for Django."""

from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from streams import blocks

class FlexPage(Page):
    """Flexible Page Class."""

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=True,
        verbose_name="Page Content"
    )

    subtitle = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Add a subtitle"
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
