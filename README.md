# Fire and Ice ADOFAI Project

AI-assisted **A Dance of Fire and Ice (ADOFAI)** chart generation project.

## Goal

User uploads an audio file. The system detects BPM, offset, beats and onsets, selects playable notes, generates a rhythm-correct ADOFAI track, validates it, and exports a complete `.adofai` chart package.

## Architecture

```text
audio file
  -> audio analysis: bpm, offset, beat grid, onsets, sections
  -> note selection: choose playable beat positions
  -> chart model: generate angleData and events
  -> ADOFAI writer: create .adofai JSON
  -> validator: repair or reject invalid charts