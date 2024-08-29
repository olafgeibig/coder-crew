import pytest
from unittest.mock import Mock, patch
from coder_crew.coder import Coder

@pytest.fixture
def mock_aider_coder():
    with patch('coder_crew.coder.AiderCoder') as MockAiderCoder:
        mock_coder = Mock()
        MockAiderCoder.create.return_value = mock_coder
        yield mock_coder

def test_generate_code(mock_aider_coder):
    # Arrange
    coder = Coder(model_name="test_model")
    mock_aider_coder.run.return_value = "Generated code"
    instructions = "Create a function"

    # Act
    result = coder.generate_code(instructions)

    # Assert
    assert result == "Generated code"
    mock_aider_coder.run.assert_called_once_with(instructions)

def test_add_files(mock_aider_coder):
    # Arrange
    coder = Coder(model_name="test_model")
    files_to_add = ["file1.py", "file2.py"]

    # Act
    coder.add_files(files_to_add)

    # Assert
    mock_aider_coder.add_files.assert_called_once_with(files_to_add)

def test_remove_files(mock_aider_coder):
    # Arrange
    coder = Coder(model_name="test_model")
    files_to_remove = ["file1.py", "file2.py"]

    # Act
    coder.remove_files(files_to_remove)

    # Assert
    mock_aider_coder.remove_files.assert_called_once_with(files_to_remove)
