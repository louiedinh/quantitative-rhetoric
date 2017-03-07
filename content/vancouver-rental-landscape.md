Title:Vancouver Rental Landscape
Date: 2017-01-28  
Category: Vancouver Real Estate


I was born and raised in Vancouver and for as long as I can remember my mom has been nagging me to buy real estate. This is normal in Asian families. As a kid, I obviously couldn't afford it. Over time my earnings have grown along with my age but the sky rocketing prices leave real estate perpetually out of reach.

To a housing hopeful, the news coverage is an emotional roller coaster. One day sales collapse and hope is restored, only to be followed by a surge that leaves prices at dizzying new heights. 

The lack of hard data was frustrating so I decided to do a little digging on my own.

This particular post explores the rental market in Vancouver. Sales numbers are exciting, but hard to compile and strongly affected by speculation. Rental prices are more stable and act as a proxy for demand of living space. We will be exploring where rentals are located within the city, and how much it will cost to rent in each neighbhourhood.

My data source is a popular online rental marketplace. The data was retrieved between November 6th, 2016 and December 9th, 2016. After cleaning and removal of duplicates, the dataset contains 5138 listings in the city of Vancouver. 

To aid this investigation, I arbitrarily split Vancouver into neighbhourhoods. The grid lines are eyeballed to approximate the neighbourhood boundaries and labeled with names off the top of my head. Please don't take them literally. I know they are wrong.

Here is my arbitrarily labelled map of Vancouver.

![](/static/vancouver-rental-landscape_files/figure-html/setup-1.png)<!-- -->





First, where are all these rentals located? A quick plot shows us that rentals are not evenly spread across the city. Here each dot is a rental posting. There is a large concentration in Downtown and along the Broadway corridor between Arbutus and Nanaimo. The rest of Vancouver is sparse in terms of vacancies. 

![](/static/vancouver-rental-landscape_files/figure-html/density-plot-1.png)<!-- -->

Breaking this down further, we can see that Downtown 47%, Mt-Pleasant-W (9%) and Mt-Pleasant-E (5%) account for more than half of the rental stock. 

![](/static/vancouver-rental-landscape_files/figure-html/rental-dist-1.png)<!-- -->

Although rentals in Downtown and along Broadway are abundant, they might not be ideal for families. Diving into the bedroom and square footage distributions, we notice that neighbourhoods can have very distinct rental stock profiles. Some neighbourhoods have many more 1 Bedroom units (BRs), than others.

![](/static/vancouver-rental-landscape_files/figure-html/bedroom-dist-1.png)<!-- -->

High rental density areas probably correspond to higher density buildings like apartments. Notice that Downtown and Mt-Pleasant-E have very distinct staircase patterns in the bedroom distribution. Many one bedrooms, then less two bedrooms, etc. In older neighbourhoods, where we expect more single family dwellings, the pattern is different. We see many more dwellings with 2 or more BRs (e.g Renfrew, Sunset and Cambie). Also, there are some nice intermediate neighbourhoods where we see the two patterns mixing.

It's hard to prove this is the case using our current dataset, but can probably be verified in the future.

The size distribution is not that exciting. As previously identified, the neighbourhoods show two distinct patterns, with some mixing. The size distribution follows a similar trend to our bedrooms. 
![](/static/vancouver-rental-landscape_files/figure-html/size-dist-1.png)<!-- -->![](/static/vancouver-rental-landscape_files/figure-html/size-dist-2.png)<!-- -->

Finally, we look at the price distribution. Let's be honest, rent in Vancouver are not cheap. The most distinct pattern is the East/West divide. The median west side home is priced over $2000 for every neighbhourhood except Marpole. Conversely, none are over $2000 on the east side.

A common rule of thumb is that you can comfortably spend at most 33% of your income on housing costs. This works out to $72,000 take-home pay or $95,000 in gross salary. Of course, this is for median household, not just a single person. A newly graduated student living with a roommate would target a much different rental market than a 4 person family. 

![](/static/vancouver-rental-landscape_files/figure-html/price-dist-1.png)<!-- -->![](/static/vancouver-rental-landscape_files/figure-html/price-dist-2.png)<!-- -->

Even this high level view of the hard data allows us to draw some conclusions.

1. A large fraction of rentals (0.62) available in Vancouver are in Downtown and on the Broadway corridor between Nanaimo and Arbutus.
2. Two main neighbourhood patterns emerge: high density, small units with fewer bedrooms. Or low density, lots of bedrooms, and space. A few neighbourhoods are a mixture of these two patterns.
3. Rent on the east side is much cheaper than the west side.

In the next post, we will explore the factors that lead to higher prices and what you can expect to rent for in each neigbhourhood.

Thanks to Charles, Mya, Maude, Ganesh, Simon and Gilbert for early comments and feedback.
