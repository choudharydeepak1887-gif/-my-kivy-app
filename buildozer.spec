name: Build Kivy APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev cmake libffi-dev libssl-dev
          pip install --upgrade pip
          pip install Cython==0.29.33 buildozer
      - name: Accept Android Licenses
        run: |
          mkdir -p ~/.android
          yes | sdkmanager --licenses || true
          mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea04e4b" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license-2 || true
      - name: Build APK
        run: |
          yes | buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-apk
          path: bin/*.apk
