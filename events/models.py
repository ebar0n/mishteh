import uuid

from django.db import models
from django.utils.translation import ugettext as _


class Event(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    image = models.URLField(verbose_name=_("image"))
    description = models.TextField(verbose_name=_("description"))
    datetime = models.DateTimeField(verbose_name=_("datetime"))
    place_address = models.CharField(max_length=50, verbose_name=_("place address"))
    place_map = models.URLField(verbose_name=_("place map"))
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("event")

    def __str__(self):
        return self.title

    @property
    def invitations(self):
        return self.invitation_set.all()


class Invitation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    detail = models.TextField(verbose_name=_("detail"))
    guests = models.PositiveSmallIntegerField(verbose_name=_("guests"))
    confirmed = models.BooleanField(default=False, verbose_name=_("confirmed"))
    message = models.TextField(verbose_name=_("message"))
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("invitation")

    def __str__(self):
        return str(self.uuid)
