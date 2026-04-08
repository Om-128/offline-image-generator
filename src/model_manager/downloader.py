from huggingface_hub import snapshot_download

from src.model_manager.constants import _MODEL_ID, _MODEL_DIR

import os

snapshot_download(
    repo_id=_MODEL_ID,
    local_dir=os.path.abspath(_MODEL_DIR),
    local_dir_use_symlinks=False,
)
