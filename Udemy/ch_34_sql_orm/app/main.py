from models import create_tables
from services import *


def main():
    # create_tables()

    # Create user
    # result = create_user("mahipal", "t.mahi009@gmail.com")
    # result = create_user("usha", "usha@gmail.com")
    # print("result: ", result)

    # Create post
    # result = create_post(1, "GenAI", "Artificial intelligence")
    # result = create_post(2, "First post", "First post data")
    # result = create_post(2, "Second post", "Second post data")
    # print("result: ", result)

    # Get user by id
    # result = get_user_by_id(1)
    # print("result: ", result)

    # Get all users
    # result = get_all_users()
    # print("result: ", result)

    # Get post by id
    # result = get_post_by_id(1)
    # print("result: ", result)

    # Get all posts by user id
    # result = get_posts_by_user(2)
    # print("result: ", result)

    # Update user email
    # result = update_user_email(1, "hello@gmail.com")
    # print("result: ", result)

    # Delete post
    # result = delete_post(3)
    # print("result: ", result)

    # Order by
    result = get_users_ordered_by_name()
    print("result: ", result)


if __name__ == "__main__":
    main()

# Run this file
# python3 main.py
