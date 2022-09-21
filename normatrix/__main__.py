from normatrix.config.config import get_config

config = get_config()

if config.show_config:
    print(f"INFO: config = {config}")

if config.pass_test:
    pass
