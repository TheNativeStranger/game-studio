#!/usr/bin/env bash
# Finds the engine, runs what can run without a person, prints only the summary. Uses no tokens.
# Exit: 0 passed, 1 failed, 2 nothing could be run.
set -uo pipefail
log=$(mktemp)
trap 'rm -f "$log"' EXIT

finish() {
  grep -E -i 'tests? (run|passed|failed)|passed|failed|error' "$log" | tail -25
  if [ "$1" -ne 0 ]; then echo "--- last lines ---"; tail -25 "$log"; fi
  echo "EXIT: $1"
  exit "$1"
}

uproject=$(find . -maxdepth 1 -name '*.uproject' -print -quit)

if [ -f project.godot ]; then
  echo "ENGINE: Godot"
  godot_bin=$(command -v godot || command -v godot4 || true)
  if [ -z "$godot_bin" ] && [ -x /Applications/Godot.app/Contents/MacOS/Godot ]; then
    godot_bin=/Applications/Godot.app/Contents/MacOS/Godot
  fi
  if [ -z "$godot_bin" ]; then echo "NO_RUNNER: godot not found"; exit 2; fi
  if [ -f addons/gut/gut_cmdln.gd ]; then
    "$godot_bin" --headless -s addons/gut/gut_cmdln.gd -gexit >"$log" 2>&1
  else
    echo "NOTE: no test addon found, running a headless start only"
    "$godot_bin" --headless --quit >"$log" 2>&1
  fi
  finish $?
elif [ -f ProjectSettings/ProjectVersion.txt ]; then
  version=$(sed -n 's/^m_EditorVersion: //p' ProjectSettings/ProjectVersion.txt | tr -d '\r')
  echo "ENGINE: Unity $version"
  unity_bin="/Applications/Unity/Hub/Editor/$version/Unity.app/Contents/MacOS/Unity"
  if [ ! -x "$unity_bin" ]; then echo "NO_RUNNER: Unity $version not found"; exit 2; fi
  results=$(mktemp)
  "$unity_bin" -batchmode -nographics -projectPath . -runTests -testPlatform EditMode -testResults "$results" -logFile - >"$log" 2>&1
  code=$?
  grep -m1 '<test-run' "$results" | sed -E 's/.*(testcasecount="[0-9]+").*(result="[A-Za-z()]+").*(passed="[0-9]+").*(failed="[0-9]+").*/\1 \2 \3 \4/' || true
  rm -f "$results"
  finish "$code"
elif [ -n "$uproject" ]; then
  echo "ENGINE: Unreal ($uproject)"
  if [ -z "${UE_EDITOR_CMD:-}" ]; then echo "NO_RUNNER: set UE_EDITOR_CMD to UnrealEditor-Cmd"; exit 2; fi
  "$UE_EDITOR_CMD" "$PWD/$uproject" -ExecCmds="Automation RunTests Project; Quit" -unattended -nopause -nullrhi >"$log" 2>&1
  finish $?
elif [ -f package.json ]; then
  echo "ENGINE: web"
  if ! node -e 'process.exit(require("./package.json").scripts?.test ? 0 : 1)' 2>/dev/null; then
    echo "NO_RUNNER: package.json has no test script"; exit 2
  fi
  npm test --silent >"$log" 2>&1
  finish $?
fi
echo "NO_RUNNER: no game project found in $(pwd)"
exit 2
