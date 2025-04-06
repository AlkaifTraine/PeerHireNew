import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model and data
model = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_csv('freelancers.csv')
df['text'] = df['skills'] + " | " + df['experience'].astype(str) + " yrs | Rating: " + df['rating'].astype(str)

# Encode freelancer profiles
freelancer_embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)

def recommend_freelancers(user_input, budget, timeline):
    user_embedding = model.encode([user_input])[0]

    similarities = cosine_similarity([user_embedding], freelancer_embeddings)[0]

    df['similarity'] = similarities
    df_filtered = df[df["cost_per_project"] <= budget].copy()
    df_filtered = df_filtered.sort_values(by="similarity", ascending=False).head(5)

    results = df_filtered[['name', 'skills', 'experience', 'rating', 'cost_per_project']].to_dict(orient='records')
    return results
