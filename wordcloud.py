import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# URL of the forum page (Replace with the actual URL)
forum_url = "https://helpforum.sky.com/"

# Fetch the webpage content
response = requests.get(forum_url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract comments (Modify the selector based on the forum structure)
comments = [comment.text for comment in soup.find_all(class_="comment-text")]

# Combine all comments into a single string
text = " ".join(comments)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Save the word cloud image
wordcloud_image_path = "static/wordcloud.png"
wordcloud.to_file(wordcloud_image_path)

# Display the word cloud (optional)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
