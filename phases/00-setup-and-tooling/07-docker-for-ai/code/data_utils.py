from datasets import load_dataset


# Load a dataset
dataset = load_dataset("stanfordnlp/imdb", split="train")

print("Dataset:")
print(dataset)

# Show the first example
print("\nFirst example:")
print(dataset[0])

# Create an 80/20 train-test split
splits = dataset.train_test_split(test_size=0.2, seed=42)

print("\nTrain examples:", len(splits["train"]))
print("Test examples:", len(splits["test"]))
