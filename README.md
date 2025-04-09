# CS50P Project - Visa Tool 🛂: GenAI version
This is a GenAI (Copilot) version of my handcrafted project [erikw/cs50p-project](https://github.com/erikw/cs50p-project). Just for fun, the code in this project was not used during or for the course. I just wanted to see how GenAI compare to manual coding using a rather minimal prompt.

The following user prompt fed to Copilot that generated this project:

> Create a python project using poetry. The project should be called visa-tool and be a tool that helps answering questions related to Visa issues. This would be showing the visa information per country, and a last exit day out of the country calculator. That calculator should take input the date of entry in the country, number of days the entry is valid for, and then output the last day one can stay in the country before one needs to exit. The program should support these features in an interactive mode, or by selecting a feature with arguments directly from CLI args.

Only three lines was needed to be manually fixed for the generated code to run. I would say the generated version of this project is maybe 70% as good as the one I wrote myself, but took only 5 minutes in total compared to two full working days!



> [!IMPORTANT]
> Everything below is generated:

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