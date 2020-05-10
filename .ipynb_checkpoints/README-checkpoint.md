# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Luis Diaz, lmd003@ucsd.edu
- Catherine Hou, cahou@ucsd.edu
- Prithviraj Pahwa, pspahwa@ucsd.edu
- David Thierry, dthierry@ucsd.edu

## Abstract

(10 points) 

### Can we judge a movie by its cover?

The dataset that we are going to analyze comes from Kaggle (https://www.kaggle.com/neha1703/movie-genre-from-its-poster). These movie posters come from IMDB with features movie title, movie genre, and image link. We want to research whether we can classify these movies by their genre or year given their poster image. Our hypothesis is that we can classify which genre/year a movie comes from using features from the poster image. The features that we will use are hue, saturation, and brightness. Some more advanced features we can analyze are edges, entropy, and energy. skimage will be our main tool to process these images and extract their features. We will be using supervised learning to extract basic features to cluster these images by genre. We can plot these clusters onto a Bitmap plot. To analyze the accuracy of our classifier, we will plotting the accuracies by genre to see which genres the classifier works the best on. In the exercises we compared multiple features by plotting them onto different scatterplots, and we will expand on this by incorporating these features into a model. 
The cover images of movies are among the first things that consumers will see, so it is paramount for studios to create an art that can capture an audience's attention and convey what the movie is about. Movies have a rich culture with depth (going deep into history), and breadth (revelant worldwide). Personally we have all seen our fair share of movies, and this gives us a chance to analyze the features that go into their creation and whether these differences among genres are significant enough to be able to classify them.

## Data

(10 points) 

This section will describe your data and its origins. Each item should contain a name of the data source, a link to the source, and any necessary background information such as:
- What is your cultural data source? 
- When was it made? 
- Who created the works? 
- Is it digital native, or is it some kind of scan, recording, photo, etc., of an analog form? 

## Code

(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

- data acquisition/scraping
- cleaning
- analysis
- generating results. 

Link each of your notebooks or .py files within this section, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

[ETL Notebook](etl.ipynb) contains the code for extracting the links to the images, transforming the information into a dataframe/csv, and loading the images into a folder. It also includes the EDA, colorfulness, and corners feature extraction and analysis of the results.

## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

### General Movie EDA
![Dist Movies](results/dist_of_movies_over_each_decade.jpg)
<br>
*This is a distribution of movie counts over each decade. The increase could either be attributed to more movies being rated on the website or in general more movies being released.*
![Movie Counts](results/counts_of_movies_per_genre.jpg)
<br>
*These are the counts of movies recorded by IMDB for each decade. Action movies have a greater presence in the 70s, 80s, and 10s, while romance movies were more present in the 90s and dominated the 00s.*
![Top 10](results/top_ten_genres.jpg)
<br>
*These are the top ten recorded movie genres in IMDB and their associated counts.*

### Colorfulness of Movie Posters
![Whole Colorfulness](results/colorfulness.jpg)
<br>
*The average colorfulness for action and romance movies across the decades. Action movies usually have higher colorfulness values than romance movies do. With these two genres, there is less colorfulness in the 10s compared to the 70s.*
![Action Colorfulness](results/action_colorfulness.jpg)
![Romance Colorfulness](results/romance_colorfulness.jpg)
*These montages are of the movie image posters that had the top 9 (to the left) and the bottom 9 (to the right) colorfulness values for the action genre (on top) and for the romance genre (on bottom). The green numbers are the colorfulness values associated with each poster. We can see that the colorfulness for action tend to be higher than that for romance based on the top and bottom 9.*

### Corners of Movie Posters
![Whole Corners](results/corners.jpg)
*The average number of corners for action and romance movies across the decades. Action movies have consistently a slightly higher number of corners than romance movies. The number of corners detected by each decade does not seem to be changing significantly.*
![Action Corners](results/action_corners.jpg)
<br>
*This is a sample of an action movie poster where on the left is the original poster and on the right are the corners plotted in blue according to the Harris Corner Detection method.*
![Romance Corners](results/romance_corners.jpg)
<br>
*This is a sample of an romance movie poster where on the left is the original poster and on the right are the corners plotted in blue according to the Harris Corner Detection method. At least comparing these two alone, we can detect more corners in the action movie sample than in the romance movie sample.*

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

Provide an account of individual members and their efforts/contributions to the specific tasks you accomplished.

Catherine worked on the general movie EDA and the feature extraction/analysis for colorfulness and corner detection.

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)
- In addition to pandas, numpy, matplotlib, and seaborn, the [ETL Notebook](etl.ipynb) requires OpenCV, glob, skimage, and imutils.

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
- [Computing image "colorfulness"](https://www.pyimagesearch.com/2017/06/05/computing-image-colorfulness-with-opencv-and-python/) (a blog post from pyimageserach that computes the colorfulness metric described in  Hasler and Süsstrunk’s 2003 paper, [Measuring colorfulness in natural images.](https://infoscience.epfl.ch/record/33994/files/HaslerS03.pdf) 
- [Harris Corner Detection Documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html) from OpenCV that detects the corners in an image.