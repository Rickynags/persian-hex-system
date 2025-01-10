import argparse
import json
import subprocess
import os

JSON_FILE = "data.json"

EXAMPLES_DIR = "examples"

LANGUAGE_EXTENSIONS = {
    "python": ".py",
    "c": ".c",
    "cpp": ".cpp",
    "php": ".php",
    "ruby": ".rb",
    "bash": ".sh",
}

os.environ["PYTHONIOENCODING"] = "utf-8"

def load_json_data(file_path):
    """Load JSON data from the specified file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file '{file_path}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file '{file_path}'.")
        exit(1)


def detect_language_scripts(directory):
    """Detect language scripts in the specified directory."""
    scripts = {}
    for file_name in os.listdir(directory):
        for lang, ext in LANGUAGE_EXTENSIONS.items():
            if file_name.endswith(ext):
                scripts[lang] = os.path.join(directory, file_name)
    return scripts


def compile_and_run_c_cpp(script_path, number, lang):
    """Compile and run C or C++ script."""
    binary_name = f"persian_hex_{lang}"

    if not os.path.exists(binary_name):
        print("Compiling C/C++ script...")
        compile_cmd = f"gcc {script_path} libs/persian_hex{".c" if lang == "c" else ".cpp"} -o {binary_name}" if lang == "c" else f"g++ {script_path} -o {binary_name}"
        compile_result = subprocess.run(compile_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        if compile_result.returncode != 0:
            print(f"Error compiling {lang} script '{script_path}':\n{compile_result.stderr}")
            return None
    
    # print("Running compiled C/C++ script with " + str(number) + "...")
    run_result = subprocess.run([f"./{binary_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, input=str(number) + "\n", encoding="utf-8")
    if run_result.returncode != 0:
        print(f"Error running compiled {lang} binary for number {number}:\n{run_result.stderr}")
        return None

    return run_result.stdout.strip()


def run_language_script(script_path, number, language):
    """Run a language script with the input number."""
    if language in ["python", "php", "ruby", "bash"]:
        try:
            result = subprocess.run(
                [language, script_path],
                input=str(number) + "\n",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8"
            )
            if result.returncode != 0:
                print(f"Running {language} script: {script_path} with number {number}")
                print(f"Error running {language} script '{script_path}' for number {number}:\n{result.stderr}")
                return None
            return result.stdout.strip()
        except Exception as e:
            print(f"Error running {language} script '{script_path}': {e}")
            return None
    elif language in ["c", "cpp"]:
        return compile_and_run_c_cpp(script_path, number, language)
    else:
        print(f"Error: Unsupported language '{language}'")
        return None


def test_language(language, script_path, json_data):
    """Test a single language against the JSON data."""
    print(f"Testing language: {language}")
    for number, expected_output in json_data.items():
        script_output = run_language_script(script_path, number, language)
        if script_output != expected_output:
            print(f"Mismatch for number {number} in {language} script:")
            print(f"  Expected: '{expected_output}'")
            print(f"  Got:      '{script_output}'")
            return False
    print(f"All tests passed for {language}!")
    return True


def test_all_languages(language_scripts, json_data):
    """Test all detected languages."""
    for language, script_path in language_scripts.items():
        if not test_language(language, script_path, json_data):
            print(f"Tests failed for {language}.")
            return False
    print("All tests passed for all languages!")
    return True


def main():
    """Main function to handle arguments and run tests."""
    parser = argparse.ArgumentParser(description="Test Persian Hex scripts.")
    parser.add_argument(
        "language",
        nargs="?",
        help="Specify a language to test (e.g., 'python'). If omitted, all languages are tested."
    )
    args = parser.parse_args()

    json_data = load_json_data(JSON_FILE)

    language_scripts = detect_language_scripts(EXAMPLES_DIR)

    if args.language:
        language = args.language.lower()
        if language not in language_scripts:
            print(f"Error: Language '{language}' not supported or script not found.")
            print(f"Supported languages: {', '.join(language_scripts.keys())}")
            exit(1)
        script_path = language_scripts[language]
        test_language(language, script_path, json_data)
    else:
        test_all_languages(language_scripts, json_data)


if __name__ == "__main__":
    main()
