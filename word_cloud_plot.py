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

# bought_name[:15]
# ['85% Lean Ground Beef',
#  'Organic Apple Slices',
#  'Apple Honeycrisp Organic',
#  'Mexican Coffee',
#  'Lactose Free Fat Free Milk',
#  'Seedless Red Grapes',
#  'Large Pineapple Chunks',
#  'Vanilla Coffee Concentrate',
#  'Large Alfresco Eggs',
#  'Blood Oranges',
#  'Uncured Genoa Salami',
#  'Mexican Finely Shredded Cheese',
#  'Organic Refried Black Beans',
#  'Organic Jasmine Rice',
#  'Whipped Cream Cheese']
