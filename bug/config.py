from hydra import compose, initialize
from omegaconf import OmegaConf, DictConfig
import hydra

with initialize(version_base="1.2", config_path="./configs/"):
    cfg = compose(config_name="params")
    print(OmegaConf.to_yaml(cfg, resolve=True))


    print(f"{cfg.data_sources.raw.data_dir_raw}")
    print(f"{cfg.data_sources.data.data_dir}")

# @hydra.main(version_base="1.2", config_path="./configs/", config_name="params")
# def my_app(cfg: DictConfig) -> None:
#     print(OmegaConf.to_yaml(cfg, resolve=True))


# if __name__ == "__main__":
#     my_app()