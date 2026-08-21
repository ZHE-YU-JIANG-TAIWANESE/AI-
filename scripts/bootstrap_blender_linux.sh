#!/usr/bin/env bash
set -Eeuo pipefail

BLENDER_VERSION="${BLENDER_VERSION:-5.2.0}"
ROOT="${OCW_FORGE_ROOT:-$HOME/.local/share/open-character-workbench}"
APPS="$ROOT/apps"
BIN="$ROOT/bin"
TARGET="$APPS/blender-$BLENDER_VERSION"
ARCHIVE="$APPS/blender-$BLENDER_VERSION.tar.xz"

mkdir -p "$APPS" "$BIN"

if [ ! -x "$TARGET/blender" ]; then
  echo "[ocw] downloading Blender $BLENDER_VERSION"
  curl -fL --retry 3 --retry-delay 2 \
    "https://download.blender.org/release/Blender5.2/blender-${BLENDER_VERSION}-linux-x64.tar.xz" \
    -o "$ARCHIVE"
  rm -rf "$TARGET"
  mkdir -p "$TARGET"
  tar -xJf "$ARCHIVE" -C "$TARGET" --strip-components=1
  rm -f "$ARCHIVE"
fi

ln -sfn "$TARGET/blender" "$BIN/blender"
"$BIN/blender" --version | head -n 2

cat <<EOF

OCW Blender installed at:
  $BIN/blender

Add this to your shell PATH if desired:
  export PATH="$BIN:\$PATH"
EOF
