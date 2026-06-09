# Fire and Ice ADOFAI Project

AI-assisted **A Dance of Fire and Ice (ADOFAI)** chart generation project.

The final product goal is:

> User uploads an audio file. The system detects beats and musical events, selects playable chart notes, generates a rhythm-correct ADOFAI track, validates it, and exports a complete `.adofai` chart package.

## Design principle

This project should not rely on a language model to directly guess a full `.adofai` file from raw audio. A reliable chart generator