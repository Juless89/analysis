#### Repository
e.g. https://github.com/utopian-io/utopian.io

#### Introduction
Utopian is a key platform in the STEEM ecosystem. Rewarding contributions to open source projects by utilising a decentralised vote-based reward system on top of the STEEM Blockchain. The STEEM blockchain is decentralised and open to everyone, this means that every action performed by Utopian on the STEEM Blockchain can be seen by anyone. Analysing these actions allows for a better understanding in how successful Utopian has been in achieving its goals and what the reach of Utopian has been since its inception. Contributors and moderators are rewarded with upvotes on the STEEM Blockchain, this analysis will look deeper into all upvotes that have been performed by Utopian.

#### Outline
- Scope of the analysis and tools
- Votes over time and average weight
- Total unique users and growth
- Distribution of votes and weight per user
- Weights and votes per category
- Conclusion

#### Scope of the analysis and tools
This analyse is based on all the upvotes made by the utopian-io account between 2017-09-28 15:39:51 and 2018-07-16 14:99:09. A total of 38075 upvotes were retrieved from the STEEM Blockchain. Votes on the STEEM Blockchain have the following structure:

```
{
  "vote":{
    "voter" : "utopian-io",
    "author" : "elear",
    "permlink" : "utopian-my-contribution-to-the-open-source-world",
    "weight" : 10000
  }
}
```

Each vote was stored into a MySQL database with its timestamp. It is important that the weight does not give any information about the value of the actual vote. A 100% vote has a weight of 10000, not regarding the amount of STEEM POWER behind the vote. Also, this analysis only looks at the actual votes performed by Utopian-io, therefor excluding any rejected submissions. The data gathered and used for this analysis as well as the tools used to extract and analyse the data can be found here.


#### Votes over time and average weight

