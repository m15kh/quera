from django.db import models

# TODO write all of your code here...

class Author(models.Model):
    name = models.CharField(max_length=50)

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        new_post = BlogPost(title=self.title, body=self.body, author=self.author, date_created=self.date_created)
        new_post.save()
        comments = Comment.objects.filter(blog_post=self)
        for comment in comments:
            Comment.objects.create(blog_post=new_post, text=comment.text)

        return new_post.id


class Comment(models.Model):
    text = models.CharField(max_length=500)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE) 




