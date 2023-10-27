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

!(alt text)[



TODO: Provide an example Image-Caption pair pointing out how GPT-4-V instroduces additional information (from it's pretraining) (which is no issue), and that the captions can probably be improved if more context from the manual is provided.



