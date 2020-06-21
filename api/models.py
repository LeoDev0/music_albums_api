from django.db import models


class Band(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False)
  counter = models.IntegerField(default=0)

  class Meta:
    ordering = ["name"]
    # verbose_name_plural = "oxen"

  def __str__(self):
      return f'{self.name} ({self.id})'


class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    cover = models.URLField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    class Meta:
      ordering = ["band"]

    def __str__(self):
      return f'{self.title} ({self.id})'
