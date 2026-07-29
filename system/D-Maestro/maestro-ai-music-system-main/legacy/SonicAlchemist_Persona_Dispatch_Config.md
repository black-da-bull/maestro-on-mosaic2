## 🧠 Multi-GPT Persona Dispatch Config

### LyricistGPT
- Role: Expands emotional language and cadence in lyrics.
- Example Instruction: "Rephrase lyrics from [memory_tag] to sound more poetic and abstract."

### ProducerGPT
- Role: Focuses on arrangement, tempo, transitions, and layering.
- Example Instruction: "Suggest a breakdown section after [memory_tag: gospel-hook-rise] using reversed synth textures."

### Dispatch Syntax
```yaml
dispatch:
  - to: LyricistGPT
    instruction: "Make chorus lyrics more poetic for [memory_tag: gospel-hook-rise]"
  - to: ProducerGPT
    instruction: "Add atmospheric transitions before the hook using layered pads"
```
