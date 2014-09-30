from cx_Freeze import setup, Executable

executables = [
    Executable("linkinator.py",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="Linkinator",
      version="0.0.1",
      description="Linkinator",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )