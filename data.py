import random
import pandas as pd
# Sample skills and names
skills_list = ['python', 'javascript', 'html', 'css', 'flask', 'django', 'react', 'nodejs', 'ml', 'ai', 'data analysis', 'sql', 'aws', 'docker']
names = [f'Freelancer {i}' for i in range(1, 1001)]

# Generate dataset
freelancers_data = []
for name in names:
    skills = ', '.join(random.sample(skills_list, k=random.randint(3, 6)))
    experience = round(random.uniform(1, 10), 1)  # years
    rating = round(random.uniform(3.5, 5.0), 2)  # out of 5
    cost_per_project = random.randint(200, 2000)
    freelancers_data.append({
        'name': name,
        'skills': skills,
        'experience': experience,
        'rating': rating,
        'cost_per_project': cost_per_project
    })

# Create DataFrame and save to CSV
freelancers_df = pd.DataFrame(freelancers_data)
freelancers_df.to_csv("freelancers.csv", index=False)