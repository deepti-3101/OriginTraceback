# OrginTraceback
Hackathon Repo
Team Name:   
Team Members: 
 A Deepti, Dominic Walter T, Ahamed Aamina Banu Y, Saratha Selvi K, Aarka Christal Suja

Problem Statement : (INTL-DA-08)
Build a solution that is able to track the origin of a given social media post (provided as an input URL or content) and identify the account, along with its details, which posted it first on that particular platform

Presentation Video Link: https://www.youtube.com/watch?v=r-HmjKApXIs

# 1. Abstract:

Images/ videos of individuals, taken with or without consent and often of a sexually-explicit nature, are posted on various social media platforms as a tactic of abuse by perpetrators with the intent to harass, impersonate, humiliate and cause harm. Such content has a tendency to instantly become viral and causes a lot of distress to the victim.
Given a piece of text, image, or video snippet as input, we build a solution that can identify the person who was the first one to post it online on a particular social media platform.
We give a detailed report on how we reached a particular result.
This project will have a high real-time use as it solves one of the major problems faced by our society.

# 2. Introduction:

We tend to take advantage of the vast and interactive platform of social media, but we forget to notice the downside of it. Nowadays, even a single post can ruin a person’s life, and yet we have failed to stop it. So our project will be a milestone in making people’s lives better. Every day, we see hundreds of messages forwarded across the globe, and it is almost impossible for us to find the origin of it. Once any content is released, it is shared, re-posted, and forwarded many times than we can imagine. This becomes a vulnerability. Hence, we are proposing a way to find the origin of any post. Thus, we find the user responsible for releasing abusive content. Our project uses image hashing to identify and compare the content that is retrieved from any media. Further, using a real-time database the information is organized and stored. Finally, the data is mapped to its origin for the first time it was ever posted.










# 3. Techstack: 

Language: Python 3.0
Libraries: ImageHash, Ipyplot, Numpy, Pandas, BeautifulSoup



Python 3.0

Python is an interpreted high-level general-purpose programming language.
 Its design philosophy emphasizes code readability with its use of significant indentation.
Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for a small and large-scale project.
Python 3 is a new version of the language.
We considered python due to its richness in libraries and the flexibility offered by it.
Python also shines bright in the data science area as it has numerous built-in features which makes it easy to tackle the needs.

Libraries:

ImageHash

Image hashes tell whether two images look nearly identical. This is different from cryptographic hashing algorithms where tiny changes in the image give completely different hashes. In image fingerprinting, we actually want our similar inputs to have similar output hashes as well. The image hash algorithms (average, perceptual, difference, wavelet) analyze the image structure on luminance (without color information). The color hash algorithm analyses the color distribution and black & gray fractions (without position information).
	
Ipyplot

IPyPlot is a small python package offering fast and efficient plotting of images inside ipython Notebooks cells. It's using IPython with HTML for faster, richer, and more interactive ways of displaying big numbers of images.

Numpy
NumPy stands for Numerical Python. It is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, Fourier transform, and matrices. It is an open-source project and we can use it freely. In Python, we have lists that serve the purpose of arrays, but they are slow to process.NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

Pandas
pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open-source data analysis/manipulation tool available in any language

# 4. Solution Proposed:

# 4.1 Overall design:

Our algorithm is divided into four stages as follows: 
1. Data scraping
2. Sanitizing & Organising data
3. Origin Computation
4. Compiling Report.


# 4.1.1 Data Scraping:

# 4.1.1.1 Effective way of searching:

