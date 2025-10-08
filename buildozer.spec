[app]
title = SciCalc
package.name = scicalc
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,txt,ttf
version = 0.1.0

# Keep this small & pinned
requirements = python3,kivy==2.3.0,cython==0.29.36,setuptools<70

orientation = portrait
fullscreen = 0

# optional: speed up rebuilds
android.compile_options = release

# (You can leave other sections as defaults)

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Pin to modern but stable API/NDK that p4a supports well
android.api = 34
android.minapi = 24
android.ndk = 25.2.9519653
# Quiet license prompts
android.accept_sdk_license = True
