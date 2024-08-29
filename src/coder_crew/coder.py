from dotenv import load_dotenv
from aider.coders import Coder as AiderCoder
from aider.models import Model
from aider.io import InputOutput

class Coder:
    def __init__(self, model_name, fnames=None, stream=False, use_git=False, edit_format="diff"):
        # Load environment variables from .env file
        load_dotenv()

        # Initialize InputOutput
        self.io = InputOutput(yes=True, chat_history_file="aider_chat_history.txt")

        # Set up the model
        if model_name == "deepseek":
            self.main_model = Model("deepseek/deepseek-coder")
        elif model_name == "llama3.1-405b":
            self.main_model = Model("openrouter/meta-llama/llama-3.1-405b-instruct")
        else:
            self.main_model = Model(model_name)

        # Initialize Aider Coder
        self.coder = AiderCoder.create(
            main_model=self.main_model,
            fnames=fnames or [],
            io=self.io,
            stream=stream,
            use_git=use_git,
            edit_format=edit_format
        )

    def generate_code(self, instructions):
        """
        Generate code based on provided instructions.
        
        Args:
        instructions (str): Instructions for code generation
        
        Returns:
        str: Generated code or modifications
        """
        # Use Aider to generate code
        response = self.coder.run(instructions)

        return response

    def add_files(self, fnames):
        """
        Add files to be managed by the coder.
        
        Args:
        fnames (list): List of file paths to add
        """
        self.coder.add_files(fnames)

    def remove_files(self, fnames):
        """
        Remove files from being managed by the coder.
        
        Args:
        fnames (list): List of file paths to remove
        """
        self.coder.remove_files(fnames)
