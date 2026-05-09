# Человек
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name