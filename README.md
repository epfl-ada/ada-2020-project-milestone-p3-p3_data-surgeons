# Title : Privacy Seeking after the Chilling Effect!

## Abstract :
The goal of the paper was to show the existence of a Chilling Effect using the Wikipedia pageviews of articles from a list of Terrorism related articles. On the other hand, we propose to study the effect on the will of seeking privacy-enhancing technologies, through what we hope would be an increase in the pageviews of privacy related articles. In order to prove it, we construct a curated list of articles which can correspond to the concept of [privacy](https://en.wikipedia.org/wiki/Category:Internet_privacy), and then provide an analysis using segmented regression (+ other methods we see fit) to examine the effect the PRISM reveal has on the search for privacy. We may also want to identify other instances in time where we see changes in the trend on pageviews for privacy-related articles.

## 1. Research questions:  
- Can we identify a change of trend in pageviews for privacy-related articles after the PRISM surveillance reveal ? (exogenous + long term).
- Do we observe other time instances of sudden changes in pageviews for privacy related articles ?
- Compare the effect of different events + enlarge the search to more countries (e.g., French Wikipedia, etc.)
- Does PRISM reveal affect the distribution of geographical origins of article views?

## 2. Proposed dataset:
As our dataset, we will fetch pageviews for curated list of articles. To this end, we consider the following list of Wikipedia privacy-related articles:
- https://en.wikipedia.org/wiki/Virtual_private_network
- https://en.wikipedia.org/wiki/Privacy
- https://en.wikipedia.org/wiki/Digital_identity
- https://en.wikipedia.org/wiki/Digital_footprint
- https://en.wikipedia.org/wiki/Privacy_laws_of_the_United_States
- https://en.wikipedia.org/wiki/Privacy_policy
- https://en.wikipedia.org/wiki/Data_Protection_Commissioner
- https://en.wikipedia.org/wiki/Personality_rights
- https://en.wikipedia.org/wiki/Information_privacy
- https://en.wikipedia.org/wiki/Right_to_privacy
- https://en.wikipedia.org/wiki/Intelligence_agency
- https://en.wikipedia.org/wiki/Personal_data
- https://en.wikipedia.org/wiki/Freedom_of_speech
- https://en.wikipedia.org/wiki/Privacy-enhancing_technologies
- https://en.wikipedia.org/wiki/Privacy_engineering
- https://en.wikipedia.org/wiki/Anonymity
- https://en.wikipedia.org/wiki/Data_security
- https://en.wikipedia.org/wiki/Eavesdropping
- https://en.wikipedia.org/wiki/Global_surveillance
- https://en.wikipedia.org/wiki/Mass_surveillance
- https://en.wikipedia.org/wiki/Private_browsing
- https://en.wikipedia.org/wiki/Incognito
https://en.wikipedia.org/wiki/Anonymous_web_browsing
- https://en.wikipedia.org/wiki/Internet_privacy
- https://en.wikipedia.org/wiki/Digital_privacy
- https://en.wikipedia.org/wiki/Computer_and_network_surveillance
- https://en.wikipedia.org/wiki/Internet_censorship_and_surveillance_by_country
- https://en.wikipedia.org/wiki/Global_surveillance
- https://en.wikipedia.org/wiki/Privacy_laws_of_the_United_States
- https://en.wikipedia.org/wiki/PRISM_(surveillance_program)




## 3. Methods
We would like to follow a similar approach as used in the paper to explore if there is any significant change in pageviews of privacy-related articles. We will use interrupted time series (ITS) design to evaluate the will of seeking privacy-enhancing technologies before and after PRISM reveal event. Then, we use segmented regression to find if there is any change in the trend of pageviews before and after the event.  In addition, we would explore long term effect of the PRISM reveal event.

We should note that we cannot strengthen our work by comparing Wikipedia users affected by surveillance with control/treatment groups. This is particularly because of the  nature of the surveillance. However, if we could find geographical area of the users we may be able to divide the users from different geographical areas to control and treatment groups.

## 4. Proposed Timeline
- Fetching the data (2 person hours)
- Segmented regression for the privacy-related dataset before and after PRISM reveal event (3 person hours)
- Identifying more changes in pageviews (3 person hours)
- Enlarging scope to Wikipedia articles of different languages and make comparison (7 person hours)
- Evaluating the effect of PRISM reveal on the distribution of geographical origins of article views (5 person hours)
- Comparing effects of other events (6 person hours)
- Prepare an extension data story (4 person hours)

## 5. Organization with the team:

## 6. Questions for TAs :
- Do you suggest any method to enrich the list of privacy-related articles?
- How can we become aware of any other similar events like PRISM reveal that can cause an increase in the pageviews of privacy-related articles?
- How can we find the geographical area distribution for pageviews of an article in Wikipedia?
