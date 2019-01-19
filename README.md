# 管理画面の設定項目
・ヘッダを変更できる

・タイトルを変更できる

・見出しを変更できる

・タイトルバーの変更ができる

・リスト項目を変更できる

・フィルターをつけられる

・検索ボックスをつけられる

・Slug と タイトルを紐付けられる

・ページネーションをつけれられる

・delete 以外のアクションを追加できる

・アクション実行時のメッセージを変更できる。

・データのヒストリーを出せる( 2019 January 18 January 19)

・フォームの項目の配置を変更できる

・fieldsets で、セクションを分けることができる

・list_displayには、任意の項目を追加できる

・リッチエディタにできる

・blog : comment のようにひもづけた状態で、画面表示できる

```bash
class CommentAdmin(admin.ModelAdmin):

    list_display = ('blog', 'text', 'date_created', 'is_active')
```

・表示項目を直接編集できるようにする

```bash
list_editable = ('text', 'is_active', )
```

・非表示にできる

```bash
'classes': ('collapse', ),
```

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

# Users

## Non staff users
* is_staff=False and is_superuser=False
* Cannot even access or login into the admin

## Staff users
* is_staff=True and is_useruser=False
* Can log in but cannot do anything until they're given permission

## Superusers
* is_staff=True and is_superuser=True
* Have all powers, can do anything even, even deleting themselves!

## Default permissions
* Django comes with a simple permissions system. It provides a way to assign permissions to specific users and groups of users.
* add, change and delete permissions are created for each Django model defined in one of your installed applications.
* Can create custom permissions

# dropdown

[django-admin-list-filter-dropdown](https://github.com/mrts/django-admin-list-filter-dropdown)

# range filter
[django-admin-rangefilter](https://github.com/silentsokolov/django-admin-rangefilter)

# Leaflet
[Leaflet](https://django-leaflet.readthedocs.io/en/latest/)

# geojson
[django-geojson](https://django-geojson.readthedocs.io/en/latest/)

# import-export
[django-import-export](https://django-import-export.readthedocs.io/en/latest/)

# Grappelli
[Django Grappelli](https://django-grappelli.readthedocs.io/en/latest/)

# django-admin-honeypot
[django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot)





