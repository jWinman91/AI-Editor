import unittest
import os
from tempfile import NamedTemporaryFile
from typing import List

from utils.text_editor import Editor

class TestEditor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_config_file = NamedTemporaryFile(delete=False)
        self.temp_config_file.write(b"prompt_config: test_prompt_config\nllm_config: test_llm_config")
        self.temp_config_file.close()

    def tearDown(self):
        # Remove the temporary file after testing
        os.remove(self.temp_config_file.name)

    def test_load_yml(self):
        editor = Editor(self.temp_config_file.name)
        data = editor.load_yml(self.temp_config_file.name)
        self.assertIsInstance(data, dict)
        self.assertEqual(data["prompt_config"], "test_prompt_config")
        self.assertEqual(data["llm_config"], "test_llm_config")

    def test_static_context(self):
        key = "test_key"
        context = Editor.static_context(key)
        self.assertIn(key, context)
        self.assertIn("output", context)

    def test_build_prompt(self):
        editor = Editor(self.temp_config_file.name)
        input_text = "test_input"
        prompt_name = "test_prompt"
        prompt_instruction = {"Context": "test_context"}
        prompt = editor.build_prompt(input_text, prompt_name, prompt_instruction)
        self.assertIn(input_text, prompt)
        self.assertIn(prompt_name, prompt)
        self.assertIn("test_context", prompt)

    def test_get_response(self):
        # Write tests for get_response method
        pass

    def test_save_history(self):
        # Write tests for save_history method
        pass

    def test_edit_text_single_input(self):
        editor = Editor(self.temp_config_file.name)
        input_text = "test_input"
        edited_text = editor.edit_text(input_text)
        self.assertIsInstance(edited_text, str)
        # Add more assertions based on the expected behavior

    def test_edit_text_multiple_inputs(self):
        editor = Editor(self.temp_config_file.name)
        input_texts = ["test_input1", "test_input2"]
        edited_texts = editor.edit_text(input_texts)
        self.assertIsInstance(edited_texts, List)
        self.assertEqual(len(edited_texts), len(input_texts))
        # Add more assertions based on the expected behavior

if __name__ == '__main__':
    unittest.main()
