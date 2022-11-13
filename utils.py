import json

def get_posts_all(path='posts.json'):
    posts = []
    if not path:
        return 'Файл json не найден'
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts
'''Uploads all posts from json file'''

def get_posts_by_user(user_name):
    posts_found = []
    posts = get_posts_all()
    for post in posts:
        if post['poster_name'] == user_name:
            posts_found.append(post)
    if len(posts_found) == 0:
        raise ValueError('Пользователь не найден')
    else:
        return posts_found
'''Returns all the post by one user'''

def get_comments_by_post_id(post_id):
    comments_found = []
    comments = get_posts_all(path='comments.json')
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_found.append(comment)
    if len(comments_found) == 0:
        raise ValueError('Пост не найден')
    else:
        return comments_found
'''Returns all the comments which refer to the certain post by post_id'''

def search_for_posts(query):
    posts_found = []
    posts = get_posts_all(path='posts.json')
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_found.append(post)
    return posts_found
'''Returns the posts which have the key word (query)'''

def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
'''Returns the posts with certain primary key number'''


#posts = get_posts_all(path='nothing.json')
#print(posts)

#post_found = get_posts_by_user('leo')
#print(post_found)

#result = get_comments_by_post_id(15)
#print(result)

#result_1 = search_for_posts('аГА')
#print(result_1)

#result_2 = get_post_by_pk(111)
#print(result_2)