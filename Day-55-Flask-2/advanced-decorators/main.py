class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False


def is_authenticated(my_func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            my_func(args[0])
    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"{user.name}'s new blog post is getting created.")


new_user = User("Angela")
new_user.is_logged_in = True

create_blog_post(new_user)
