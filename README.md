# BeautyNLP

# Dataset description

Dataset contains products descriptions of beauty products from https://jejustore.pl/. 
They were divided into two price categories : below 50 zł (0) and over 50 zł (1). There are 2 536 samples, 1 268 in each category.

Classification depends on description of effects, formula, highlighted ingredients, skin type.
There is no brands names or INCI in descriptions to avoid classifying whole brand or one substance at once.

# Webscraper
Webscrapper scrap information from website with BeautifulSoup and then saves it to .csv file.
