from instabot import Bot

bot = Bot()

# Login to Instagram
bot.login(username='crackjeca', password='Jeca@2025')


# Post a photo
bot.upload_photo('path_to_your_photo.jpg', caption='Your photo caption here')


# Post a video
bot.upload_video('path_to_your_video.mp4', caption='Your video caption here')


# Follow a list of users
bot.follow_users(['username1', 'username2', 'username3'])


# Follow a user
bot.follow('arikmukherjee3')


# Like a post
bot.like('https://www.instagram.com/p/target_post_id/')


# Comment on a post
bot.comment('https://www.instagram.com/p/target_post_id/', 'Your comment here')


# Unfollow a user
bot.unfollow('target_username')


# Send a direct message
bot.send_message('target_username', 'Your message here')


# Logout from Instagram
bot.logout()


# like a post (by hashtag)
bot.like_by_hashtag('#your_hashtag')
bot.like_by_feed(amount=5)
bot.like_hashtag('your_hashtag', amount=5)