<center>![Screenshot 2018-07-19 16.18.41.png](https://cdn.steemitimages.com/DQmW3vEj9rtDpEbB3vWZ68XRJzvv6jXAC6py5tsdprUa8Rm/Screenshot%202018-07-19%2016.18.41.png)</center>
After an intial phase with a low amount of votes but a high weight there is a second phase with a high amount votes and lower average weight per vote. Around this time the Utopian-io account has been getting considerable amount of STEEM POWER delegations. It seems that both the amount of votes and average weight per vote have stabilised around the end of March indicating a solid voting strategy had been formed.

##### Total unique users and growth

<center>
![Screenshot 2018-07-19 01.16.27.png](https://cdn.steemitimages.com/DQmTv3ZyfjuiUY2EC6gjqnpQpt1UT1pSCArekJnaG7dNWWj/Screenshot%202018-07-19%2001.16.27.png)</center>
This chart displays the amount of unique users that have received a vote from the Utopian-io account. Growth appeared to be stable from the start and started to slow down around March. This coincides with the overall downturn in the crypto market and the STEEM price. A new period of growth started on 2018-05-29 after Utopian released a [statement](https://steemit.com/utopian-io/@utopian-io/utopian-io-is-giving-you-more-innovation-trail-and-higher-maximum-rewards) increasing rewards for contributions and trailing @steemstem and @steemmakers.

![Screenshot 2018-07-19 16.34.34.png](https://cdn.steemitimages.com/DQmP1hx2nxGkgBA2njPUKeDm3qXc5yTH22KoXNA628WkjQL/Screenshot%202018-07-19%2016.34.34.png)
[source](https://coinmarketcap.com/currencies/steem/)


##### Distribution of votes and weight per user

For the following analyses votes over a period of 90 days have been analysed. To avoid outliers at the early stages of deployment and generating an up to date view of current voting.

<center>![Screenshot 2018-07-19 15.09.19.png](https://cdn.steemitimages.com/DQmWDFobSnSc3BDQ7bTrGsgYDjJR5kemG7o2XbLxBrTLuqP/Screenshot%202018-07-19%2015.09.19.png)</center>

<table>
<tr><td><b>Tag</b></td><td><b>Total weight</b></td><td><b>%</b></td></tr>
<tr><td>utopian-io</td><td>75380</td><td>1.36%</td></tr>
<tr><td>tensor</td><td>74801</td><td>1.35%</td></tr>
<tr><td>amosbastian</td><td>71031</td><td>1.28%</td></tr>
<tr><td>espoem</td><td>66418</td><td>1.20%</td></tr>
<tr><td>baranpirincal</td><td>59565</td><td>1.07%</td></tr>
<tr><td>tobaloidee</td><td>59317</td><td>1.07%</td></tr>
<tr><td>buckydurddle</td><td>59035</td><td>1.06%</td></tr>
<tr><td>cha0s0000</td><td>58186</td><td>1.05%</td></tr>
<tr><td>mcfarhat</td><td>50556</td><td>0.91%</td></tr>
<tr><td>mkt</td><td>48502</td><td>0.87%</td></tr>
<tr><td>realinfo</td><td>45058</td><td>0.81%</td></tr>
<tr><td>kit.andres</td><td>44436</td><td>0.80%</td></tr>
<tr><td>rosatravels</td><td>43899</td><td>0.79%</td></tr>
<tr><td>tobias-g</td><td>42120</td><td>0.76%</td></tr>
<tr><td>andrejcibik</td><td>41823</td><td>0.75%</td></tr>
<tr><td>steemstem</td><td>41500</td><td>0.75%</td></tr>
<tr><td>zularizal</td><td>41304</td><td>0.74%</td></tr>
<tr><td>fego</td><td>39307</td><td>0.71%</td></tr>
<tr><td>knowledges</td><td>38778</td><td>0.70%</td></tr>
<tr><td>crokkon</td><td>38671</td><td>0.70%</td></tr>
<tr><td>Rest</td><td>5295</td><td>81.3%</td></tr>
</table>

Shows in the diagram and table above are the top 20 users with regard to the weight of the votes they are receiving. Excluding utopian-io the top user received 1.35% of all the weight. While all the other users received 81.3% of the upvote weight.

<center>![Screenshot 2018-07-19 15.09.38.png](https://cdn.steemitimages.com/DQmRJRudBtiw5n7xYHLyUFU14zLjLBsyCfci2yWibCZ5XzR/Screenshot%202018-07-19%2015.09.38.png)</center>

<table>
<tr><td><b>Tag</b></td><td><b>Total votes</b></td><td><b>%</b></td></tr>
<tr><td>utopian-io</td><td>183</td><td>2.92%</td></tr>
<tr><td>kr-nahid</td><td>60</td><td>0.96%</td></tr>
<tr><td>tobias-g</td><td>58</td><td>0.92%</td></tr>
<tr><td>neupanedipen</td><td>57</td><td>0.91%</td></tr>
<tr><td>kodeblacc</td><td>54</td><td>0.86%</td></tr>
<tr><td>rosatravels</td><td>48</td><td>0.76%</td></tr>
<tr><td>virus95</td><td>47</td><td>0.75%</td></tr>
<tr><td>ammarraisafti</td><td>46</td><td>0.73%</td></tr>
<tr><td>organik</td><td>44</td><td>0.70%</td></tr>
<tr><td>to-the-sun</td><td>42</td><td>0.67%</td></tr>
<tr><td>tensor</td><td>40</td><td>0.64%</td></tr>
<tr><td>shaphir</td><td>36</td><td>0.57%</td></tr>
<tr><td>crokkon</td><td>35</td><td>0.56%</td></tr>
<tr><td>baranpirincal</td><td>35</td><td>0.56%</td></tr>
<tr><td>sourovafrin</td><td>35</td><td>0.56%</td></tr>
<tr><td>justyy</td><td>33</td><td>0.53%</td></tr>
<tr><td>gregory.latinier</td><td>33</td><td>0.53%</td></tr>
<tr><td>tobaloidee</td><td>32</td><td>0.51%</td></tr>
<tr><td>fego</td><td>31</td><td>0.49%</td></tr>
<tr><td>kit.andres</td><td>31</td><td>0.49%</td></tr>
<tr><td>Rest</td><td>5295</td><td>84.38%</td></tr>
</table>

The amount of vote each users has received appears to be more spread out, with the top user, excluding utopian-io, receiving 0.96%. All the users outside op the top 20 received 84.38% of the votes. Also only 7 users appear in both top 20s.

<center>![Screenshot 2018-07-19 15.07.34.png](https://cdn.steemitimages.com/DQmUQH4fvY9bkc4iE3hyLbyUko8wP5LBHdfTSTcfvUQSfLm/Screenshot%202018-07-19%2015.07.34.png)</center>

The [pareto](https://en.wikipedia.org/wiki/Pareto_principle) principle, which states that "roughly 80% of the effects come from 20% of the causes"  appears to hold for the distribution of voting weight among the users. Which is normal and an indicator for a healthy system.


##### Weights and votes per category
There are 12 different categories for which contributions can be made. For each vote, if possible, the tags were extracted and referenced against these 12 categories. Categories with a higher relative weight vs votes appear to be the most rewarding. In order bug-hunting, development and graphics were the most popular and also paid out the most in total terms.

<center>![Screenshot 2018-07-19 14.59.30.png](https://cdn.steemitimages.com/DQmS2AUnXDX4dE9hLMyni9PUBSyY5c8VQtCMXYQEoNXWSM8/Screenshot%202018-07-19%2014.59.30.png)</center>

<table>
<tr><td><b>Tag</b></td><td><b>Average weight</b></td></tr>
<tr><td>development</td><td>2034</td></tr>
<tr><td>analysis</td><td>1905</td></tr>
<tr><td>translations</td><td>1848</td></tr>
<tr><td>video-tutorials</td><td>1652</td></tr>
<tr><td>graphics</td><td>1571</td></tr>
<tr><td>documentation</td><td>1202</td></tr>
<tr><td>tutorials</td><td>1164</td></tr>
<tr><td>blog</td><td>939</td></tr>
<tr><td>social</td><td>842</td></tr>
<tr><td>copywriting</td><td>825</td></tr>
<tr><td>ideas</td><td>380</td></tr>
<tr><td>bug-hunting</td><td>377</td></tr>
</table>

#### Conclusion
- The utopian project has reached over 3486 unique users over a time period of 290 days. During this time frame 38 075 votes were casted.
- It has taken about 6 months for voting to stabilise
- The top user received 1.35% of the total voting weight
- The top users received 0.96% of the total votes
- There is only a 7/20 overlap between top users based on voting weight and top users based on votes. Suggesting that quality outperforms quantity.
- The Pareto principle holds indicating a healthy system.
- In order development, analysis and translations are the most rewarding categories
- In order bug-hunting, development and graphics are the most popular categories.


#### Proof of Authorship
