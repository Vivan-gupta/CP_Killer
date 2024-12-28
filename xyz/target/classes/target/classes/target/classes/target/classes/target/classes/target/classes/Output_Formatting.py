def filter_out_code(response):
    import re

    # Use a regex pattern to find code blocks enclosed in triple backticks
    code_block_pattern = r"```(?:.|\n)*?```"
    code_blocks_found = len(re.findall(code_block_pattern, response)) > 0

    # Additional check for common programming keywords
    keywords_pattern = r"\b(def|class|import|for|if|else|while|return|\bint\b|\bfloat\b|\bstring\b|\bpublic\b|\bprivate\b)\b"
    keywords_found = len(re.findall(keywords_pattern, response, re.IGNORECASE)) > 2

    # Boolean result indicating if any code patterns are found
    code_detected = code_blocks_found or keywords_found

    # Remove code blocks
    filtered_response = re.sub(code_block_pattern, "", response)

    # Optionally, remove lines that start with a code identifier (e.g., "code:")
    code_line_pattern = r"^code:.*$"
    filtered_response = re.sub(code_line_pattern, "", filtered_response, flags=re.MULTILINE)

    return filtered_response.strip(), code_detected
