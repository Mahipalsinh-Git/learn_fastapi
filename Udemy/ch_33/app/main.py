from tables import create_table
from services import (
    create_user,
    create_post,
    get_user_by_id,
    get_posts_by_user_id,
    get_all_posts,
    update_user_email,
    delete_post,
)


def main():
    # Create tables
    create_table()

    # insert user
    # create_user("mahipal", "demo@gmail.com")

    # insert post
    # create_post(1, "AI", "This is the future AI")

    # select user by id
    # result = get_user_by_id(1)
    # print("result: ", result)

    # select user by id
    # results = get_posts_by_user_id(1)
    # for result in results:
    #     print("result: ", result)

    # fetch all posts
    # results = get_all_posts()
    # for result in results:
    #     print("result: ", result)

    # update user email
    # update_user_email(1, "hello@gmail.com")

    # delete post by id
    delete_post(2)


if __name__ == "__main__":
    main()
