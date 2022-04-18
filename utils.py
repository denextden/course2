import json

POST_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


def get_posts_all():
    """возвращает посты"""
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    users_posts = []
    for user in get_posts_all():
        if user['poster_name'].lower() == user_name.lower():
            users_posts.append({
                "poster_name": user['poster_name'],
                "poster_avatar": user['poster_avatar'],
                "pic": user['pic'],
                "content": user['content'],
                "views_count": user['views_count'],
                "likes_count": user['likes_count'],
                "pk": user['pk']
            }
            )
    return users_posts


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    with open(COMMENT_PATH, 'r', encoding='utf-8') as file:
        comments = json.load(file)
        comments_by_post = []
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_by_post.append(
                    {
                        'commenter_name': comment['commenter_name'],
                        'comment': comment['comment'],
                        "post_id": comment['post_id']
                    }
                )
        
        return comments_by_post



def search_for_posts(query):
    """возвращает список постов по ключевому слову"""

    posts_by_word = []
    for word in get_posts_all():
        if query.lower() in word['content'].lower():
            posts_by_word.append(
                {
                    "poster_name": word['poster_name'],
                    "poster_avatar": word['poster_avatar'],
                    "pic": word['pic'],
                    "content": word['content'],
                    "views_count": word['views_count'],
                    "likes_count": word['likes_count'],
                    "pk": word['pk']
                }
            )
    return posts_by_word


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    for post in get_posts_all():
        if pk == post['pk']:
            return {
                "poster_name": post['poster_name'],
                "poster_avatar": post['poster_avatar'],
                "pic": post['pic'],
                "content": post['content'],
                "views_count": post['views_count'],
                "likes_count": post['likes_count'],
                "pk": post['pk']
            }
