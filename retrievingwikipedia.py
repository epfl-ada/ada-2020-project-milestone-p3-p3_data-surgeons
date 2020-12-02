import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('cat', metavar='category', type=str,help='Category for which to search articles')
parser.add_argument('depth', metavar='depth', type=int,help='Depth up to which to search articles')
parser.add_argument('cat_depth', metavar='cat_depth', type=int,help='Depth up to which to search subcategories into categories')
parser.add_argument('-o', default='articles.txt', type=str)
args = parser.parse_args()

import requests
from itertools import zip_longest
S = requests.Session()

#Wikipedia queries accept at most 50 titles in a single query, need to be able to group by 50
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return (set(filter(None,x)) for x in zip_longest(*args, fillvalue=fillvalue))

#Creates a string of "|" separated titles for querying articles 
def get_title_string(titles):
  return "|".join((str(x) for x in titles))

#Returns either all sub-categories or all pages linked inside a category
def get_search_from_cat(title, searched):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
    "action": "query",
    "format": "json",
    "list" : "categorymembers",
    "cmtitle": title,
    "cmtype": searched,
    "prop": "links",
    "cmlimit":"max"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    PAGES = DATA["query"]["categorymembers"]
    cats = [v["title"] for v in PAGES]
    return cats
     
#Returns all subcategories linked in a category
def get_subcat_from_cat(title):
    return get_search_from_cat(title, "subcat")
       
#Returns all articles linked in a category
def get_articles_from_cat(title):
    return get_search_from_cat(title,"page")

#Returns all articles linked in an article (or list of articles separated by "|")
def get_articles_from_article(title):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
    "action": "query",
    "format": "json",
    "titles": title,
    "prop": "links",
    "pllimit":"max"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    PAGES = DATA["query"]["pages"]
    cats = [l["title"] for _,v in PAGES.items() if "links" in v for l in v["links"] ]
    return cats

#Returns all articles and subcategories up until a depth, starting from a list of categories
def get_all_from_categories(categories,depth,cat_depth=0):
    articles = set()
    traversed_categories = set()
    traversed_articles = set()
    
    #Get all subcategories up to specific depth
    for d in range(cat_depth):
        for cat in (categories - traversed_categories).copy():
            traversed_categories.update(cat) #Make sure to not visit twice the same category
            categories.update(get_subcat_from_cat(cat))
    print("Got all subcats : {}".format(len(categories)))

    #Get all articles from subcategories
    for cat in categories:
        articles.update(get_articles_from_cat(cat))
    print("Got all articles from subcats : {}".format(len(articles)))

    #Get all articles from articles up to specified depth
    for d in range(depth):
        for article in grouper((articles - traversed_articles).copy(),50):
            titles = get_title_string(article)
            traversed_articles.update(article) #Make sure to not visit twice the same article
            articles.update(get_articles_from_article(titles))
    print("Got all articles : {}".format(len(articles)))
    return articles, categories

articles, cats = get_all_from_categories({args.cat},depth=args.depth,cat_depth=args.cat_depth)
articles = sorted(list(articles))

with open(args.o, 'w') as filehandle:
    for article in articles:
        filehandle.write('{}\n'.format(article))


