[app]
title = SciCalc
package.name = scicalc
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,txt,ttf
version = 0.1.0


requirements = python3,kivy
orientation = portrait
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1


[android]
# Target API is handled by the Docker image
android.arch = armeabi-v7a, arm64-v8a
