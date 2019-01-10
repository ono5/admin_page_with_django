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

```

