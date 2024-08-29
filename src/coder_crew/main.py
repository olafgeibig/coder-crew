from coder_crew.coder import Coder
def main():
    # Initialize the coder with desired model and options
    coder = Coder(
        model_name="deepseek",
        fnames=["example.py"],
        stream=False,
        use_git=False,
        edit_format="diff"
    )

    # Generate code based on instructions provided as an argument
    instructions = "Create a function that calculates the factorial of a number"
    result = coder.generate_code(instructions)
    print(result)

    # Add or remove files as needed
    # coder.add_files(["new_file.py"])
    # coder.remove_files(["example.py"])

if __name__ == "__main__":
    main()