# Atari-10K

Very much a work in progress.



Changes done to the text versions of the manuals:
- shorten it as much as possible via proper formatting (i.e. removing unnecessary indentation and line breaks)
- properly labeling all figures

TODO:
- For each manual, create a sub-folder containing the relevant figures, as well as a json with detailed captions for each figure.
- In the text version of each manual, reference the figure number (corresponding to the externally labeled image and json caption)
- double check that all game versions match those in the gymnasium environments
- for each game, create a small document pointing out which game-mode is used (the manual usually explains a number of different ones) and how the described controls translate to the one the AI is able to use.


For ease of use we provide both the pdf version of the manuals, as well as the text version. Where relevant, we have used GPT-4-Vision to caption the various Figures in the manuals for the text version (See Section X for the specific prompt used). The figures and generated captions can be found in the environment folders under "Figures" and "figure_captions.json" respectively (where the png name corresponds to the Json keys as well as the references to the figures in the .txt file).









GPT-4-Vision prompt:
The following captioning strategy was used for all relevant figures in the game manuals:
 - provide a screenshot of the specific figure to GPT-4-Vision
 - propmt: "The above is a screenshot of a figure in the atari 2600 {GAME-NAME} manual. I want to use the text transcription of the manual to better train AI agents, and to that end, need an as specific as possible caption of the image. Please consider be as specific in terms of location, description, and usefulness for actually playing the game as possible."
