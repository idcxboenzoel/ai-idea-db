from setuptools import setup
from setuptools.command.install import install
import requests
import os

URL_WEB = os.getenv("IDEA_DB_WEB", "https://raw.githubusercontent.com/idcxboenzoel/ai-idea-db/main/ideas_db_web.json")
DEST_WEB = "ideas_db_web.json"

URL_LOCAL = os.getenv("IDEA_DB_WEB", "https://raw.githubusercontent.com/idcxboenzoel/ai-idea-db/main/ideas_db_local.json")
DEST_LOCAL = "ideas_db_local.json"

class CustomInstall(install):
    def run(self):
        print(f"📥 Mengunduh ide dari: {URL_WEB} dan {URL_LOCAL}")
        try:
            r = requests.get(URL_WEB)
            r.raise_for_status()
            with open(DEST_WEB, "w") as f:
                f.write(r.text)
            print(f"✅ Berhasil diunduh ke: {DEST_WEB}")
            
            r = requests.get(URL_LOCAL)
            r.raise_for_status()
            with open(DEST_LOCAL, "w") as f:
                f.write(r.text)
            print(f"✅ Berhasil diunduh ke: {DEST_LOCAL}")
        except Exception as e:
            print(f"❌ Gagal mengunduh: {e}")
        super().run()  # gunakan super() daripada install.run(self)

setup(
    name="idea-fetcher-db-json",
    version="0.1",
    install_requires=["requests", "app"],
    py_modules=[],
    cmdclass={'install': CustomInstall}
)