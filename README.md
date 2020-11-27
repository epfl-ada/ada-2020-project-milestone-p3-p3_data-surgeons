
# Title : Online Surveillance and Privacy Seeking

## Abstract :
The goal of the paper was to show the existence of a Chilling Effect using the Wikipedia pageviews of articles from a list of Terrorism related articles. On the other hand, we propose to study the effect on the will of seeking privacy-enhancing technologies (PET), through what we hope would be an increase in the pageviews of articles related to the subject. In order to prove it, we construct a curated list of articles which can correspond to the concept of [PET](https://en.wikipedia.org/wiki/Category:Internet_privacy), and then provide an analysis using segmented regression to examine the effect the PRISM reveal has on the search for more privacy. We will also see if there are other instances in time where we see changes in the trend on pageviews for PET-related articles.

## 1. Research questions:  
- Can we identify a change of trend in pageviews for PET-related articles after the PRISM surveillance reveal? (exogenous + long term).
- Do we observe other time instances of sudden changes in pageviews for PET-related articles? Follow-up: what could be the reason for these sudden changes?
- Is the (increased/decreased/unchanged) interest in privacy-enhancing technologies unique to English wikipedia, or do we observe inconsistencies between language editions?

## 2. Proposed dataset:
As our dataset, we will fetch pageviews for a curated list of articles. The curated list will be produced by an annotation process discussed below.

We will then get the pageviews for these selected articles. The original paper makes use of `stats.grok.se` to this end, but as the service is currently unavailable we will instead make use of the Pageview API developed by the Wikimedia foundation. This API also provides an endpoint to get the pageviews for all of Wikipedia directly, facilitating the comparative analysis of our curated list vs all articles.

## 3. Methods
### Annotating the articles
This list of articles is constructed by starting from [this](https://en.wikipedia.org/wiki/Category:Privacy) seed webpage. The articles under this category will then be appended to the list of articles we will annotate. After this we follow the subcategories for this category and repeat the process from there at a pre-defined depth (for example: Go into Category:Privacy, add links, follow all subcategories, add their links and stop). We then filter the articles: for each article, each member will mark it as relevant or irrelevant, and any article which has any inter-annotator disagreement will be discarded from the analysis.

### Data collection
We then call the Pageviews API with our given article for both the English and French language editions of wikipedia. We use the `/monthly/` endpoint to get an aggregate of the views for each month. We also make use of the `/aggregate/all-projects/` endpoint to get the monthly pageviews for all the articles on both the English and French language editions. We will retrieve the monthly aggregates for 2 years before and after the event to allow any long-term changes to become apparent.

### Explaining other events
We will then examine our data: are there other spikes at other points in time? In order to understand these changes in the trend we will use google news and utilize a filter around the dates in which a given spike was seen. This will allow us to see any major events occurring, and will aid in finding a plausible explanation.

### Main ITS analysis
We would like to follow a similar approach as used in the paper to explore if there is any significant change in pageviews of PET-related articles. We will use interrupted time series (ITS) design to evaluate the will of seeking privacy-enhancing technologies before and after the PRISM reveal event. Then, we use segmented regression to find if there is any change in the trend of pageviews before and after the event. Given our time-span of 2 years pre- and post-event we will be able to gauge some longer term effects than in the assigned paper. We also perform the same analysis for all wikipedia articles to compare the fitted coefficients (and in order to be able to differentiate from global trends).

### Comparing with French wikipedia
We should note that we cannot strengthen our work by comparing Wikipedia users affected by surveillance with control/treatment groups. This is particularly the case because of the nature of the surveillance. However, if we could define a geographical area of the users (for example by assuming that the traffic on the italian version of wikipedia likely comes from italians), we may be able to divide the users from different geographical areas into control and treatment groups. For this reason we will also be analyzing the French wikipedia and compare with the previous analysis. In order to get the equivalent article in a different language we use the Wikidata entry for the given article. These entries contain links to the equivalent article in the various language editions of Wikipedia.

## 4. Proposed Timeline

### Week 1
- Creating our dataset by querying the API 
- Annotating our list of links.
- Getting started on segmented regression analysis for each language edition.
- Start writing report (“Introduction” and “Related Works” sections)
### Week 2
- Finalize segmented regression analysis.
- Analyzing data to see if there are any other spikes in traffic that can be explained.
- Enlarging scope to Wikipedia articles of different languages and make comparison
- continue writing report (“Dataset” section including data collection and dataset description with summary statistics,Analyze report)
### Week 3
- Finalizing data analyze 
- Work on video (script and visuals)
- Writing data story
- Finishing report (completing “Experiments and results” section)



## 5. Organization with the team:
During week 1 everyone will work on annotating the given articles to construct our dataset.

Daniel:
- During week 1 or 2 (depending on how long the annotation process takes), Daniel will create code to query and process the Pageview API into a DataFrame suitable for our analysis. 
- During week 2 Daniel will analyze (and produce a figure of) the overall pageviews of wikipedia in comparison to our subgroup.
- During week 3 Daniel will work a lot on the text of the report itself, while also working on the script for the video. He may also lend his beautiful voice to do the voicover in the video.

Hatef:
- During week 1, Hatef will annotate the articles for the dataset. 
- During week 1 and 2, Hatef works on “introduction” and “related works” of the report.
- During week 2, Hatef will implement segmented regression for the privacy-related dataset before and after PRISM reveal event.
- During week 3, Hatef works on the report and the slides of the video pitch.

Léopaul:
- During week 1, Léopaul will work on generating the list of articles before annotation
- During week 2, Léopaul will work on the segmented regression analysis, try to find relationships with the wikipedia data of other languages, and find other events that may have impacted the pageviews.
- During week 3, Léopaul will work on the report and the video presentation (+ any video editing ?).

## 6. Questions for TAs :
- Is our approach to generate a list of articles methodologically sound?
- Do you suggest any method to enrich the list of privacy-related articles?
- How can we become aware of any other similar events like PRISM reveal that can cause an increase in the pageviews of privacy-related articles?

