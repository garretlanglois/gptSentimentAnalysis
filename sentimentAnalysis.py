import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key

def analyze_sentiment(sentences):
    """
    Sends a list of sentences to ChatGPT and returns a list of sentiment scores.

    Parameters:
    sentences (list of str): List of sentences to analyze.

    Returns:
    list of dict: A list containing the sentence and its sentiment score.
    """
    results = []
    for sentence in sentences:
        
        prompt = f"Please analyze the sentiment of the following sentence and provide a sentiment score between -1 (negative) and 1 (positive). Just provide the numerical score.\n\nSentence: \"{sentence}\""

        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0,
        )

        
        sentiment_score = response.choices[0].message.content.strip()

        results.append({
            "sentence": sentence,
            "sentiment_score": sentiment_score
        })

    return results


if __name__ == "__main__":
    sentences = [
        "I absolutely love this product!",
        "I'm not happy with the service.",
        "This was okay, nothing special.",
    ]

    
    sentiment_scores = analyze_sentiment(sentences)

    
    for result in sentiment_scores:
        print(f"Sentence: {result['sentence']}\nSentiment Score: {result['sentiment_score']}\n")