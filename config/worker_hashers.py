"""PBKDF2 de Django usando Web Crypto cuando CPython/WASM no incluye OpenSSL."""
import base64
import sys
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class WorkerPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def encode(self, password, salt, iterations=None):
        if sys.platform != "emscripten":
            return super().encode(password, salt, iterations)
        self._check_encode_args(password, salt)
        from js import crypto, Object, Uint8Array
        from pyodide.ffi import run_sync, to_js
        iterations = iterations or self.iterations
        parameters = to_js({"name": "PBKDF2", "hash": "SHA-256", "salt": salt.encode("utf-8"),
                            "iterations": iterations}, dict_converter=Object.fromEntries)
        key = run_sync(crypto.subtle.importKey("raw", to_js(password.encode("utf-8")),
                                              "PBKDF2", False, to_js(["deriveBits"])))
        derived = run_sync(crypto.subtle.deriveBits(parameters, key, 256))
        raw = Uint8Array.new(derived).to_py().tobytes()
        encoded = base64.b64encode(raw).decode("ascii").strip()
        return f"{self.algorithm}${iterations}${salt}${encoded}"
