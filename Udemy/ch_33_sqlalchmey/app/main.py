from tables import create_table
from services import *


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
    # delete_post(2)

    # Print get users orderby name
    # print(get_users_ordered_by_name())

    # Print get all posts
    # print(get_post_latest_first())

    # Group by
    # print(get_post_count_per_user())

    # Join
    # print(get_posts_with_author())

    # Raw query
    #     raw_sql_insert_full_query(
    #         """
    #         INSERT INTO users(name, email)
    #                    VALUES("tech", "tech@gmail.com")
    # """
    #     )

    # raw_sql_insert_values("test user", "test_user@gmail.com")

    print(raw_sql_select("test_user@gmail.com"))


if __name__ == "__main__":
    main()
