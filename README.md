# Atari-10K

Very much a work in progress.
(TODO write proper intro)
For ease of use we provide both the pdf version of the manuals, as well as the text version. Where relevant, we have used GPT-4-Vision to caption the various Figures in the manuals for the text version (See "Image Captioning" below for the specific prompt used). The figures and generated captions can be found in the environment folders under "Figures" and "figure_captions.json" respectively (where the png name corresponds to the Json keys as well as the references to the figures in the .txt file).

Changes done to the text versions of the manuals:
- shorten it as much as possible via proper formatting (i.e. removing unnecessary indentation and line breaks)
- properly labeling all figures




TODO:
- double check that all game versions match those in the gymnasium environments
- for each game, create a small document pointing out which game-mode is used (the manual usually explains a number of different ones) and how the described controls translate to the one the AI is able to use.
- the GPT-4-V descriptions introduce a good amount of information that is not shown on the actual Figures. Maybe provide the before the figure and after the figure context as well.






## Image Captioning

GPT-4-Vision prompt:
The following captioning strategy was used for all relevant figures in the game manuals:
 - provide a screenshot of the specific figure to GPT-4-Vision
 - propmt: "The above is a screenshot of a figure in the atari 2600 {GAME-NAME} manual. I want to use the text transcription of the manual to better train AI agents, and to that end, need an as specific as possible caption of the image. Please consider be as specific in terms of location, description, and usefulness for actually playing the game as possible."

below we provide an example of such an image-caption pair for Figure1 for the Mario Bros. game.

Figure1:
![alt text](https://github.com/LeonGuertler/Atari-10K/blob/main/manuals/MarioBros/Figures/Figure1.png?raw=true)

GTP-4-V generated Caption (with adjusted formating for ease of reading):
In a screenshot from the Atari 2600 game 'Mario Bros', two gameplay sections are depicted, separated vertically:\nUpper Section:\n\tLabeled 'Mario'\n\tDisplays a dark background, representing the game arena.\n\tMario, dressed in his signature blue and red attire, stands on a platform on the left side.\n\tOn the right, there's a small enemy creature with a crown.\n\tAbove Mario is a scoreboard, showing '050400' points.\n\tAbove the enemy, there's a numerical indication of the game round: '1'.\n\tVarious platforms and ladders are seen, which players can utilize to navigate the level.\n\nLower Section:\n\tLabeled 'Luigi'\n\tShows a similar dark game arena.\n\tLuigi, in green attire, is on the right side, near a turtle enemy.\n\tAnother enemy, which looks like a coin, is located on a platform below Luigi.\n\tLuigi's score of '064010' points is shown on the bottom.\n\tThe game round is also indicated as '1', shown near the bottom center.\n\tLike the upper section, multiple platforms and ladders are present, providing strategic pathways for the players.\nBoth sections demonstrate the platform-based design of the game and emphasize the importance of navigating through the level, avoiding or defeating enemies, and accumulating points.


TODO: Provide an example Image-Caption pair pointing out how GPT-4-V instroduces additional information (from it's pretraining) (which is no issue), and that the captions can probably be improved if more context from the manual is provided.



