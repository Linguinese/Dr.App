import pandas as pd

# List of input files
input_files = ["Put your csv files here"]

# Initialize an empty DataFrame to store results
all_results = pd.DataFrame()

# Loop through each file and process it
for input_file in input_files:
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Check if necessary columns exist
        required_columns = ['Pt Name', 'Date added', 'Dr. ', 'Trials']
        if not all(col in df.columns for col in required_columns):
            print(f"Skipping {input_file}: does not contain all required columns.")
            continue  # Skip to the next file if the columns are not present

        # Filter for entries where the doctor is "Hoyle" and Trials contain "Trials Dispensed"
        filtered_df = df[(df['Dr. '] == 'Dr. Name') & (df['Trials'].str.contains('Trials Dispensed', na=False))]

        # Select only the desired columns for display
        result = filtered_df[['Pt Name', 'Date added']]

        # Append the results to the all_results DataFrame
        all_results = pd.concat([all_results, result], ignore_index=True)

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Display the combined results
if not all_results.empty:
    print(all_results)
else:
    print("No results found for Dr. Name with Trials Dispensed in the provided files.")

# Optionally, if you want to save the result to a new CSV file
# all_results.to_csv('hoyles_trials_dispensed_combined.csv', index=False)