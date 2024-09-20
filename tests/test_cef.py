import platform
import sys

from cefpython3 import cefpython as cef


def main() -> None:
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shut down all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(
        url=" https://www.google.com/",
        window_title="Olá, mundo! Este é o primeiro exemplo do CEF python",
    )
    cef.MessageLoop()
    cef.Shutdown()


def check_versions() -> None:
    ver = cef.GetVersion()
    print("[hello_world.py] CEF python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print(
        f"[hello_world.py] python {platform.python_version()} {platform.architecture()[0]}",
    )
    assert cef.__version__ >= "57.0", "CEF python v57.0+ required to run this"


if __name__ == "__main__":
    main()
