from project.social_media import  SocialMedia
from unittest import TestCase, main

class TestSocialMedia(TestCase):
    def setUp(self):
        self.media = SocialMedia("Test Username", "Twitter", 1200, "Gaming")
        self.media2 = SocialMedia("Test Username", "Twitter", 1200, "Gaming")
        self.allowed_platforms = ['Instagram', 'YouTube', 'Twitter']

        for post_content in [f"Post Content {n}" for n in range(1, 11)]:
            self.media.create_post(post_content)

        for post_idx in range(len(self.media._posts)):
            for _ in range(post_idx):
                self.media.like_post(post_idx)

            for _ in range(len(self.media._posts) - post_idx):
                self.media.comment_on_post(post_idx, f"A good comment {_+1}")


    def test_initialisations(self):
        # Test values
        self.assertEqual("Test Username", self.media._username)
        self.assertEqual("Twitter", self.media._platform)
        self.assertEqual(1200, self.media._followers)
        self.assertEqual("Gaming", self.media._content_type)
        self.assertEqual([], self.media2._posts)
        # Test types
        self.assertIsInstance(self.media._username, str)
        self.assertIsInstance(self.media._platform, str)
        self.assertIsInstance(self.media._followers, int)
        self.assertIsInstance(self.media._content_type, str)
        self.assertIsInstance(self.media._posts, list)

    def test_properties(self):
        self.assertEqual(self.media._platform, self.media.platform)
        self.assertEqual(self.media._followers, self.media.followers)

    def test_platform_setter_correct_platform(self):
        for platform in self.allowed_platforms:
            self.media.platform = platform
            self.assertEqual(platform, self.media._platform)

    def test_platform_setter_incorrect_platform(self):
        with self.assertRaises(ValueError) as ctx:
            self.media.platform = "Kik"
        self.assertEqual(f"Platform should be one of {self.allowed_platforms}", str(ctx.exception))

    def test_existence_of_validate_and_set_platform(self):
        has_attr = hasattr(self.media, "_validate_and_set_platform")
        self.assertTrue(has_attr)
        if has_attr:
            self.assertTrue(callable(self.media._validate_and_set_platform))

    def test_followers_negative_followers(self):
        with self.assertRaises(ValueError) as ctx:
            self.media.followers = -1
        self.assertEqual(f"Followers cannot be negative.", str(ctx.exception))

    def test_create_post_(self):
        for post_content in [f"Post Content {n}" for n in range(10, 16)]:
            self.assertEqual(f"New {self.media._content_type} post created by {self.media._username} on {self.media._platform}.", self.media.create_post(post_content))
            self.assertIn({'content': post_content, 'likes': 0, 'comments': []}, self.media._posts)

    def test_like_post_valid(self):
        for post_idx in range(len(self.media._posts)):
            expected = f"Post liked by {self.media._username}."
            likes = self.media._posts[post_idx].get('likes', 0)
            result = self.media.like_post(post_idx)
            self.assertEqual(result, expected)
            self.assertEqual(likes + 1, self.media._posts[post_idx].get('likes', 0))

    def test_like_post_reached_max(self):
        for post_idx in range(len(self.media._posts)):
            expected = "Post has reached the maximum number of likes."
            likes = 10
            for _ in range(11):
                self.media.like_post(post_idx)
            result = self.media.like_post(post_idx)
            self.assertEqual(result, expected)
            self.assertEqual(likes, self.media._posts[post_idx].get('likes', 0))

    def test_like_post_invalid_idx(self):
        post_idxes = [-2, len(self.media._posts), len(self.media._posts)+10]

        for post_idx in post_idxes:
            self.assertEqual("Invalid post index.", self.media.like_post(post_idx))

    def test_comment_on_post_valid(self):
        media = SocialMedia("Test Username", "Twitter", 1200, "Gaming")
        media.create_post("Post Content #78")
        for comment in [f"A valid comment {n}" for n in range(1, 11)]:
            result = media.comment_on_post(0, comment)
            self.assertEqual(f"Comment added by {media._username} on the post.", result)
            self.assertIn({'user': media._username, 'comment': comment}, media._posts[0].get('comments', []))

    def test_comment_on_post_short(self):
        for comment in [f"Comment {n}" for n in range(1, 11)]:
            result = self.media.comment_on_post(0, comment)
            self.assertEqual("Comment should be more than 10 characters.", result)
            self.assertNotIn({'user': self.media._username, 'comment': comment}, self.media._posts[0].get('comments', []))





if __name__ == "__main__":
    main()