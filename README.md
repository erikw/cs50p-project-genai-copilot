# visa-tool

## Overview
The `visa-tool` is a Python application designed to assist users with questions related to visa issues. It provides information about visa requirements for different countries and includes a calculator to determine the last day one can stay in a country based on their entry date and the validity of their visa.

## Features
- **Visa Information**: Retrieve visa requirements and details for various countries.
- **Exit Day Calculator**: Calculate the last day one can stay in a country based on the date of entry and the number of valid days.

## Installation
To install the `visa-tool`, you need to have [Poetry](https://python-poetry.org/) installed. Once you have Poetry set up, you can install the project by running:

```bash
poetry install
```

## Usage
You can use the `visa-tool` in two ways: interactively or via command-line arguments.

### Interactive Mode
To start the interactive mode, run:

```bash
poetry run python -m visa_tool.cli interactive
```

### Command-Line Arguments
You can also access specific features directly from the command line. For example:

- To get visa information for a specific country:

```bash
poetry run python -m visa_tool.cli visa_info <country_name>
```

- To calculate the last exit day:

```bash
poetry run python -m visa_tool.cli calculate_exit_day <entry_date> <valid_days>
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.