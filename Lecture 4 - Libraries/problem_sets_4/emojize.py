########## EMOJIZE ##########
# Imports
import emoji

#
user_input = emoji.emojize(input("Input: "), language="alias")
if emoji.emoji_count(user_input) >= 1:
    print(f"Output: {user_input}")

# else statement to check if input without emojis will fail, not actually needed, just for my own giggles
# else:
#     print(emoji.emojize("No emojis in input :disappointed_face:"))
