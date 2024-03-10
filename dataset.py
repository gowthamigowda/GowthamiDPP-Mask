import numpy as np
import pandas as pd

# Set the number of users and genres
num_users = 500
num_genres = 10

# Generate a random binary matrix representing user preferences
streaming_dataset = np.random.choice([0, 1], size=(num_users, num_genres), p=[0.7, 0.3])

# Create a DataFrame from the generated matrix
columns = [f"Genre{i}" for i in range(1, num_genres + 1)]
df = pd.DataFrame(streaming_dataset, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv("streaming_preferences_dataset.csv", index=False)

print("Dataset saved successfully.")
