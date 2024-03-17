import launch

if not launch.is_installed("MoviePy"):
    launch.run_pip("install MoviePy==1.0.3", "requirements for xyzvideo")