In order to make scraping for images more effective, we have developed an algorithm that uses hashtags ( # tags )  to navigate to the main page and narrows the scope of the search, this helps in reducing the waste of computational power spent on a broader search. However, if the algorithm cannot find any hashtags associated with the given post, it can get manual input from the user at the time of triggering else will launch a broader search based on location and other aspects



# 4.1.1.2  Data retrieved:

On exploring every new node we collect the following data for processing

Time and date of the post (if the post is relatively old, only the date)
The URL of the image involved in the post
Account username
Social interactions (number of likes and comments)
Hashtags used (or the equivalent - depending on the social media platform)

# 4.1.2 Sanitizing & Organising data

To process the data we collect, we first should organize the data. Considering the vast amounts of data we need to process, we build the solution in such a way that we collect data to a centralized server. This enables distributive computing, by sharing workloads between an array of computers. 

Our scheme is as follows :

# 4.1.2.1 Hashing:
To compare images between posts, we hash the images and compare the hash values, we designed special algorithms that use different hashing techniques to conclude whether two images are edits of the same post 

# 4.1.2.2 Database:

We are using Google’s Firebase Realtime Database as the centralized database solution for storing/retrieving node data and hash values for computation. This enables us to split work between different computers, improving the overall performance of our solution

# 4.1.2.3 Exporting node data:

Node data can be exported into JSON files after exploration directly. These datasets can be used for other analytics, and further analysis of the case depending upon the initial report and situation.

# 4.1.2.4 Data structure:

Project Bucket


      {
        “Search ID”:
        {
                “Root”: “URL”;
		“Nodes”:
                {
                       “HashValue1”: 
                       {
                              “Time”: “value”;
                              “Date”: “value”;
                              “LikesNo”: value;
                              “commentsNo”: value;
                              “SharesNo”: value;
                       };

                       “HashValue2”: {……….} 
               };
        };
     }


# Explanation: 

Root: 
Type
String
Content
URL of the given post



Nodes:
Type
JSON  
Content
a collection of all the scraped posts



Hash value: (with serial number)
Type
JSON  
Content
Data scrapping from a post represented by its unique hash 




# 4.1.3 Origin Computation:

To traceback to the original post, we have designed the algorithm as follows

After retrieving data from RTDB, hashes will be sequentially processed to sort it in chronological order based on the time and date, in case of unavailability of certain data, it will be computed based on other parameters like the number of comments, shares, likes, and etc, creating a tree structure representing the flow of posts. Eventually, the start will be converging to fewer nodes. We then calculate the probability of being the origin for every node based on parameters other.

# 4.1.4 Report:

After computation to share the conclusions, we procedurally generate an HTML document and a pdf. The HTML document contains a very detailed flow of posts and data represented by every node in the network in a human-readable format. It will also contain additional data retrieved by the system and tooltips justifying the node’s position in the graph. The Pdf file will have a summary of the search and conclusions, without displaying any data.


# 4.2 Accuracy and time:

In order to trace back to the origin, we need to search, index, and profile all the images under some constraints which take a tremendous amount of time and computation power, to tackle this we created different algorithms that balance the time and accuracy into different proportions, discussed more on the methods in the following section.

Accuracy: 

we have estimated the accuracy of the most accurate method of this solution as at least 89%. The actual numbers can only be calculated on the completion of this project. It also depends greatly on the hashing algorithms we use, so in order to improve the accuracy of the algorithms, we sanitize the input image we provide for hashing, more details are mentioned in the following sections.

# 4.3 Methods

Different methods we provide:

# Fastest Method
Looks for the exact image, audio, video file - fails with edits and compression
Uses a single hashing algorithm
Fastest of all three methods
Accuracy is less

# Normal Method
Uses two Hashing Algorithms
Validation of search and computation
Can tolerate minor compressions and edits
More accurate than the previous method

# Deep search 
Most accurate 
Takes more time relatively
Accounts major edits and compression
Uses several hashing techniques to validate results

# Additional Methods (Optional):
Search part of a picture (if the clue is suspected to be cropped picture)
Adds to additional time in computing results
A detailed report will be included with every branch
Grid Verification: splits the image into 3x3 grid and algorithm proceeds individually with every piece, this increases the chance of matching the edited pictures


# 4.4 Report of the search 

1. HTML file:

1.1. Display the processed information.
1.2. create a dynamic interactive graph to follow the flow of posts
	1.2.1. On hovering, it exposes the user to further data
1.3.The nodes are displayed as cards
	1.3.1. It shows the navigation of posts

	
2. Pdf-summary:

It contains a detailed report based on the algorithm executed. It gives the conclusion, final result of the search to the end-user. This does not expose any intermediate node data or branch decisions.

"OCR : Photo by TheMobilTrend on November 05, 2021. Photo by TheMobilTrend on November 05, 2021. themobiltrend's profile picture\" class=\"_6q-tv\" crossorigin=\"anonymous\" data-testid=\"user-avatar\" draggable=\"false\" src=\"https://instagram.fixm3-1.fna.fbcdn.net/v/t51.2885-19/147293119_262782585407971_6434223692277284646_n.jpg?stp=dst-jpg_s150x150&amp;cb=9ad74b5e-7e291d1f&amp;_nc_ht=instagram.fixm3-1.fna.fbcdn.net&amp;_nc_cat=107&amp;_nc_ohc=yrzk4N9QQY8AX_U6rWS&amp;edm=AABBvjUBAAAA&amp;ccb=7-4&amp;oh=681a95eee2bf96a19313c3b8e5401b7f&amp;oe=61B66FDC&amp;_nc_sid=83d603\"></a></div></div><div class=\"o-MQd z8cbW \"><div class=\"PQo_0 RqtMr\"><div class=\"e1e1d\"><span class=\"Jv7Aj mArmR MqpiF  \"><a class=\"sqdOP yWX7d     _8A5w5   ZIAjV \" href=\"/themobiltrend/\" tabindex=\"0\">themobiltrend</a></span></div><div class=\"bY2yH\"><div class=\"qvG_g\"><span class=\"RPhNB FLVQW  _7qOna\">•</span></div><button class=\"sqdOP yWX7d    y3zKF     \" type=\"button\">Follow</button></div></div><div class=\"M30cS\"><div></div><div class=\"JF9hh\"></div></div></div></header><div class=\"MEAGs\"><button class=\"wpO6b  \" type=\"button\"><div class=\"QBdPU \"><div class=\"             qF0y9          Igw0E   rBNOH          YBx95       _4EzTm                                                                                                              \" style=\"height: 24px; width: 24px;\"><svg aria-label=\"More Options\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"24\" role=\"img\" viewBox=\"0 0 24 24\" width=\"24\"><circle cx=\"12\" cy=\"12\" r=\"1.5\"></circle><circle cx=\"6.5\" cy=\"12\" r=\"1.5\"></circle><circle cx=\"17.5\" cy=\"12\" r=\"1.5\"></circle></svg></div></div></button></div></div></div><div class=\"eo2As  \"><section class=\"ltpMr  Slqrh\"><span class=\"fr66n\"><button class=\"wpO6b  \" type=\"button\"><div class=\"QBdPU B58H7\"><svg aria-label=\"Like\" class=\"_8-yf5 \" color=\"#8e8e8e\" fill=\"#8e8e8e\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z\"></path></svg></div><div class=\"QBdPU rrUvL\"><span class=\"\"><svg aria-label=\"Like\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z\"></path></svg></span></div></button></span><span class=\"_15y0l\"><button class=\"wpO6b  \" type=\"button\"><div class=\"QBdPU B58H7\"><svg aria-label=\"Comment\" class=\"_8-yf5 \" color=\"#8e8e8e\" fill=\"#8e8e8e\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path clip-rule=\"evenodd\" d=\"M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z\" fill-rule=\"evenodd\"></path></svg></div><div class=\"QBdPU rrUvL\"><svg aria-label=\"Comment\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path clip-rule=\"evenodd\" d=\"M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z\" fill-rule=\"evenodd\"></path></svg></div></button></span><span class=\"_5e4p\"><button class=\"wpO6b  \" type=\"button\"><div class=\"QBdPU B58H7\"><svg aria-label=\"Share Post\" class=\"_8-yf5 \" color=\"#8e8e8e\" fill=\"#8e8e8e\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M47.8 3.8c-.3-.5-.8-.8-1.3-.8h-45C.9 3.1.3 3.5.1 4S0 5.2.4 5.7l15.9 15.6 5.5 22.6c.1.6.6 1 1.2 1.1h.2c.5 0 1-.3 1.3-.7l23.2-39c.4-.4.4-1 .1-1.5zM5.2 6.1h35.5L18 18.7 5.2 6.1zm18.7 33.6l-4.4-18.4L42.4 8.6 23.9 39.7z\"></path></svg></div><div class=\"QBdPU rrUvL\"><svg aria-label=\"Share Post\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M47.8 3.8c-.3-.5-.8-.8-1.3-.8h-45C.9 3.1.3 3.5.1 4S0 5.2.4 5.7l15.9 15.6 5.5 22.6c.1.6.6 1 1.2 1.1h.2c.5 0 1-.3 1.3-.7l23.2-39c.4-.4.4-1 .1-1.5zM5.2 6.1h35.5L18 18.7 5.2 6.1zm18.7 33.6l-4.4-18.4L42.4 8.6 23.9 39.7z\"></path></svg></div></button></span><span class=\"wmtNn\"><div><div aria-disabled=\"false\" role=\"button\" tabindex=\"0\"><button class=\"wpO6b  \" type=\"button\"><div class=\"QBdPU B58H7\"><svg aria-label=\"Save\" class=\"_8-yf5 \" color=\"#8e8e8e\" fill=\"#8e8e8e\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M43.5 48c-.4 0-.8-.2-1.1-.4L24 29 5.6 47.6c-.4.4-1.1.6-1.6.3-.6-.2-1-.8-1-1.4v-45C3 .7 3.7 0 4.5 0h39c.8 0 1.5.7 1.5 1.5v45c0 .6-.4 1.2-.9 1.4-.2.1-.4.1-.6.1zM24 26c.8 0 1.6.3 2.2.9l15.8 16V3H6v39.9l15.8-16c.6-.6 1.4-.9 2.2-.9z\"></path></svg></div><div class=\"QBdPU rrUvL\"><svg aria-label=\"Save\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"24\" role=\"img\" viewBox=\"0 0 48 48\" width=\"24\"><path d=\"M43.5 48c-.4 0-.8-.2-1.1-.4L24 29 5.6 47.6c-.4.4-1.1.6-1.6.3-.6-.2-1-.8-1-1.4v-45C3 .7 3.7 0 4.5 0h39c.8 0 1.5.7 1.5 1.5v45c0 .6-.4 1.2-.9 1.4-.2.1-.4.1-.6.1zM24 26c.8 0 1.6.3 2.2.9l15.8 16V3H6v39.9l15.8-16c.6-.6 1.4-.9 2.2-.9z\"></path></svg></div></button></div></div></span></section><section class=\"EDfFK ygqzn\"><div class=\"             qF0y9          Igw0E     IwRSH      eGOV_     ybXk5   vwCYk                                                                                                               \"><div class=\"Nm9Fw\"><a class=\"zV_Nj\" href=\"/p/CV55qKrIPhg/liked_by/\" tabindex=\"0\"><span>71</span> likes</a></div></div></section><div class=\"EtaWk\"><ul class=\"XQXOT    pXf-y \"><div role=\"button\" class=\"ZyFrc\" tabindex=\"0\"><li class=\"gElp9 rUo9f  PpGvg \" role=\"menuitem\"><div class=\"P9YgZ\"><div class=\"C7I1f X7jCj\"><div class=\"Jv7Aj mArmR   pZp3x\"><div class=\"RR-M-  TKzGu  \" aria-disabled=\"true\" role=\"button\" tabindex=\"-1\"><canvas class=\"CfWVH\" height=\"42\" width=\"42\" style=\"position: absolute; top: -5px; left: -5px; width: 42px; height: 42px;\"></canvas><a class=\"_2dbep qNELH kIKUG\" href=\"/themobiltrend/\" tabindex=\"0\" style=\"width: 32px; height: 32px; display: block;\"> Az LG bejelentette, hogy William Cho stratégiai igazgatói posztja mellett december 1-jétől a vezérigazgatói teendőket is átveszi. 👨‍⚖️ \nCho korábban az LG North America elnökeként hat évig az általa létrehozott, új üzleti lehetőségek előmozdításáért felelős LG Business Incubation Center működéséért felelt, ami házon belüli projekteket és startup partnereket fog össze. 🤝 Kíváncsian várjuk, hogy milyen irányba fog tartani az LG Electronics a vezetése alatt. 🤔🤞👍\n.\n.\n.\n.\n.\n#lg #lgelectronics #williamcho #lgmagyarorszag #themobiltrend #mobil #mobilblog #mobilblogger #mobilhírek Lei Jun szerint 2-3 éven belül forgalomba kerülhet az első négykerekű, ami tisztán elektromos hajtást kap. 🔌⚡🚗 \nEnnek érdekében a vállalat egy hatalmas üzemet létesít Pekingben, ahol évi 300 ezer autó gyártására kerülhet sor.\nA legvalószínűbb, hogy 2024-ben gördülhetnek le az első modellek a gyártósorokról, ám azt egyelőre még nem tudni, hogy pontosan milyen típusú járművek lesznek. 🤔\nVajon a crossovereket célozza meg a Xiaomi, vagy marad a személyautóknál? 🤷\n.\n.\n.\n.\n.\n#xiaomi #xiaomicar #carfactory #peking #xiaomielectriccar #electriccar #themobiltrend #mobil #mobilblog #mobilhírek #elektromosauto A Sony még októberben jelentette be az Xperia Pro-I modellt, mely egy hatalmas &quot;1.0-type&quot; szenzorral fog érkezni és úgy tűnik, hogy a bemutatás dátuma is nyilvánossá vált. 🔍👀 \nAz Xperia Pro-I december 2.-án debütál az Egyesült Királyságban és Franciaországban, majd december 7.-én Németországban és december 10.-én az Egyesült Államokban. 📱☝️\n.\n.\n.\n.\n.\n#sony #sonymobile #sonyxperia #sonyxperiaproi #bejelentés #mobil #mobilblog #mobilblogger #mobilhírek #techhírek #themobiltrend A múlt héten jelent meg a TENAA-n az Oppo K9 család legújabb okostelefonja, mely kínai kiszivárogtatók szerint az Oppo K9X nevet kapja. 📱👀 Kialakításra a Realme Q3-ra hasonlít, de a burkolat alatt egy Dimensity 900-as lapkakészlet kapott helyet. 🔥\n.\n.\n.\n.\n.\n#oppo #oppok9 #oppok9x #k9x #oppomobiles #themobiltrend #mobil #mobilblog #mobilhírek #mobilblogger Egy újabb és sokak által régóta várt új funkció került beépítésre a Spotify alkalmazásba. 🎵🆕\nA legújabb frissítésnek köszönhetően az összes zeneszám teljes dalszövege elérhető a Spotifyon és nem csupán a Prémium felhasználók számára. 📃☝️\n.\n.\n.\n.\n.\n#spotify #spotifylyrics #lyrics #spotifynewfeature #themobiltrend #mobil #mobilblog #mobilhírek #mobilblogger Instagram\" class=\"s4Iyt\" src=\"/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png\" srcset=\"/static/images/web/mobile_nav_type_logo-2x.png/1b47f9d0e595.png 2x\"></div></div></a></div><div class=\"_0aCwM \"><input aria-label=\"Search input\" autocapitalize=\"none\" class=\"XTCLo x3qfX \" placeholder=\"Search\" type=\"text\" value=\"\"><div class=\"pbgfb\" role=\"button\" tabindex=\"0\"><div class=\"eyXLr\"><span class=\"_6RZXI coreSpriteSearchIcon\"></span><span class=\"TqC_a\">Search</span></div></div><div class=\"yPP5B\"></div></div><div class=\"ctQZg \"><div class=\"J5g42\"><div class=\"XrOey\"><div class=\"\"><a href=\"/\" tabindex=\"0\"><svg aria-label=\"Home\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"22\" role=\"img\" viewBox=\"0 0 48 48\" width=\"22\"><path d=\"M45.3 48H30c-.8 0-1.5-.7-1.5-1.5V34.2c0-2.6-2-4.6-4.6-4.6s-4.6 2-4.6 4.6v12.3c0 .8-.7 1.5-1.5 1.5H2.5c-.8 0-1.5-.7-1.5-1.5V23c0-.4.2-.8.4-1.1L22.9.4c.6-.6 1.5-.6 2.1 0l21.5 21.5c.4.4.6 1.1.3 1.6 0 .1-.1.1-.1.2v22.8c.1.8-.6 1.5-1.4 1.5zm-13.8-3h12.3V23.4L24 3.6l-20 20V45h12.3V34.2c0-4.3 3.3-7.6 7.6-7.6s7.6 3.3 7.6 7.6V45z\"></path></svg></a></div></div><div class=\"XrOey\"><a aria-label=\"Direct messaging – 0 new notifications link\" class=\"xWeGp\" href=\"/direct/inbox/\" tabindex=\"0\"><svg aria-label=\"Direct\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"22\" role=\"img\" viewBox=\"0 0 48 48\" width=\"22\"><path d=\"M47.8 3.8c-.3-.5-.8-.8-1.3-.8h-45C.9 3.1.3 3.5.1 4S0 5.2.4 5.7l15.9 15.6 5.5 22.6c.1.6.6 1 1.2 1.1h.2c.5 0 1-.3 1.3-.7l23.2-39c.4-.4.4-1 .1-1.5zM5.2 6.1h35.5L18 18.7 5.2 6.1zm18.7 33.6l-4.4-18.4L42.4 8.6 23.9 39.7z\"></path></svg></a></div><div class=\"XrOey\"><div class=\"vZuFV\"><button class=\"wpO6b ZQScA \" type=\"button\"><div class=\"QBdPU \"><svg aria-label=\"New post\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"22\" role=\"img\" viewBox=\"0 0 48 48\" width=\"22\"><path d=\"M31.8 48H16.2c-6.6 0-9.6-1.6-12.1-4C1.6 41.4 0 38.4 0 31.8V16.2C0 9.6 1.6 6.6 4 4.1 6.6 1.6 9.6 0 16.2 0h15.6c6.6 0 9.6 1.6 12.1 4C46.4 6.6 48 9.6 48 16.2v15.6c0 6.6-1.6 9.6-4 12.1-2.6 2.5-5.6 4.1-12.2 4.1zM16.2 3C10 3 7.8 4.6 6.1 6.2 4.6 7.8 3 10 3 16.2v15.6c0 6.2 1.6 8.4 3.2 10.1 1.6 1.6 3.8 3.1 10 3.1h15.6c6.2 0 8.4-1.6 10.1-3.2 1.6-1.6 3.1-3.8 3.1-10V16.2c0-6.2-1.6-8.4-3.2-10.1C40.2 4.6 38 3 31.8 3H16.2z\"></path><path d=\"M36.3 25.5H11.7c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h24.6c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5z\"></path><path d=\"M24 37.8c-.8 0-1.5-.7-1.5-1.5V11.7c0-.8.7-1.5 1.5-1.5s1.5.7 1.5 1.5v24.6c0 .8-.7 1.5-1.5 1.5z\"></path></svg></div></button></div></div><div class=\"XrOey\"><a href=\"/explore/\" tabindex=\"0\"><svg aria-label=\"Find people\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"22\" role=\"img\" viewBox=\"0 0 48 48\" width=\"22\"><path clip-rule=\"evenodd\" d=\"M24 0C10.8 0 0 10.8 0 24s10.8 24 24 24 24-10.8 24-24S37.2 0 24 0zm0 45C12.4 45 3 35.6 3 24S12.4 3 24 3s21 9.4 21 21-9.4 21-21 21zm10.2-33.2l-14.8 7c-.3.1-.6.4-.7.7l-7 14.8c-.3.6-.2 1.3.3 1.7.3.3.7.4 1.1.4.2 0 .4 0 .6-.1l14.8-7c.3-.1.6-.4.7-.7l7-14.8c.3-.6.2-1.3-.3-1.7-.4-.5-1.1-.6-1.7-.3zm-7.4 15l-5.5-5.5 10.5-5-5 10.5z\" fill-rule=\"evenodd\"></path></svg></a></div><div class=\"XrOey\"><a class=\"_0ZPOP kIKUG \" href=\"/accounts/activity/\"><svg aria-label=\"Activity Feed\" class=\"_8-yf5 \" color=\"#262626\" fill=\"#262626\" height=\"22\" role=\"img\" viewBox=\"0 0 48 48\" width=\"22\"><path d=\"M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z\"></path></svg></a><div class=\"poA5q\" style=\"margin-left: -423px;\"></div></div><div class=\"XrOey\"><div class=\"\"></div><span class=\"_2dbep qNELH\" role=\"link\" tabindex=\"0\" style=\"width: 22px; height: 22px;\"> "