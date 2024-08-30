import pytest
import pandas as pd
from sentiment_analysis import analyze_sentiment, add_sentiment_scores

def test_analyze_sentiment():
    # Example input data for testing
    text = "The stock market is doing great!"
    
    # Expected sentiment score (e.g., 1 for positive sentiment, -1 for negative sentiment, 0 for neutral)
    expected_score = 1
    
    # Call the function to test
    result = analyze_sentiment(text)
    
    # Assert that the result matches the expected score
    assert result == expected_score, f"Expected {expected_score}, but got {result}"

def test_add_sentiment_scores():
    # Example DataFrame input for testing
    data = pd.DataFrame({
        'text': ["The stock market is doing great!", "I'm worried about the economy."]
    })
    
    # Call the function to test
    result_df = add_sentiment_scores(data)
    
    # Check that the sentiment scores column was added to the DataFrame
    assert 'sentiment_score' in result_df.columns, "sentiment_score column not found in result DataFrame"
    
    # Check that the sentiment scores are as expected
    expected_scores = [1, -1]  # Assuming the second text is negative
    assert result_df['sentiment_score'].tolist() == expected_scores, f"Expected {expected_scores}, but got {result_df['sentiment_score'].tolist()}"
