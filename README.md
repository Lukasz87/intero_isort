# Isort intero

This is a plugin for [isort](https://github.com/PyCQA/isort) that enforces import order following the coding guidelines in the [Odoo documentation](https://www.odoo.com/documentation/15.0/contributing/development/coding_guidelines.html#imports).

## How to Use

### Manually

1. **Install:**
    ```bash
    pip install git+https://github.com/Lukasz87/intero_isort
    ```

2. **Run file checking:**
    ```bash
    isort <path-to-file>/file_to_check.py
    ```

### Automatically - Using [pre-commit](https://pre-commit.com/):

1. **Add to `pre-commit-config.yaml`:**
    ```yaml
    - repo: https://github.com/Lukasz87/intero_isort
      rev: v1.0
      hooks:
        - id: isort
          args: ["--profile", "black", "--filter-files"]
    ```
   Repo (`repo`) URL and revision (`rev`) should be updated with the URL and version where you will be hosting the package, or you can use the provided ones.

## Optionally Configuration
Adding the `.isort.cfg` is not necessary because in package installation 
is added default config as you can see in `pyproject.toml` in section: `[tool.isort]`.

You can customize the behavior of the Intero isort by adding the `.isort.cfg` 
file in project. And it will be overwriting default configuration in .toml file:


```cfg
[settings]
known_odoo=odoo
known_odooaddons = odoo.addons
default_section=THIRDPARTY
sections=THIRDPARTY,ODOO,ODOO_ADDONS
multi_line_output=3
sort_order=intero
line_length=79
```

You can also put configuration directly to package in file `pyproject.toml` in the section
 [tool.isort] ( but you need to reinstall the package after it):


```toml
[tool.isort]
profile = "black"
known_odooaddons = "odoo.addons"
known_odoo = "odoo"
default_section = "THIRDPARTY"
sections = ["THIRDPARTY", "ODOO", "ODOOADDONS"]
multi_line_output = 3
sort_order = "intero"
line_length = 79
```
<span style="color: #D35400; font-weight: bold;">Warning:</span> .toml in [tool.isort] has a problem with "_" so you can't write "known_odoo_addons"; it should be "known_odooaddons".
