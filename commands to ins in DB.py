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
24. Comment.objects.get(id=1).like()
25. Comment.objects.get(id=1).dislike()
26. Comment.objects.get(id=1).dislike()
27. Post.objects.get(id=1).like()
28. Comment.objects.get(id=2).like()
29. Comment.objects.get(id=2).like()
30. Comment.objects.get(id=2).dislike()
31. Post.objects.get(id=2).like()
32. Post.objects.get(id=3).like()
33. Post.objects.get(id=3).like()
34. Post.objects.get(id=3).dislike()
35. author  = Author.objects.get(id=2)
36. Post.objects.create(author=author, categoryType='NW', title='newstittle', text='newstext')
37. Post.objects.get(id=4).postCategory.add(Category.objects.get(id=4))
38. Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=User.objects.get(id=4), text='anytextcomment')
39. Post.objects.get(id=4).like()
40. Post.objects.get(id=4).like()
41. Post.objects.get(id=4).dislike()
42. Comment.objects.get(id=5).like()
43. Comment.objects.get(id=5).like()
44. Comment.objects.get(id=3).like()
45. Comment.objects.get(id=5).like()
46. Comment.objects.get(id=4).like()
47. a = Author.objects.get(id=1)
48. a.update_rating()
49. a = Author.objects.get(id=2)
50. a.update_rating()
51. Comment.objects.get(id=5).like()
52. Comment.objects.get(id=5).like()
53. a = Author.objects.order_by('-ratingAuthor')[:1]
54. for i in a:
...     i.ratingAuthor
...     i.authorUser.username
55. Post.objects.get(id=4).like()
56. Post.objects.get(id=3).like()
57. Post.objects.get(id=3).like()
58. Post.objects.get(id=4).like()
59. Post.objects.get(id=4).like()
60. bestPost = Post.objects.all().order_by('-rating')[0]
61. print('Автор лучшей статьи: ', bestPost.author.authorUser.username)
62. s = Post.objects.all().order_by('-rating')[:1]
63. for i in s:
        i.dateCreation
        i.rating
        i.title
        i.preview()
64. c = Comment.objects.all()
65. for i in c:
        i.dateCreation
        i.commentUser
        i.rating
        i.text





