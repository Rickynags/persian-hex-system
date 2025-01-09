import subprocess
import json

def run_test_py(input_number):
    """Run test.py with a specific input and capture the output."""
    try:
        result = subprocess.run(
            ["python", "test.py"],
            input=f"{input_number}\n",  # Send the input number to test.py
            text=True,
            capture_output=True,
            check=True
        )
        # Capture the output printed by test.py
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running test.py with input {input_number}: {e}")
        return None

def main():
    start = 0
    end = 999  # You can adjust this range to your needs
    output_file = "persian_hex_output.json"

    results = {}
    for num in range(start, end + 1):
        print(f"Processing number: {num}")
        output = run_test_py(num)
        if output:
            # Store the number and its output in the dictionary
            results[num] = output
        else:
            print(f"Skipping number {num} due to an error.")

    # Save results to a JSON file
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=2)

    print(f"Data successfully saved to {output_file}")

if __name__ == "__main__":
    main()
