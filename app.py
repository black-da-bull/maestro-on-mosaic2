"""Repository-root entry point; shares the deployed runtime application."""
import importlib.util
import sys
from pathlib import Path

RUNTIME_ROOT = Path(__file__).resolve().parent / "runtime" / "maestro-workforce"
sys.path.insert(0, str(RUNTIME_ROOT))
spec = importlib.util.spec_from_file_location("maestro_mvp_app", RUNTIME_ROOT / "app.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
base_app = module.app

import audio_analysis_gateway


def app(environ, start_response):
    experimental = audio_analysis_gateway.handle_wsgi(environ, start_response)
    if experimental is not None:
        return experimental
    return base_app(environ, start_response)
