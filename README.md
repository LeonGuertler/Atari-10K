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
1. provide a screenshot of the specific figure to GPT-4-Vision
2. propmt: "The above is a screenshot of a figure in the atari 2600 {GAME-NAME} manual. I want to use the text transcription of the manual to better train AI agents, and to that end, need an as specific as possible caption of the image. Please consider be as specific in terms of location, description, and usefulness for actually playing the game as possible."

Below we provide an example of such an image-caption pair for Figure1 for the Mario Bros. game.

### Figure1
<p align="center">
  <img src="https://github.com/LeonGuertler/Atari-10K/blob/main/manuals/MarioBros/Figures/Figure1.png?raw=true" width="250">
</p>

### GTP-4-V Generated Caption (formatted for clarity)
<blockquote>
<i>
"In a screenshot from the Atari 2600 game 'Mario Bros', two gameplay sections are depicted, separated vertically:*
</i>
<ul>
<li><i>Upper Section:</i></li>
  <ul>
  <li><i>Labeled 'Mario'</i></li>
  <li><i>Displays a dark background, representing the game arena.</i></li>
  <li><i>Mario, dressed in his signature blue and red attire, stands on a platform on the left side.</i></li>
  <li><i>On the right, there's a small enemy creature with a crown.</i></li>
  <li><i>Above Mario is a scoreboard, showing '050400' points.</i></li>
  <li><i>Above the enemy, there's a numerical indication of the game round: '1'.</i></li>
  <li><i>Various platforms and ladders are seen, which players can utilize to navigate the level.</i></li>
  </ul>
<li><i>Lower Section:</i></li>
  <ul>
  <li><i>Labeled 'Luigi'</i></li>
  <li><i>Shows a similar dark game arena.</i></li>
  <li><i>Luigi, in green attire, is on the right side, near a turtle enemy.</i></li>
  <li><i>Another enemy, which looks like a coin, is located on a platform below Luigi.</i></li>
  <li><i>Luigi's score of '064010' points is shown on the bottom.</i></li>
  <li><i>The game round is also indicated as '1', shown near the bottom center.</i></li>
  <li><i>Like the upper section, multiple platforms and ladders are present, providing strategic pathways for the players.
</i></li>
</ul>
<i>
Both sections showcase the game's platform design, emphasizing level navigation, enemy evasion or defeat, and point accumulation."
</i>
</blockquote>

As can be seen in the above provided example, GPT-4-V adds additional information to the captions which is not provided in the image (esp. the last part). Since the purpose of this benchmark is to, among other things, leverage the internal world of LLMs, the additional information provided by GPT-4-V is not a problem, but rather a welcome addition. It is also worth pointing out that, as discussed above, the images a captioned based on a static prompt and the image, rather than the image in the context of the manual. For the image-caption paris we manually inspected, this does not seem to be an issue, but might nevertheless be a worthwile avenue for improving model performance (or better yet, accepting the full manual as a multi-model input).


