"""Deployed WSGI entrypoint for the Maestro runtime plus audio-analysis gateway."""
from __future__ import annotations

import audio_analysis_gateway
import app as workforce_app

base_app = workforce_app.app


def app(environ, start_response):
    experimental = audio_analysis_gateway.handle_wsgi(environ, start_response)
    if experimental is not None:
        return experimental
    return base_app(environ, start_response)
