import matplotlib.pyplot as plt

def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))

    # Display image
    plt.imshow(wordcloud) 
    
    # No axis details
    plt.axis("off");
    
from wordcloud import WordCloud, STOPWORDS

# generate wordcloud
text = str(bought_name)
wordcloud = WordCloud(width=3000, height=2000, random_state=42, background_color='black', colormap='Set2', 
                      collocations=False, stopwords=STOPWORDS).generate(text)
# plot
plot_cloud(wordcloud)
