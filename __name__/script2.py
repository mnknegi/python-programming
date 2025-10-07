
import script1

# The if __name__ == "__main__": block inside script1 does not execute, because now __name__ is "script1".
# Avoid unwanted code execution on import.