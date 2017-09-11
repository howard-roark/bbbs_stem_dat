from django.contrib import admin
from .models import Post
from .models import Challenge

class PostAdmin(admin.ModelAdmin):
	all_headers = ["title", "updated", "timestamp"]
	list_display = all_headers
	search_fields = ["title", "content"]
	# list_filter = ["updated", "timestamp"] # Breaks BS Admin
	date_hierarchy = "timestamp"
	list_display_links = all_headers
	
	class Meta:
		model = Post

class ChallengeAdmin(admin.ModelAdmin):
	all_headers = ["title", "points_value"]
	list_display = all_headers
	search_fields = ["title", "content", "points_value"]
	list_display_links = all_headers

	class Meta:
		model = Challenge

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Challenge, ChallengeAdmin)