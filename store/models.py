# store/models.py
from django.db import models

class Software(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='software_images/')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	features = models.TextField(default='')  # Thêm default
	requirements = models.TextField(default='')  # Thêm default
	screenshots = models.JSONField(default=list)
	download_link = models.URLField(blank=True, default='')  # Thêm default
	demo_link = models.URLField(blank=True, default='')  # Thêm default
	created_at = models.DateTimeField(auto_now_add=True)
	
	def get_features_list(self):
		return self.features.split('\n') if self.features else []
	
	def __str__(self):
		return self.name