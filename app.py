from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author='Robert', title = 'Sample Title', description = 'Sample Descriptions')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())