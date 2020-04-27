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

## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

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

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
