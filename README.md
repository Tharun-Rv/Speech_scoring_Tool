# Intern Case Study Scoring App (Google Colab)

This project contains a Streamlit-based case study scoring app. It is designed to be run easily in Google Colab without local setup.

## How to Run in Google Colab

1. Open the provided Colab notebook or clone this repository in Google Colab.
2. Run the notebook cells sequentially main.py1 and main.py2 andmain.py3 in each cell seperately.
3. The Streamlit app will launch within Colab using `ngrok` or similar service.
4. Use the interactive interface to paste transcripts and get scores based on the rubric.

## Features

- Uses Sentence Transformers for semantic similarity
- Grammar checking with LanguageTool
- Vocabulary richness and sentiment analysis
- Keyword and flow scoring with custom rules
- Fully runnable inside Google Colab environment

## Requirements

All necessary packages are installed within the notebook using `pip`. No local environment setup needed.

## Notes

- Internet connection is required for Colab and model downloads.
- Running Streamlit inside Colab may require use of services like `ngrok` for web tunneling.

## Contact

For support or questions, reach out to Tharun Ravi at tharunravi3009@gmail.com.
