# ユーザーデータ登録

ユーザーデータを一気に登録する。

```bash
pip install Faker

python manage.py shell
>>> from main.models import Blog
>>> from faker import Faker
>>> faker = Faker()
'Kyle Parks'
>>> faker.first_name()
'Jennifer'

>>> for _ in range(0, 500):
         Blog.objects.create(title=faker.sentence(), body=faker.paragraph())

<Blog: Attack indeed race make.>
<Blog: Accept work myself capital occur others they.>
<Blog: Almost within major establish.>
<Blog: Fly enter together reflect.>


for blog in Blog.objects.iterator():
...     comments = [Comment(text=faker.paragraph()) for _ in range(0, 3)]
...     comments = [Comment(text=faker.paragraph(), blog=blog) for _ in range(0, 3)]
...     Comment.objects.bulk_create(comments)
 Comment.objects.count()
1510


```

# rich editor

[django-summoernote](https://github.com/summernote/django-summernote)

# Model relations
One to one(Blog and BlogSettings)

One to many(Blog and Comments)

Many to Many(Blogs and Tags)
