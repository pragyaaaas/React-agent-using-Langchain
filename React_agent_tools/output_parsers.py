from langchain.output_parsers import OutputParser
from typing import Any, Dict

class TranslationOutputParser(OutputParser):
    def parse(self, output: Dict[str, Any]) -> str:
        """
        Parses the output from the translate_text tool and formats it as a string.

        Args:
            output (Dict[str, Any]): The output from the translate_text tool.

        Returns:
            str: The formatted output string.
        """
        input_text = output["input_text"]
        target_language = output["target_language"]
        translated_text = output["result"]

        return f"The translation of '{input_text}' from English to {target_language} is: {translated_text}"
