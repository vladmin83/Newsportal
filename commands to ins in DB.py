список всех команд, запускаемых в Django shell

1. User.objects.create_user('Vlad')
2. u1 = User.objects.create_user('Sergey')
3. Author.objects.create(authorUser=u1)
4. u2 = User.objects.create_user('Alex')
5. Author.objects.create(authorUser=u2)
6. User.objects.create_user('Tom')
7. Category.objects.create(name='IT')
8. Category.objects.create(name='Politics')
9. Category.objects.create(name='Sport')
10. Category.objects.create(name='Millitary')
12. author  = Author.objects.get(id=1)
13. Post.objectrs.create(author=author, categoryType='NW', title='sometitle', text='sometext')
14. Post.objects.create(author=author, categoryType='AR', title='newtitle', text='somebigtext')
15. Post.objects.create(author=author, categoryType='AR', title='bigtitle', text='somebigtext2')
16. Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
17. Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
18. Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
19. Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
20. Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
21. Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor2')
22. Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor3')
23. Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=User.objects.get(id=1), text='anytextbyauthor4')
