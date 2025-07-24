import os

# Base project structure
structure = [
    "CAMET/README.md",
    "CAMET/requirements.txt",
    "CAMET/environment.yml",
    "CAMET/setup.py",
    "CAMET/.gitignore",
    "CAMET/.env.example",
    "CAMET/pyproject.toml",

    "CAMET/camet/__init__.py",
    "CAMET/camet/models/__init__.py",
    "CAMET/camet/models/camet_transformer.py",
    "CAMET/camet/models/vision_encoder.py",
    "CAMET/camet/models/audio_encoder.py",
    "CAMET/camet/models/physio_encoder.py",
    "CAMET/camet/models/cultural_adapter.py",
    "CAMET/camet/models/attention_fusion.py",
    "CAMET/camet/models/baselines/__init__.py",
    "CAMET/camet/models/baselines/tensor_fusion_network.py",
    "CAMET/camet/models/baselines/multimodal_transformer.py",
    "CAMET/camet/models/baselines/misa.py",
    "CAMET/camet/models/baselines/single_modality.py",

    "CAMET/camet/data/__init__.py",
    "CAMET/camet/data/datasets.py",
    "CAMET/camet/data/preprocessing/__init__.py",
    "CAMET/camet/data/preprocessing/facial_processor.py",
    "CAMET/camet/data/preprocessing/audio_processor.py",
    "CAMET/camet/data/preprocessing/physio_processor.py",
    "CAMET/camet/data/preprocessing/cultural_encoder.py",
    "CAMET/camet/data/loaders.py",
    "CAMET/camet/data/augmentation.py",

    "CAMET/camet/training/__init__.py",
    "CAMET/camet/training/trainer.py",
    "CAMET/camet/training/losses.py",
    "CAMET/camet/training/metrics.py",
    "CAMET/camet/training/optimizers.py",
    "CAMET/camet/training/schedulers.py",
    "CAMET/camet/training/callbacks.py",

    "CAMET/camet/evaluation/__init__.py",
    "CAMET/camet/evaluation/evaluator.py",
    "CAMET/camet/evaluation/cultural_analysis.py",
    "CAMET/camet/evaluation/statistical_tests.py",
    "CAMET/camet/evaluation/ablation_studies.py",
    "CAMET/camet/evaluation/error_analysis.py",

    "CAMET/camet/utils/__init__.py",
    "CAMET/camet/utils/config.py",
    "CAMET/camet/utils/logging.py",
    "CAMET/camet/utils/visualization.py",
    "CAMET/camet/utils/checkpoint.py",
    "CAMET/camet/utils/reproducibility.py",
    "CAMET/camet/utils/device.py",

    "CAMET/camet/inference/__init__.py",
    "CAMET/camet/inference/predictor.py",
    "CAMET/camet/inference/benchmark.py",
    "CAMET/camet/inference/export.py",

    "CAMET/configs/model/camet_base.yaml",
    "CAMET/configs/model/camet_large.yaml",
    "CAMET/configs/model/baseline_configs/tfn.yaml",
    "CAMET/configs/model/baseline_configs/multimodal_transformer.yaml",
    "CAMET/configs/model/baseline_configs/misa.yaml",

    "CAMET/configs/data/meld.yaml",
    "CAMET/configs/data/iemocap.yaml",
    "CAMET/configs/data/emotiw.yaml",
    "CAMET/configs/data/custom_cultural.yaml",

    "CAMET/configs/training/default.yaml",
    "CAMET/configs/training/hyperparameter_search.yaml",
    "CAMET/configs/training/cross_validation.yaml",

    "CAMET/configs/evaluation/cultural_fairness.yaml",
    "CAMET/configs/evaluation/statistical_tests.yaml",
    "CAMET/configs/evaluation/ablation_studies.yaml",

    "CAMET/scripts/setup_environment.sh",
    "CAMET/scripts/download_datasets.py",
    "CAMET/scripts/preprocess_data.py",
    "CAMET/scripts/train_model.py",
    "CAMET/scripts/evaluate_model.py",
    "CAMET/scripts/run_experiments.py",
    "CAMET/scripts/hyperparameter_search.py",
    "CAMET/scripts/generate_results.py",
    "CAMET/scripts/benchmark_inference.py",

    "CAMET/experiments/runs/.gitkeep",
    "CAMET/experiments/baselines/.gitkeep",
    "CAMET/experiments/ablations/.gitkeep",
    "CAMET/experiments/cultural_analysis/.gitkeep",

    "CAMET/data/raw/meld/.gitkeep",
    "CAMET/data/raw/iemocap/.gitkeep",
    "CAMET/data/raw/emotiw/.gitkeep",
    "CAMET/data/raw/custom_cultural/.gitkeep",
    "CAMET/data/processed/facial_features/.gitkeep",
    "CAMET/data/processed/audio_spectrograms/.gitkeep",
    "CAMET/data/processed/physiological_signals/.gitkeep",
    "CAMET/data/processed/cultural_metadata/.gitkeep",
    "CAMET/data/splits/5fold_cv/.gitkeep",
    "CAMET/data/splits/cultural_groups/.gitkeep",

    "CAMET/models/pretrained/.gitkeep",
    "CAMET/models/camet/.gitkeep",
    "CAMET/models/baselines/.gitkeep",

    "CAMET/results/paper_figures/.gitkeep",
    "CAMET/results/tables/.gitkeep",
    "CAMET/results/statistical_tests/.gitkeep",
    "CAMET/results/cultural_analysis/.gitkeep",

    "CAMET/notebooks/01_data_exploration.ipynb",
    "CAMET/notebooks/02_preprocessing_analysis.ipynb",
    "CAMET/notebooks/03_model_development.ipynb",
    "CAMET/notebooks/04_training_analysis.ipynb",
    "CAMET/notebooks/05_results_visualization.ipynb",
    "CAMET/notebooks/06_cultural_bias_analysis.ipynb",

    "CAMET/tests/__init__.py",
    "CAMET/tests/test_models/test_camet_transformer.py",
    "CAMET/tests/test_models/test_encoders.py",
    "CAMET/tests/test_models/test_baselines.py",
    "CAMET/tests/test_data/test_preprocessing.py",
    "CAMET/tests/test_data/test_datasets.py",
    "CAMET/tests/test_data/test_loaders.py",
    "CAMET/tests/test_training/test_trainer.py",
    "CAMET/tests/test_training/test_losses.py",
    "CAMET/tests/test_training/test_metrics.py",
    "CAMET/tests/test_evaluation/test_evaluator.py",
    "CAMET/tests/test_evaluation/test_statistical_tests.py",

    "CAMET/docs/source/index.rst",
    "CAMET/docs/source/installation.rst",
    "CAMET/docs/source/quickstart.rst",
    "CAMET/docs/source/architecture.rst",
    "CAMET/docs/source/experiments.rst",
    "CAMET/docs/source/api/.gitkeep",
    "CAMET/docs/build/.gitkeep",
    "CAMET/docs/requirements.txt",

    "CAMET/docker/Dockerfile",
    "CAMET/docker/docker-compose.yml",
    "CAMET/docker/requirements-docker.txt",
    "CAMET/docker/scripts/entrypoint.sh",
    "CAMET/docker/scripts/run_experiments.sh"
]

def create_structure(paths):
    for path in paths:
        full_path = os.path.normpath(path)
        dir_name = os.path.dirname(full_path)
        os.makedirs(dir_name, exist_ok=True)
        if not full_path.endswith("/"):
            with open(full_path, "w", encoding="utf-8") as f:
                if os.path.basename(full_path).endswith(".py"):
                    f.write("# Placeholder Python file\n")
                elif os.path.basename(full_path).endswith(".md"):
                    f.write("# CAMET Project\n")
                elif os.path.basename(full_path).endswith(".yaml"):
                    f.write("# YAML Config Placeholder\n")
                elif os.path.basename(full_path).endswith(".sh"):
                    f.write("#!/bin/bash\n\n# Script Placeholder\n")
                else:
                    f.write("")  # blank file

if __name__ == "__main__":
    create_structure(structure)
    print("CAMET folder structure created successfully!")
